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
    print(request_json)


    response = {}
    response["session"] = request_json["session"]
    response["scene"] = {
        "name": request_json["scene"]["name"],
        "slots": {},
        "next": {
            "name": "actions.scene.END_CONVERSATION"
        }
    }

    response["prompt"] = {
        "override": False,
        "firstSimple": {
            "speech": "Hello World.",
            "text": ""
        }
    }

    print("RESPONSE = {}".format(response))

    return response

