import grpc

from concurrent import futures
import time

# import the generated classes
import insultme_pb2
import insultme_pb2_grpc

import insultme


class insultmeServicer(insultme_pb2_grpc.insultmeServicer):

    def insultme(self, context):
        response = insultme_pb2.insultReply
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

insultme_pb2_grpc.add_insultmeServicer_to_server(insultmeServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
