import django
from cheroot import wsgi
from django.conf import settings
from django.test.utils import get_runner


def _configure():
    if settings.configured:
        return
    settings.configure(
        DEBUG=True,
        SECRET_KEY="test-secret-key",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["*"],
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "django_cheroot",
        ],
        DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    )
    django.setup()


urlpatterns = []


def test_command_is_registered():
    _configure()
    from django.core.management import get_commands

    assert get_commands().get("cheroot") == "django_cheroot"


def test_build_server_defaults():
    _configure()
    from django_cheroot.management.commands.cheroot import (
        DEFAULT_CONNECTIONS,
        DEFAULT_MAX_THREADS,
        DEFAULT_MIN_THREADS,
        build_cheroot_server,
    )

    server = build_cheroot_server()
    try:
        assert isinstance(server, wsgi.Server)
        assert server.bind_addr == ("127.0.0.1", 8000)
        assert server.requests.min == DEFAULT_MIN_THREADS
        assert server.requests.max == DEFAULT_MAX_THREADS
        assert server.request_queue_size == DEFAULT_CONNECTIONS
    finally:
        server.stop()


def test_build_server_custom_args():
    _configure()
    from django_cheroot.management.commands.cheroot import build_cheroot_server

    server = build_cheroot_server(
        host="0.0.0.0", port=9001, min_threads=5, max_threads=15, connections=8
    )
    try:
        assert server.bind_addr == ("0.0.0.0", 9001)
        assert server.requests.min == 5
        assert server.requests.max == 15
        assert server.request_queue_size == 8
    finally:
        server.stop()
