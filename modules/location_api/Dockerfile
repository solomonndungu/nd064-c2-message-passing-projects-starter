FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
copy app/udaconnect/location.proto app/udaconnect/location.proto
RUN python3 -m grpc_tools.protoc -I./app/udaconnect --python_out=./app/udaconnect --grpc_python_out=./app/udaconnect app/udaconnect/location.proto
EXPOSE 5006

COPY . .
ENTRYPOINT ["python3", "app/grpc_server.py"]