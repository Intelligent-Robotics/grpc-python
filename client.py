import grpc
import counter_pb2
import counter_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = counter_pb2_grpc.CounterStub(channel)

starting_value = 0
initial_request = counter_pb2.Count(value=starting_value)
response = stub.AddOne(initial_request)
print(f"Request: {starting_value} --> Response: {response.value}")

number_of_calls = 999
for i in range(number_of_calls):
    request = counter_pb2.Count(value=response.value)
    response = stub.AddOne(request)
    print(f"Request: {request.value} --> Response: {response.value}")