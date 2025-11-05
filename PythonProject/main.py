from sanic import Sanic
from controllers.TestController import test_bp
from controllers.UserController import user_bp
import threading
from sanic_cors import CORS
from services.UserService import start_grpc_server

app = Sanic("MyAcessApp")
CORS(app)
app.blueprint(test_bp)
app.blueprint(user_bp)

if __name__ == "__main__":
    grpc_thread = threading.Thread(target=start_grpc_server, daemon=True)
    grpc_thread.start()

    app.run(host="0.0.0.0", port=8000, single_process=True)
