import grpc
from concurrent import futures
import time

from config.connections import analyzer_pb2_grpc, analyzer_pb2
from helpers.ConnectionHelper import ConnectionHelper

class UserService(analyzer_pb2_grpc.UserServiceServicer):
    def InsertUserData(self, request, context):
        print(f"Datos recibidos desde Go:")
        print(f"name={request.name}, bpm={request.bpm}, timestamp={request.timestamp}")

        try:
            connectionHelper = ConnectionHelper()
            connectionHelper.insert("UserInfo", {
                "name": request.name,
                "bpm": request.bpm,
                "timestamp": request.timestamp
            })
            return analyzer_pb2.InsertResponse(ok=True, message="User data inserted successfully")
        except Exception as e:
            print(f"Error inserting: {e}")
            return analyzer_pb2.InsertResponse(ok=False, message=f"Insert failed: {e}")

def start_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    analyzer_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50052')
    print("🚀 gRPC Server corriendo en puerto 50052")
    server.start()

    # Mantiene el hilo activo
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)