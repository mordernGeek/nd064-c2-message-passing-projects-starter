import grpc
import udaperson_pb2
import udaperson_pb2_grpc
#from flask import request

print("sending random message to udapersons...")

channel = grpc.insecure_channel("localhost:5005", options=(('grpc.enable_http_proxy', 0),))
 #kindly confirm this is the right port
stub = udaperson_pb2_grpc.PersonServiceStub(channel)

person = udaperson_pb2.GetPerson(
  id = 320,
  firstname = 'Olai',
  lastname = 'finally gets',
  company = 'grpc',
)

#print(feed.Create(person)
response = stub.Create(person)
