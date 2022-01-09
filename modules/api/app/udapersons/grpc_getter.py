import grpc
import udaperson_pb2
import udaperson_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:50051")
stub = udaperson_pb2_grpc.PersonServiceStub(channel)

response = stub.Get(udaperson_pb2.Empty())
print(response)
