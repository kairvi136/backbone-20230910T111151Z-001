import json

def serialize_data(data):
    return json.dumps(data).encode()

def deserialize_data(data):
    return json.loads(data.decode())
