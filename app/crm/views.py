import uuid
# from typing import Any
from aiohttp.web_exceptions import HTTPNotFound
# from aiohttp.web_response import json_response
# from aiohttp.web_response import Response
from aiohttp_apispec import docs, request_schema, response_schema, querystring_schema

from app.crm.models import User
from app.crm.schemes import UserSchema, ListUsersResponseSchema, UserGetRequestSchema, UserGetResponseSchema, \
    UserAddSchema
from app.web.app import View


from app.web.schemes import OkResponseSchema
from app.web.utils import json_response


# from aiohttp.web import json_response as aiohttp_json_response
# def json_response(data: Any = None, status: str = 'ok') -> Response:
#     if data is None:
#         data = {}
#     return aiohttp_json_response(
#         data={
#             "status": status,
#             "data": data,
#         })

class AddUserView(View):
    @docs(tags=['crm'], summary='add new user', description='Test method description')
    @request_schema(UserAddSchema)
    @response_schema(OkResponseSchema, 200)
    async def post(self):
        data = self.request['data']
        user = User(email=data["email"], id_=uuid.uuid4())
        await self.request.app.crm_accessor.add_user(user)
        return json_response()


class ListUsersView(View):
    @docs(tags=['crm'], summary='list users', description='Test measdadthod description')
    @response_schema(ListUsersResponseSchema, 200)
    async def get(self):
        users = await self.request.app.crm_accessor.list_users()
        raw_users = [{'email': user.email, "id": str(user.id_)} for user in users]
        # raw_users = [UserSchema().dump(user) for user in users]
        return json_response(data={'users': raw_users})

class GetUserView(View):
    @docs(tags=['crm'], summary='get user', description='Test method description')
    # @request_schema(UserGetRequestSchema)
    @querystring_schema(UserGetRequestSchema)
    @response_schema(UserGetResponseSchema, 200)
    async def get(self):
        user_id = self.request.query['id']
        user = await self.request.app.crm_accessor.get_user(uuid.UUID(user_id))
        if user:
            return json_response(data={'user': {'email': user.email, 'id': str(user.id_)}})
        else:
            raise HTTPNotFound
