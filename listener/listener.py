import json
import time
import webhook_listener
from jsonschema import validate

with open('/app/schema.json') as schema_file:
  schema = json.load(schema_file)

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
