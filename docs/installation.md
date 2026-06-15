---
title: Installation
description: Install Django Cheroot from PyPI and register it in your Django project's INSTALLED_APPS.
sidebar:
  order: 2
---

Getting Django Cheroot running takes two steps: install the package, then register the app.

## 1. Install the package

```bash
pip install django-cheroot
```

This pulls in [Cheroot](https://github.com/cherrypy/cheroot) automatically. If you use a `requirements.txt`, add:

```text
django-cheroot
```

## 2. Register the app

Add `django_cheroot` to `INSTALLED_APPS` in your project's `settings.py`:

```python
INSTALLED_APPS = [
    # ... your other apps
    "django_cheroot",
]
```

Registering the app is what makes the `cheroot` management command discoverable. With it in place, the command shows up alongside Django's built-in commands:

```bash
python manage.py cheroot --help
```

## Requirements

| | Supported |
| --- | --- |
| Python | 3.8 or newer |
| Django | 4.2, 5.x, or 6.0 |
| Cheroot | 10 or newer (installed automatically) |

:::tip
Django Cheroot serves the WSGI application returned by `django.core.wsgi.get_wsgi_application()`, which respects your `DJANGO_SETTINGS_MODULE` and `WSGI_APPLICATION` settings — exactly like any other WSGI server. There's nothing extra to configure for it to find your app.
:::

## Next steps

- [Usage](/django-cheroot/usage/) — start the server and pass arguments.
- [Configuration](/django-cheroot/configuration/) — the full option reference.
