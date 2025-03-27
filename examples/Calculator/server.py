from concurrent import futures
import grpc
import calculate_pb2, calculate_pb2_grpc

class CalculatorServicer(calculate_pb2_grpc.CalculatorServicer):
  def CalcSum(self, request, context):
    print(f"Received values {request.a} and {request.b}")
    final = request.a + request.b
    return calculate_pb2.CalcOutput(sum=final)
  
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  calculate_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
  server.add_insecure_port('localhost:50051')
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
  serve()