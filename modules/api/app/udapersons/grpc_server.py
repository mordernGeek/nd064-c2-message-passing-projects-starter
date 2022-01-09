import time
from concurrent import futures
import grpc
import udaperson_pb2
import udaperson_pb2_grpc


class PersonService(udaperson_pb2_grpc.PersonServiceServicer):


    def Get(self, request, context):
        fetch_entry = udaperson_pb2.GetPerson(
		id = 20, 
		firstname = "upland",
		lastname = "engineering",
		company = "limited"
	)
		
        result = udaperson_pb2.AllPersons()
        result.all.extend([fetch_entry])
        return result 
   
   
    def Create(self, request, context):
        new_entry = {
            "id": int(request.id),
            "firstname": request.name,
            "lastname": request.surname,
            "company": request.companyname,
        }
        print(new_entry)
		
        return udaperson_pb2.GetPerson(**new_entry)
		
	
		
# Initialize gRPC server
    def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        udaperson_pb2_grpc.add_PersonServiceServicer_to_server(PersonService(), server)
        print("grpc server functional...")
        server.add_insecure_port("[::]:50051")
        server.start()

        try:
            while True:
                time.sleep(86400)
            
            
        except KeyboardInterrupt:
            server.stop(0)
        

