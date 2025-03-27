# Quickstart

### Install dependencies
```bash
pip install -r requirements.txt
```

### Generate gRPC code
```bash
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. counter.proto
```

### Start the server
```bash
python3 server.py
```

### Run the client
```bash
python3 client.py
```