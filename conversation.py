from parser import InputParser
class Conversation:

    def __init__(self, request) -> None:
        self.request = request
        self.input = InputParser(request)

    def next(self):
        if self.input.intent_type() == "actions.intent.CANCEL":
            return Goodbye()

        if token := self.input.conversation_token():
            print(self.input.conversation_token)
            print(self.request["inputs"])
            return Answer(token, self.input)

        return Question()