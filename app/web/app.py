from typing import Optional

from aiohttp.web import Application as AiohttpApplication, run_app as aiohttp_run_app, \
    View as AiohttpView, Request as AiohttpRequest

from app.store import setup_accessors
from app.store.crm.accessor import CrmAccessor

from app.web.routes import setup_routes


# class Application(AiohttpApplication):
#     database: dict = {}
#     crm_accessor: Optional[CrmAccessor] = None
class Application(AiohttpApplication):
    # config: Optional[Config] = None
    database: dict = {}
    crm_accessor: Optional[CrmAccessor] = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    setup_routes(app)
    print('setup_routes')
    setup_accessors(app)
    print('setup_accessors')
    # print(app.crm_accessor.)
    aiohttp_run_app(app)
    print('aiohttp_run_app')
