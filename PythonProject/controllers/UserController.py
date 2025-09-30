from sanic import Blueprint
from sanic.response import json
from common.routes import routes
from helpers.ConnectionHelper import ConnectionHelper

user_bp = Blueprint("user")

class UserController:
    @user_bp.get(f"/{routes['user']}")
    async def hello_world(request):
        connectionHelper = ConnectionHelper()
        connectionHelper.insert("UserInfo", {"name":"oscar"})
        return json({"message": "UserController greeting!"})

    @user_bp.post(f"/{routes['user']}")
    async def insert_info(request):
        data = request.json
        connectionHelper = ConnectionHelper()
        connectionHelper.insert("UserInfo", data)
        return json({
            "message": "UserInfo inserted!"
        })