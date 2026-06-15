---
title: Custom Thread Pool
description: Tune Cheroot's worker thread pool and connection backlog from the command line for your app's concurrency profile.
sidebar:
  order: 2
---

Django Cheroot exposes Cheroot's thread-pool controls directly, so you can size the server for your workload without touching Python.

## Bind publicly on a custom port

To make the server reachable from outside the local machine (for example inside a container), bind to all interfaces:

```bash
python manage.py cheroot --hostip 0.0.0.0 --port 8080
```

:::caution
`0.0.0.0` listens on every network interface. Keep it behind a firewall or reverse proxy — don't expose Cheroot directly to the public internet.
:::

## Tune the worker pool

For a busier app, grow the pool and the connection backlog:

```bash
python manage.py cheroot \
  --hostip 0.0.0.0 \
  --port 8080 \
  --minthreads 50 \
  --maxthreads 100 \
  --connections 50
```

What each flag does:

- `--minthreads 50` keeps 50 worker threads warm so traffic spikes don't pay thread-startup cost.
- `--maxthreads 100` lets the pool grow to 100 threads under sustained concurrency.
- `--connections 50` widens the accept backlog so bursts of new connections queue instead of being refused.

## A lean, low-memory profile

For a mostly-idle internal service, keep the pool small:

```bash
python manage.py cheroot -t 4 -w 16 -c 10
```

:::tip
Django views are typically I/O-bound (database, cache, external APIs), so thread count, not CPU count, is the lever that matters. Start from the defaults, measure real concurrency, then size `maxthreads` to your observed peak rather than guessing high.
:::

## Next steps

- [Production behind a proxy](/django-cheroot/examples/production/) — front Cheroot with nginx for TLS and static files.
- [Configuration](/django-cheroot/configuration/) — the full option reference.
