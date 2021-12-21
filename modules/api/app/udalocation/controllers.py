from datetime import datetime

from app.udalocation.models import Location
from app.udalocation.schemas import (
    LocationSchema,
)
from app.udalocation.services import LocationService
from flask import request, g, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

from Kafka import KafkaProducer


DATE_FORMAT = "%Y-%m-%d"

api = Namespace("udalocation", description="Connections via geolocation.")  # noqa


# TODO: This needs better exception handling
# integrating with apache kafka 

@app.before_request

def before_request():
    #Creating my kafka producer

    TOPIC_NAME = "locations"
    KAFKA_SERVER = 'localhost:9092' #need to assert this, shouldn't my server be where i write the logic?
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    g.kafka_producer = producer 




@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        request.get_json()
        location: Location = LocationService.create(request.get_json())
        return Response(status=202)
        #return location

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location



    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)

        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        return results
