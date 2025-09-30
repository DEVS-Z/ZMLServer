from sanic import Blueprint
from sanic.response import json
from common.routes import routes
from helpers.ConnectionHelper import ConnectionHelper

user_bp = Blueprint("user")

class UserController:
    @user_bp.get(f"/{routes['user']}/test")
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
    @user_bp.get(f"/{routes['user']}")
    async def get_info(request):
        connectionHelper = ConnectionHelper()
        connectionHelper.init_connection()
        cursor = connectionHelper._database['UserInfo'].aggregate([
            {
                "$project": {
                    "_id": 0,
                    "name": 1,
                    "bpm": 1,
                    "date": {
                        "$dateToString": {
                            "format": "%Y-%m-%d",
                            "date": { "$toDate": "$timestamp" }  # 👈 convierte string → Date
                        }
                    }
                }
            },
            {
                "$group": {
                    "_id": {
                        "date": "$date",
                        "name": "$name"
                    },
                    "records": {
                        "$push": {
                            "bpm": "$bpm",
                            "timestamp": "$date"
                        }
                    }
                }
            },
            {
                "$group": {
                    "_id": "$_id.date",
                    "users": {
                        "$push": {
                            "name": "$_id.name",
                            "records": "$records"
                        }
                    }
                }
            },
            {
                "$sort": {"_id": 1}
            }
        ])
        data = list(cursor)

        return json(data)