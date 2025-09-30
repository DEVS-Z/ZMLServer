from sanic import Sanic
from controllers.TestController import test_bp
from controllers.UserController import user_bp
from sanic_cors import CORS

app = Sanic("MyAcessApp")
CORS(app)
app.blueprint(test_bp)
app.blueprint(user_bp)# registrar blueprint

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, single_process=True)
