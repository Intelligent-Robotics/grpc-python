from concurrent import futures
import grpc
import greet_pb2, greet_pb2_grpc

class GreeterServicer(greet_pb2_grpc.GreeterServicer):
  def SayHello(self, request, context):
    print(f"Received from {request.name}")
    return greet_pb2.HelloReply(message='Hello, %s!' % request.name)
  
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
  server.add_insecure_port('localhost:50051')
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
  serve()