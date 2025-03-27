import grpc
from concurrent import futures
import counter_pb2
import counter_pb2_grpc

class CounterServer(counter_pb2_grpc.CounterServicer):
    def AddOne(self, request, context):
        print(f"Processing request {request.value}")
        new_value = request.value + 1
        response = counter_pb2.Count(value=new_value)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
counter_pb2_grpc.add_CounterServicer_to_server(CounterServer(), server)
server.add_insecure_port('[::]:50051')

print("Starting gRPC server...")
server.start()
server.wait_for_termination()