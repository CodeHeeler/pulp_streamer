=====
Usage
=====

To run the content app with Gunicorn use its pulpcore.content:server entry point like::

    gunicorn pulpcore.content:server --bind localhost:8080 --worker-class aiohttp.GunicornWebWorker -w 2

