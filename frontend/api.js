/* Shared client for the event API. Set window.EVENT_API_BASE_URL before this
   file to override the deployed backend during local development. */
(function (window) {
  const defaultBaseUrl = 'https://zero5nov-workshop.onrender.com';
  const baseUrl = (window.EVENT_API_BASE_URL || localStorage.getItem('eventApiBaseUrl') || defaultBaseUrl).replace(/\/$/, '');
  const tokenKey = 'eventpulse.accessToken';

  function getToken() {
    return localStorage.getItem(tokenKey) || '';
  }

  function setToken(value) {
    const token = (value || '').trim().replace(/^Bearer\s+/i, '');
    if (token) localStorage.setItem(tokenKey, token);
    else localStorage.removeItem(tokenKey);
    return token;
  }

  async function request(path, options) {
    const config = options || {};
    const headers = new Headers(config.headers || {});
    if (config.body && !headers.has('Content-Type')) headers.set('Content-Type', 'application/json');
    const token = config.token || getToken();
    if (token) headers.set('Authorization', 'Bearer ' + token.replace(/^Bearer\s+/i, ''));

    const response = await fetch(baseUrl + path, { ...config, headers });
    const text = await response.text();
    let data = null;
    try { data = text ? JSON.parse(text) : null; } catch (_) { data = text; }
    if (!response.ok) {
      const error = new Error((data && data.error) || ('Request failed with HTTP ' + response.status));
      error.status = response.status;
      error.data = data;
      throw error;
    }
    return data;
  }

  window.EventApi = {
    baseUrl,
    getToken,
    setToken,
    clearToken: () => localStorage.removeItem(tokenKey),
    request,
    getEvents: () => request('/api/events'),
    getEvent: (id) => request('/api/events/' + encodeURIComponent(id)),
    register: (eventId, fields) => request('/api/registrations', {
      method: 'POST',
      body: JSON.stringify({ event_id: eventId, ...(fields || {}) })
    }),
    getMyRegistrations: () => request('/api/me/registrations'),
    getEventRegistrations: (eventId) => request('/api/events/' + encodeURIComponent(eventId) + '/registrations')
  };
})(window);
