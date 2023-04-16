from cheroot import wsgi
from django.core.wsgi import get_wsgi_application
from django.core.management.base import BaseCommand


def run_cheroot_server(
    host: str = '127.0.0.1',
    port: int = 8000,
    numthreads: int = 30,
    max_threads: int = 40,
    request_queue_size: int = 20,
):
    application = get_wsgi_application()
    addr = host, port
    server = wsgi.Server(
        addr, application,
        numthreads=numthreads,  # minimum number of threads to keep in thread pool
        max=max_threads,  # maximum number of threads.
        request_queue_size=request_queue_size
    )
    server.start()


class Command(BaseCommand):
    help = 'Run Django WSGI application using CherryPy Cheroot Server'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--port', type=int,
                            help='Port to run server on')
        parser.add_argument('-ip', '--host_ip', type=str, help='Host IP')
        parser.add_argument('-t', '--numthreads', type=int,
                            help='Min threads in Thread Pool for CherryPy Server')
        parser.add_argument('-w', '--maxthreads', type=int,
                            help='Max worker threads')
        parser.add_argument('-c', '--request_queue_size',
                            type=int, help='Max queued connections')

    def handle(self, *args, **options):
        port = options['port'] or 8000
        host = options['host_ip'] or '127.0.0.1'
        numthreads = options['numthreads'] or 20
        max_threads = options['maxthreads'] or 40
        request_queue_size = options['request_queue_size'] or 20
        run_cheroot_server(
            port=port,
            host=host,
            numthreads=numthreads,
            max_threads=max_threads,
            request_queue_size=request_queue_size
        )
