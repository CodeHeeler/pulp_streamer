from aiohttp import web

from .handler import Handler


handler = Handler()

async def server(*args, **kwargs):
    app = web.Application()
    app.add_routes([web.get('/', handler.ok)])
    return app
