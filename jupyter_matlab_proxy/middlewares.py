from aiohttp import web
from getpass import getuser

def check_header_factory(header_name,header_value):
    @middleware
    async def check_header(request, handler):
        resp = await handler(request)
        if request.headers.get(header_name) != header_value:
            raise web.HTTPForbidden()
        return resp
    return check_header

@web.middleware
async def forwarded_user(request, handler):
    resp = await handler(request)
    if request.headers.get('X-Forwarded-User') != getuser():
        raise web.HTTPForbidden()
    return resp  
