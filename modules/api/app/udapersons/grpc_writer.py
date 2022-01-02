import grpc
import udaperson_pb2
import udaperson_pb2_grpc
from flask import request

print("sending random message to udapersons...")

channel = grpc.insecure_channel("localhost:5005") #kindly confirm this is the right port
feed = udaperson_pb2_grpc.PersonServiceStub(channel)

person = udaperson_pb2.GetPerson(
  id = 320,
  firstname = 34,
  lastname = 100,
  company = 20,
)

response = feed.Create(person)
