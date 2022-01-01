import grpc
import udaperson_pb2
import udaperson_pb2_grpc
from kafka import KafkaConsumer
from flask import request


#Udaconnect file that writes to Udalocation and UdaPersons
#REST, grpc and kafka are implemented separately here


TOPIC_NAME = 'location'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)


print("sending random message to udapersons...")

channel = grpc.insecure_channel("localhost:5007") #kindly confirm this is the right port
feed = udaperson_pb2_grpc.PersonServiceStub(channel)

person = udaperson_pb2.GetPerson(
  id = 320;
  firstname = Olai;
  lastname = Wdsvl;
  company = Uel;
}

response = feed.Create(person)



ask = request.get('http://localhost:5000/kafka')

if ask.status_code == 200:
    print(ask.json())
	
	
askb = request.get('http://localhost:5000/grpc')

if askb.status_code == 200:
    print(askb.json())
	
	
