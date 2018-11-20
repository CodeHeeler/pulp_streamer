from aiohttp import web

from .handler import Handler


handler = Handler()

async def server(*args, **kwargs):
    app = web.Application()
    app.add_routes([web.get('/streamer/{path:.+}', handler.stream_content)])
    return app
