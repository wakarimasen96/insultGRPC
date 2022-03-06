import google
import grpc



import insultme_pb2
import insultme_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = insultme_pb2_grpc.insultmeStub(channel)

# create a valid request message
insultme = insultme_pb2.insultRequest
# make the call
response = stub.insultme

# et voilà
print(response)







