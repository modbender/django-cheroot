---
title: Basic
description: A minimal end-to-end example — install Django Cheroot, register the app, and serve a Django project with one command.
sidebar:
  order: 1
---

The smallest complete setup: install the package, register the app, and run the server.

## 1. Install

```bash
pip install django-cheroot
```

## 2. Register the app

```python
# settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cheroot",
]
```

## 3. Serve the project

```bash
python manage.py cheroot
```

You'll see Cheroot start up and begin serving on `http://127.0.0.1:8000`. Open that URL in a browser and you'll get the same response your Django project serves under any other WSGI server.

Stop the server with `Ctrl+C`.

:::tip
Because Django Cheroot serves the real WSGI application (not Django's development `runserver`), it's a closer match to how your app behaves in production — useful for catching WSGI-specific issues before you deploy.
:::

## Next steps

- [Custom thread pool](/django-cheroot/examples/custom-threads/) — tune the worker pool for your workload.
- [Production behind a proxy](/django-cheroot/examples/production/) — run Cheroot behind nginx.
