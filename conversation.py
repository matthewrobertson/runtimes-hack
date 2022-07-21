from input_parser import InputParser
from goodbye import Goodbye
from question import Question
from answer import Answer

class Conversation:

    def __init__(self, request) -> None:
        self.request = request
        self.input = InputParser(request)

    def next(self):
        if self.input.intent_type() == "actions.intent.CANCEL":
            return Goodbye()

        if token := self.input.conversation_token():
            return Answer(token, self.input)

        return Question()
