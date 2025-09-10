from sanic import Blueprint
from sanic.response import json
from common.routes import routes

test_bp = Blueprint("access")

@test_bp.get(f"/{routes['test']}")
async def hello_world(request):
    return json({"message": "Hello, python server!"})
