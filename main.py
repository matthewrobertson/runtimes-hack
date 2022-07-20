import json


class InputParser:

    def __init__(self, input) -> None:
        self.input = input

    def intent_type(self):
        return self.input[0]["intent"]
    
    def correct(self):
        return True
    
    def x(self):
        return 5

    def y(self):
        return 4


class Question:

    def __init__(self, x, y, prefix = "") -> None:
        self.x = x
        self.y = y
        self.prefix = prefix

    def get_json(self) -> object:
        text = f'What is {self.x} + {self.y}?'
        if self.prefix != "":
            text = self.prefix + " " + text
        return {
            "expectUserResponse": True,
            "expectedInputs": [
                {
                    "inputPrompt": {
                        "richInitialPrompt": {
                            "items": [
                                {
                                    "simpleResponse": {
                                        "textToSpeech": text,
                                        "displayText": text,
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
        if self.input.correct():
            q = Question(3, 3, "That is correct!")
            return q.get_json()
        
        q = Question(self.input.x(), self.input.y(), "Sorry that is incorrect.")
        return q.get_json()


class Goodbye:

    def __init__(self) -> None:
        pass

    def get_json(self) -> object:
        return {
            "expectUserResponse": False,
            "finalResponse": {
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": "Okay, thanks for playing!"
                            }
                        }
                    ]
                }
            }
        }


class Conversation:

    def __init__(self, request) -> None:
        self.request = request
        self.input = InputParser(request["inputs"])

    def next(self):
        if self.input.intent_type() == "actions.intent.CANCEL":
            return Goodbye()

        if "conversationToken" in self.request["conversation"]:
            print(self.request["conversation"]["conversationToken"])
            print(self.request["inputs"])
            state = json.loads(
                self.request["conversation"]["conversationToken"])
            token = self.request["conversation"]["conversationToken"]
            return Answer(token, self.input)

        return Question(5, 4)


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
