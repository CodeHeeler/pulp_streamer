=====
Usage
=====

To run the streamer with Gunicorn use its pulpcore.streamer:server entry point like::

    gunicorn pulpcore.streamer:server --bind localhost:8080 --worker-class aiohttp.GunicornWebWorker -w 2

