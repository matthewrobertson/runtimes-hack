import json
from re import X


class Question:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_json(self) -> object:
        return {
            "expectUserResponse": True,
            "expectedInputs": [
                {
                    "inputPrompt": {
                        "richInitialPrompt": {
                            "items": [
                                {
                                    "simpleResponse": {
                                        "textToSpeech": f'What is {self.x} + {self.y}?',
                                        "displayText": f'What is {self.x} + {self.y}?',
                                    }
                                }
                            ]
                        }
                    },
                    "possibleIntents": [
                        {
                            "intent": "actions.intent.TEXT"
                        }
                    ]
                }
            ],
            "conversationToken": json.dumps({"x": self.x, "y": self.y, "ans": self.x+self.y})
        }


class Answer:

    def __init__(self, token, input) -> None:
        self.conversationToken = token
        self.input = input

    def get_json(self) -> object:
        return {
            "expectUserResponse": False,
            "finalResponse": {
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": "Okay, talk to you next time!"
                            }
                        }
                    ]
                }
            }
        }


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

    if "conversationToken" in request_json["conversation"]:
        print(request_json["conversation"]["conversationToken"])
        print(request_json["inputs"])
        token = request_json["conversation"]["conversationToken"]
        ans = Answer(token, request_json["inputs"])
        return ans.get_json()

    question = Question(5, 4)
    return question.get_json()
