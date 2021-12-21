import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.udapersons.models import Person
from app.udapersons.schemas import PersonSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
from concurrent import futures
import grpc
import udaperson_pb2
import udaperson_pb2_grpc


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udapersons-api")


class PersonService(udaperson_pb2_grpc.PersonServiceServicer):
    @staticmethod
    def create(person: Dict) -> Person:
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        db.session.add(new_person)
        db.session.commit()

        return udaperson_pb2.GetPerson(new_person)

    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return udaperson_pb2.GetPerson(person)

    @staticmethod
    def retrieve_all() -> List[Person]:
        #return db.session.query(Person).all()
        return udaperson_pb2.AllPersons(Person)

    def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        udaperson_pb2_grpc.add_PersonServiceServicer_to_server(PersonService(), server)

        print("looks like i got to this point!")
        server.add_insecure_port("[::]:50051")
        server.start()
        server.wait_for_termination()

##Initializing the server


#class PersonServiceServicer(udaperson_pb2_grpc.services):
