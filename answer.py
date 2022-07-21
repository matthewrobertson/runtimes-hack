from question import Question

class Answer:

    def __init__(self, token, input) -> None:
        self.conversationToken = token
        self.input = input

    def get_json(self) -> object:
        try:
            if self.input.correct():
                q = Question(prefix = "That is correct!")
                return q.get_json()
            
            q = Question(self.input.x(), self.input.y(), "Sorry that is incorrect.")
            return q.get_json()
        except:
            q = Question(self.input.x(), self.input.y(), "Sorry I did not understand that.")
            return q.get_json()
