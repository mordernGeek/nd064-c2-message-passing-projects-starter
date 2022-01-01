Skip to content
udacity
/
nd064-c2-message-passing-exercises
Public
Code
Issues
Pull requests
4
Actions
Projects
More
nd064-c2-message-passing-exercises/lesson-3-implementing-message-passing/grpc-demo/main.py /
@leejustin
leejustin Add Lesson 3 content
 History
 1 contributor
 36 lines (27 sloc)  834 Bytes
import time
from concurrent import futures

import grpc
import item_pb2
import item_pb2_grpc


class ItemServicer(item_pb2_grpc.ItemServiceServicer):
    def Create(self, request, context):

        request_value = {
            "name": request.name,
            "brand_name": request.brand_name,
            "id": int(request.id),
            "weight": request.weight,
        }
        print(request_value)

        return item_pb2.ItemMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
item_pb2_grpc.add_ItemServiceServicer_to_server(ItemServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

Loading complete