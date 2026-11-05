"""Event registration API backed by Supabase."""

import os
from functools import wraps
from typing import Any, Callable

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from postgrest import APIError
from supabase import Client, create_client

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

app = Flask(__name__)
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("SUPABASE_URL and SUPABASE_KEY must be set in .env")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = os.environ.get("FRONTEND_ORIGIN", "*")
    response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.route("/api/<path:_path>", methods=["OPTIONS"])
def preflight(_path):
    return ("", 204)


def api_error(message: str, status: int):
    return jsonify({"error": message}), status


def auth_required(view: Callable):
    @wraps(view)
    def wrapped(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        scheme, _, token = header.partition(" ")
        if scheme.lower() != "bearer" or not token:
            return api_error("Authentication required", 401)
        try:
            user = supabase.auth.get_user(token).user
        except Exception:
            return api_error("Invalid or expired access token", 401)
        if not user:
            return api_error("Invalid or expired access token", 401)
        return view(user, *args, **kwargs)

    return wrapped


def handle_supabase_error(error: APIError):
    code = getattr(error, "code", None)
    if code == "23505":
        return api_error("Already registered for this event", 409)
    if code in {"PGRST116", "404"}:
        return api_error("Not found", 404)
    app.logger.exception("Supabase request failed")
    return api_error("Backend data request failed", 500)

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        response = supabase.table('users').select('*').execute()

        return jsonify({
            "status": "success",
            "users": response.data
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
@app.get("/")
def index():
    return jsonify({"service": "events-api", "status": "ok"})


@app.get("/api/events")
def list_events():
    try:
        result = supabase.table("events").select("*").execute()
        return jsonify(result.data or [])
    except APIError as error:
        return handle_supabase_error(error)


@app.get("/api/events/<event_id>")
def get_event(event_id: str):
    try:
        result = supabase.table("events").select("*").eq("event_id", event_id).maybe_single().execute()
        if not result.data:
            return api_error("Event not found", 404)
        return jsonify(result.data)
    except APIError as error:
        return handle_supabase_error(error)


@app.post("/api/registrations")
@auth_required
def create_registration(user: Any):
    body = request.get_json(silent=True) or {}
    event_id = body.get("event_id", body.get("eventId"))
    if not event_id:
        return api_error("event_id is required", 400)
    payload = {"event_id": event_id, "user_id": user.id}
    for field in ("name", "email", "notes"):
        if field in body:
            payload[field] = body[field]
    try:
        event = supabase.table("events").select("event_id").eq("event_id", event_id).maybe_single().execute()
        if not event.data:
            return api_error("Event not found", 404)
        result = supabase.table("registrations").insert(payload).execute()
        return jsonify(result.data[0] if result.data else payload), 201
    except APIError as error:
        return handle_supabase_error(error)


@app.get("/api/me/registrations")
@auth_required
def my_registrations(user: Any):
    try:
        result = supabase.table("registrations").select("*").eq("user_id", user.id).execute()
        return jsonify(result.data or [])
    except APIError as error:
        return handle_supabase_error(error)


@app.get("/api/events/<event_id>/registrations")
@auth_required
def event_registrations(user: Any, event_id: str):
    try:
        event = supabase.table("events").select("*").eq("event_id", event_id).maybe_single().execute()
        if not event.data:
            return api_error("Event not found", 404)
        owner_id = event.data.get("organizer_id") or event.data.get("student_id")
        if owner_id != user.id:
            return api_error("Only the event organizer can view attendees", 403)
        result = supabase.table("registrations").select("*").eq("event_id", event_id).execute()
        return jsonify(result.data or [])
    except APIError as error:
        return handle_supabase_error(error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "9810")), debug=True)
