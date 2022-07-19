class Question:

    def __init__(self, request) -> None:
        self.request = request

    def set_next_scene(self, name) -> None:
        self.next_scene = name

    def set_prompt(self, text, speech) -> None:
        self.text_prompt = text
        self.speech_prompt = speech

    def get_json(self) -> object:
        return {
            "session": self.request["session"],
            "scene": {
                "name": self.request["scene"]["name"],
                "slots": {},
                "next": {
                    "name": self.next_scene
                }
            },
            "prompt": {
                "override": False,
                "firstSimple": {
                    "speech": self.speech_prompt,
                    "text": self.text_prompt
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

    question = Question(request_json)
    question.set_next_scene("actions.scene.END_CONVERSATION")
    prompt = "What is 6 + 6"
    question.set_prompt(prompt, prompt)

    return question.get_json()
