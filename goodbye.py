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