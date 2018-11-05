import logging

from aiohttp import web


log = logging.getLogger(__name__)


class Handler:

    async def ok(self, request):
        response = web.StreamResponse()
        await response.prepare(request)
        await response.write(b'0' * 1024)
        await response.write_eof()
        return response
