import state

class InputParser:

    def __init__(self, request) -> None:
        self.request = request
        if "conversationToken" in request["conversation"]:
            self.state = state.State(request["conversation"]["conversationToken"])
        else:
            self.state = state.State() 
    
    def conversation_token(self):
        if "conversationToken" in self.request["conversation"]:
            return self.request["conversation"]["conversationToken"]

    def intent_type(self):
        return self.request["inputs"][0]["intent"]

    def correct(self):
        return self.state.correct(int(self.arg_value("text")))
    
    def x(self):
        return self.state.x()

    def y(self):
        return self.state.y()

    def arg_value(self, name) -> str:
        if "arguments" in self.request["inputs"][0]:
            args = self.request["inputs"][0]["arguments"]
            arg = next(x for x in args if x["name"] == name)
            if arg:
                return arg["textValue"]