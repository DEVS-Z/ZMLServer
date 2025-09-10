from sanic import Blueprint
from sanic.response import json
from common.routes import routes

user_bp = Blueprint("user")

class UserController:
    @user_bp.get(f"/{routes['user']}")
    async def hello_world(request):
        return json({"message": "UserController greeting!"})