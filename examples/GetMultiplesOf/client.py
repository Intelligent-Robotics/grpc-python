import grpc
import get_multiples_of_pb2_grpc as pb_grpc
import get_multiples_of_pb2 as pb


def generate_numbers():
    number = 0
    while number < 100:
        print(f"[CLIENT] -> {number}")
        request = pb.Number(value=number)
        next_value = yield request
        if next_value is not None:
            number = next_value
        number += 1


def send_message(stub):
    requests = generate_numbers()
    responses = stub.CheckAll(requests)
    for response in responses:
        requests.send(response.value)
        print(f"[SERVER] <- {response.value} !!")


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb_grpc.MultiplesOfStub(channel)
        send_message(stub)


if __name__ == '__main__':
    run()