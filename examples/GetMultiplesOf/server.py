
from concurrent import futures

import grpc
import get_multiples_of_pb2_grpc as pb_grpc


class MultiplesOfService(pb_grpc.MultiplesOfServicer):

    def CheckAll(self, requests, context):
        for number in requests:
            if number.value % 5 == 0:
                yield number


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_grpc.add_MultiplesOfServicer_to_server(MultiplesOfService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()