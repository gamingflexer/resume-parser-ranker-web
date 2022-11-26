import uuid
import json

def uuid4_generator():
    return str(uuid.uuid4())

def to_json(data):
    return json.loads(json.dumps(data))