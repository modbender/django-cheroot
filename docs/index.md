---
title: Django Cheroot
description: Serve your Django WSGI application with Cheroot, the high-performance, pure-Python HTTP server from CherryPy, via a single management command.
sidebar:
  order: 1
---

Django Cheroot lets you serve a Django project with [Cheroot](https://github.com/cherrypy/cheroot) — the high-performance, pure-Python HTTP server that powers CherryPy — through a single `manage.py cheroot` management command.

It's a small, dependency-light alternative to WSGI servers like Gunicorn or uWSGI. Because Cheroot is pure Python, it runs anywhere Python does (including Windows), with no C build toolchain and no extra process manager to wire up.

## Key features

- **One command** — add the app to `INSTALLED_APPS` and run `python manage.py cheroot`. No config files, no separate launcher.
- **Pure Python** — Cheroot has no compiled extensions, so it installs and runs cleanly on Linux, macOS, and Windows.
- **Tunable thread pool** — control the minimum/maximum worker threads and the queued-connection backlog straight from the command line.
- **Familiar WSGI** — it serves the exact same WSGI application Django builds for any other server, so behavior matches production.

## A 30-second taste

Install it:

```bash
pip install django-cheroot
```

Register the app in `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    "django_cheroot",
]
```

Serve your project:

```bash
python manage.py cheroot
```

That starts Cheroot on `http://127.0.0.1:8000` serving your Django WSGI application.

## Compatibility

| | Supported |
| --- | --- |
| Django Cheroot | 1.x |
| Python | 3.8+ |
| Django | 4.2, 5.x, and 6.0 |
| Cheroot | 10+ |

:::caution
Cheroot is a WSGI HTTP server, not a hardened edge server. For production it's common to run it behind a reverse proxy (nginx, Caddy) that terminates TLS and serves static files, the same way you would front Gunicorn.
:::

## Where to next

- [Installation](/django-cheroot/installation/) — install the package and register the app.
- [Usage](/django-cheroot/usage/) — run the `cheroot` command and its arguments.
- [Configuration](/django-cheroot/configuration/) — every command-line option and its default.
