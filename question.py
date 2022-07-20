import random

class Question:

    def __init__(self, x = random.randrange(10), y = random.randrange(10), prefix = "") -> None:
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
