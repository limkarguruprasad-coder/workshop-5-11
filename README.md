# Events API

Flask + Supabase backend prepared for deployment on Render.

## Deploy on Render

1. Push this project to a GitHub/GitLab repository.
2. In Render, choose **New > Blueprint** and select the repository.
3. Render will read `render.yaml` and create the web service.
4. Enter these environment variables when prompted:
   - `SUPABASE_URL`: your Supabase project URL
   - `SUPABASE_KEY`: your Supabase anon/service key, according to your RLS setup
   - `FRONTEND_ORIGIN`: the deployed frontend origin, or `*` during development
5. Deploy and use the generated Render URL as the backend base URL.

The service starts with Gunicorn and listens on Render's `$PORT` automatically.

## Local run

From the project root:

```powershell
& .\my_backend\venv\Scripts\python.exe .\my_backend\app.py
```

The API is available at `http://localhost:9810` by default.

## Endpoints

- `GET /api/events`
- `GET /api/events/<id>`
- `POST /api/registrations` (Bearer token required)
- `GET /api/me/registrations` (Bearer token required)
- `GET /api/events/<id>/registrations` (event organizer only)

The Supabase database should contain `events` and `registrations` tables. The
event attendee authorization expects `events.organizer_id`; registrations use
`event_id` and `user_id`.
