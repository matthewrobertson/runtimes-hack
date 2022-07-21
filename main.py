from conversation import Conversation
import json

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    print(json.dumps(request_json, indent=4, sort_keys=True))
    convo = Conversation(request_json)
    return convo.next().get_json()
