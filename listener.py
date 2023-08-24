import json
import time
import webhook_listener
from jsonschema import validate

schema = {
    "type" : "object",
    "properties" : {
        "action" : {"type" : "string"},
        "entity_type" : {"type" : "string"},
        "time" : {"type" : "string"},
        "id" : {"type" : "string"},
        "payload" : {
            "type" : "object",
            "properties": {
                "id" : {"type" : "string"},
                "name" : {"type" : "string"},
            }
        },
    },
}


another_schema = {
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
    },
}


def process_post_request(request, *args, **kwargs):
    print(
        "Received request:\n"
        + "Method: {}\n".format(request.method)
        + "Headers: {}\n".format(request.headers)
        + "Args (url path): {}\n".format(args)
        + "Keyword Args (url parameters): {}\n".format(kwargs)
        + "Body: {}".format(
            request.body.read(int(request.headers["Content-Length"]))
            if int(request.headers.get("Content-Length", 0)) > 0
            else ""
        )
    )
    data = json.loads(next(iter(kwargs)))
    validate(instance=data, schema=schema)

    # Process the request!
    # ...

    return


webhooks = webhook_listener.Listener(handlers={"POST": process_post_request})
webhooks.start()

while True:
    print("Still alive...")
    time.sleep(300)
