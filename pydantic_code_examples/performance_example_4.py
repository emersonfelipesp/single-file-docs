
    class CompletedStr(str):
        def __init__(self, s: str):
            self.s = s
            self.done = False
    