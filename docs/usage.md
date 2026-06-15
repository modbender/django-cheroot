---
title: Usage
description: Run the cheroot management command to serve your Django project, with optional flags for host, port, and thread-pool tuning.
sidebar:
  order: 3
---

Once the app is registered, you serve your project with a single management command.

## Run the server

```bash
python manage.py cheroot
```

This starts Cheroot on `http://127.0.0.1:8000`, serving your Django WSGI application with the default thread-pool settings. Press `Ctrl+C` to stop it.

## Command-line arguments

Every argument is optional and has both a short and a long form. Passing none uses the defaults shown below.

| Argument | Short | Long | Type | Default |
| --- | --- | --- | --- | --- |
| Host IP | `-ip` | `--hostip` | `str` | `127.0.0.1` |
| Port | `-p` | `--port` | `int` | `8000` |
| Max worker threads | `-w` | `--maxthreads` | `int` | `40` |
| Min threads in the pool | `-t` | `--minthreads` | `int` | `30` |
| Max queued connections | `-c` | `--connections` | `int` | `20` |

The two commands below are equivalent — they just spell the same defaults with short and long flags:

```bash
python manage.py cheroot -ip 127.0.0.1 -p 8000 -w 40 -t 30 -c 20
```

```bash
python manage.py cheroot --hostip 127.0.0.1 --port 8000 --maxthreads 40 --minthreads 30 --connections 20
```

## Common invocations

Bind to all interfaces (so the server is reachable from other machines or containers):

```bash
python manage.py cheroot --hostip 0.0.0.0 --port 8000
```

Run on a different port:

```bash
python manage.py cheroot -p 9000
```

:::caution
Binding to `0.0.0.0` exposes the server on every network interface. Only do this behind a firewall or reverse proxy — never expose Cheroot directly to the public internet without one.
:::

## What the flags map to

The thread-pool flags map directly onto Cheroot's `wsgi.Server`:

- `--minthreads` → `numthreads`: the minimum number of worker threads kept in the pool.
- `--maxthreads` → `max`: the maximum number of worker threads Cheroot will spin up under load.
- `--connections` → `request_queue_size`: how many incoming connections may sit in the OS accept queue before new ones are refused.

See [Configuration](/django-cheroot/configuration/) for guidance on choosing values, and [Examples](/django-cheroot/examples/basic/) for end-to-end recipes.
