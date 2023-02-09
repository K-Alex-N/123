import uuid
from typing import Any

# from aiohttp.web_response import json_response
from aiohttp.web_response import Response

from app.crm.models import User
from app.web.app import View
from aiohttp.web import json_response as aiohttp_json_response
def json_response(data: Any = None, status: str = 'ok') -> Response:
    if data is None:
        data = {}
    return aiohttp_json_response(
        data={
            "status": status,
            "data": data,
        })

class AddUserView(View):
    async def post(self):
        data = await self.request.json()
        user = User(email=data["email"], id_=uuid.uuid4())
        await self.request.app.crm_accessor.add_user(user)
        return json_response()
