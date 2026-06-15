---
title: Configuration
description: The full Django Cheroot option reference — host, port, and thread-pool tuning — with defaults and guidance on choosing values.
sidebar:
  order: 4
---

Django Cheroot is configured entirely through the `cheroot` command's arguments — there are no extra settings to add to `settings.py`. This page is the complete reference.

## Option reference

| Option | Short | Long | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Host IP | `-ip` | `--hostip` | `str` | `127.0.0.1` | The address to bind. Use `0.0.0.0` to listen on all interfaces. |
| Port | `-p` | `--port` | `int` | `8000` | The TCP port to listen on. |
| Max worker threads | `-w` | `--maxthreads` | `int` | `40` | Upper bound on worker threads Cheroot will create under load. |
| Min threads | `-t` | `--minthreads` | `int` | `30` | Threads kept warm in the pool at all times. |
| Max queued connections | `-c` | `--connections` | `int` | `20` | Size of the OS listen backlog for pending connections. |

```bash
python manage.py cheroot \
  --hostip 0.0.0.0 \
  --port 8000 \
  --minthreads 30 \
  --maxthreads 40 \
  --connections 20
```

## How the options map to Cheroot

Internally the command builds a `cheroot.wsgi.Server` and starts it. The mapping is:

| Command option | `cheroot.wsgi.Server` parameter |
| --- | --- |
| `--hostip` + `--port` | `bind_addr` (the `(host, port)` tuple) |
| `--minthreads` | `numthreads` |
| `--maxthreads` | `max` |
| `--connections` | `request_queue_size` |

## Choosing thread-pool values

- **`--minthreads` / `--maxthreads`** size the worker pool. Cheroot keeps `minthreads` warm and grows toward `maxthreads` as concurrent requests arrive. For mostly-idle apps, keep `minthreads` low; for steady traffic, set it close to your typical concurrency so you don't pay thread-startup cost on every spike. `maxthreads` should account for your peak concurrent in-flight requests.
- **`--connections`** is the accept backlog — how many connections may wait for a free worker before the OS starts refusing them. Raise it if you see connection resets under bursty load.

:::tip
A reasonable starting point for a small-to-medium app is the defaults (`minthreads 30`, `maxthreads 40`, `connections 20`). Tune upward only after measuring; oversized thread pools waste memory without improving throughput for I/O-bound Django views.
:::

:::caution
Cheroot serves requests but does not, by itself, terminate TLS or efficiently serve large static files. In production, run it behind a reverse proxy (nginx, Caddy, Traefik) that handles HTTPS and static assets, and let Cheroot focus on your Django application — the same pattern used with Gunicorn or uWSGI.
:::

## Next steps

- [Basic](/django-cheroot/examples/basic/) — a minimal end-to-end setup.
- [Production behind a proxy](/django-cheroot/examples/production/) — running Cheroot behind nginx.
