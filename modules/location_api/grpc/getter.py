import grpc
import location_pb2
import location_pb2_grpc
from app.udaconnect.services import location
"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    person_id= location.person_id,
    creation_time= location.creation_time,
    latitude= location.latitude,
    longitude= location.longitude
)

response = stub.Create(location)