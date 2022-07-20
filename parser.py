import state

class InputParser:

    def __init__(self, request) -> None:
        self.request = request
        if "conversationToken" in request["conversation"]["conversationToken"]:
            self.state = state.State(request["conversation"]["conversationToken"])
        else:
            self.state = state.State() 

    def correct(self):
        return self.state.correct(int(self.arg_value("text")))
    
    def x(self):
        return self.state.x()

    def y(self):
        return self.state.y()

    def arg_value(self, name) -> str:
        if "arguments" in self.request["inputs"][0]:
            args = self.request["inputs"][0]["arguments"]
            arg = args[index(args, lambda item: item["name"] == name)]
            if arg:
                return arg["textValue"]