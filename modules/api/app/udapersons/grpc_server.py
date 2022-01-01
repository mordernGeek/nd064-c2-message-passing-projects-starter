import time
from concurrent import futures

import grpc
import udaperson_pb2
import udaperson_pb2_grpc


class PersonService(udaperson_pb2_grpc.PersonServiceServicer):
    def Create(self, request, context):

        new_entry = {
            "id": int(request.id),
			"firstname": request.name
			"lastname": request.surname
			"company": request.companyname,
        }
        print(new_entry)

        return udaperson_pb2.GetPerson(**new_entry)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
item_pb2_grpc.add_ItemServiceServicer_to_server(ItemServicer(), server)


print("grpc server functional...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

