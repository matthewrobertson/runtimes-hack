import json

class State:
    def __init__(self, conversation_token = "") -> None:
        if conversation_token != "":
            self.state = json.loads(conversation_token)
        else:
            self.state = {}
    
    def x(self) -> int:
        return self.state["x"]

    def y(self) -> int:
        return self.state["y"]

    def ans(self) -> int:
        return self.state["ans"]

    def correct(self, ans: int) -> bool:
        return self.ans() == ans