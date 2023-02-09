# import uuid
#
# from aiohttp_apispec import docs, request_schema, response_schema, querystring_schema
#
# from app.crm.models import User
# from app.crm.schemes import ListUsersResponseSchema, UserGetRequestSchema, UserGetResponseSchema, \
#     UserAddSchema, UserSchema
# from app.web.app import View
# from app.web.schemes import OkResponseSchema
# from app.web.utils import json_response, check_basic_auth
from aiohttp.web_response import json_response


class AddUserView(View):
    @docs(tags=["crm"], summary="Add new user", description="Add new user to database")
    @request_schema(UserAddSchema)
    @response_schema(OkResponseSchema, 200)
    async def post(self):
        data = self.request["data"]
        user = User(email=data["email"], id_=uuid.uuid4())
        await self.request.app.crm_accessor.add_user(user)
        return json_response()

