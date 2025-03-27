import grpc
import greet_pb2, greet_pb2_grpc


def run():
  with grpc.insecure_channel('localhost:50051') as channel:
    stub = greet_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(greet_pb2.HelloRequest(name='you'))
    print(response.message)

if __name__ == "__main__":
  run()