import grpc
import calculate_pb2, calculate_pb2_grpc


def run():
  with grpc.insecure_channel('localhost:50051') as channel:
    stub = calculate_pb2_grpc.CalculatorStub(channel)
    response = stub.CalcSum(calculate_pb2.ValuesInput(a=25, b=37))
    print(response.sum)

if __name__ == "__main__":
  run()