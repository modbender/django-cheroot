---
title: Production Behind a Proxy
description: Run Django Cheroot behind an nginx reverse proxy that terminates TLS and serves static files, with Cheroot focused on the Django app.
sidebar:
  order: 3
---

Cheroot is a capable WSGI application server, but like Gunicorn or uWSGI it isn't meant to face the public internet directly. The standard pattern is to put a reverse proxy in front of it to terminate TLS, serve static files, and forward dynamic requests to Cheroot.

## 1. Run Cheroot on a local port

Bind Cheroot to localhost so only the proxy on the same host can reach it:

```bash
python manage.py cheroot --hostip 127.0.0.1 --port 8000 --minthreads 50 --maxthreads 100
```

In a real deployment you'd run this under a process supervisor (systemd, Supervisor, or a container's entrypoint) so it restarts on failure.

### Example systemd unit

```ini
# /etc/systemd/system/myproject.service
[Unit]
Description=MyProject (Django via Cheroot)
After=network.target

[Service]
User=www-data
WorkingDirectory=/srv/myproject
Environment=DJANGO_SETTINGS_MODULE=myproject.settings
ExecStart=/srv/myproject/.venv/bin/python manage.py cheroot --hostip 127.0.0.1 --port 8000
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## 2. Front it with nginx

Let nginx terminate TLS, serve `STATIC_ROOT` directly, and proxy everything else to Cheroot:

```nginx
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate     /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location /static/ {
        alias /srv/myproject/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 3. Collect static files

nginx serves static assets, so build them once on deploy:

```bash
python manage.py collectstatic --noinput
```

:::tip
Since nginx sets `X-Forwarded-Proto`, configure Django to trust it so `request.is_secure()` and HTTPS redirects work correctly:

```python
# settings.py
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
```
:::

:::caution
Set `DEBUG = False` and a correct `ALLOWED_HOSTS` in production. Cheroot serves exactly what your WSGI app produces — it won't mask an insecure Django configuration.
:::

## Next steps

- [Custom thread pool](/django-cheroot/examples/custom-threads/) — size the worker pool for your traffic.
- [Configuration](/django-cheroot/configuration/) — the full option reference.
