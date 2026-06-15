# Django Cheroot

Django Cheroot provides a bridge to use [Cheroot](https://github.com/cherrypy/cheroot), the high-performance, pure-Python HTTP server used by CherryPy, to serve your Django WSGI application.

_An alternative to other WSGI servers like Gunicorn, uWSGI, etc._

## Documentation

Full documentation lives at **[modbender.in/django-cheroot](https://modbender.in/django-cheroot/)**.

## Install

```shell
pip install django-cheroot
```

In `settings.py`, add the app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    "django_cheroot",
]
```

## Usage

The simplest usage, with default settings:

```shell
python manage.py cheroot
```

With explicit arguments (these are the defaults):

```shell
python manage.py cheroot -ip 127.0.0.1 -p 8000 -w 40 -t 30 -c 20
```

```shell
python manage.py cheroot --hostip 127.0.0.1 --port 8000 --maxthreads 40 --minthreads 30 --connections 20
```

## Arguments

| Name                       | Short | Long          | Type | Default   |
| -------------------------- | ----- | ------------- | ---- | --------- |
| IP Address                 | -ip   | --hostip      | str  | 127.0.0.1 |
| Port                       | -p    | --port        | int  | 8000      |
| Max Worker Threads         | -w    | --maxthreads  | int  | 40        |
| Min Threads in Thread Pool | -t    | --minthreads  | int  | 30        |
| Max Queued Connections     | -c    | --connections | int  | 20        |

## Compatibility

| | Supported |
| --- | --- |
| Python | 3.8+ |
| Django | 4.2, 5.x, 6.0 |
| Cheroot | 10+ |
