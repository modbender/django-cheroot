from cheroot import wsgi
from django.core.management.base import BaseCommand
from django.core.wsgi import get_wsgi_application

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
DEFAULT_MIN_THREADS = 30
DEFAULT_MAX_THREADS = 40
DEFAULT_CONNECTIONS = 20


def build_cheroot_server(
    host=DEFAULT_HOST,
    port=DEFAULT_PORT,
    min_threads=DEFAULT_MIN_THREADS,
    max_threads=DEFAULT_MAX_THREADS,
    connections=DEFAULT_CONNECTIONS,
):
    """Build a Cheroot WSGI server bound to the Django WSGI application.

    Returns the unstarted ``cheroot.wsgi.Server`` so callers (and tests) can
    inspect or manage it; call ``.start()`` to begin serving.
    """
    application = get_wsgi_application()
    return wsgi.Server(
        (host, port),
        application,
        numthreads=min_threads,  # minimum threads kept in the pool
        max=max_threads,  # maximum worker threads (-1 for unlimited)
        request_queue_size=connections,  # max queued connections
    )


def run_cheroot_server(**kwargs):
    server = build_cheroot_server(**kwargs)
    server.start()


class Command(BaseCommand):
    help = "Run the Django WSGI application using the Cheroot HTTP server"

    def add_arguments(self, parser):
        parser.add_argument(
            "-ip", "--hostip", type=str, default=DEFAULT_HOST, help="Host IP to bind"
        )
        parser.add_argument(
            "-p", "--port", type=int, default=DEFAULT_PORT, help="Server port"
        )
        parser.add_argument(
            "-w",
            "--maxthreads",
            type=int,
            default=DEFAULT_MAX_THREADS,
            help="Maximum worker threads",
        )
        parser.add_argument(
            "-t",
            "--minthreads",
            type=int,
            default=DEFAULT_MIN_THREADS,
            help="Minimum threads kept in the thread pool",
        )
        parser.add_argument(
            "-c",
            "--connections",
            type=int,
            default=DEFAULT_CONNECTIONS,
            help="Maximum queued connections",
        )

    def handle(self, *args, **options):
        host = options["hostip"]
        port = options["port"]
        self.stdout.write(
            self.style.SUCCESS(f"Starting Cheroot server at http://{host}:{port}")
        )
        try:
            run_cheroot_server(
                host=host,
                port=port,
                min_threads=options["minthreads"],
                max_threads=options["maxthreads"],
                connections=options["connections"],
            )
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("\nShutting down Cheroot server."))
