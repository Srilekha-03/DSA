class BrowserHistory:

    def __init__(self, homepage: str):
        self.past = []
        self.future = []
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.past.append(self.curr)
        self.curr = url
        self.future = []

    def back(self, steps: int) -> str:
        while steps > 0 and self.past:
            self.future.append(self.curr)
            self.curr = self.past.pop()
            steps -= 1
        return self.curr

    def forward(self, steps: int) -> str:
        while steps > 0 and self.future:
            self.past.append(self.curr)
            self.curr = self.future.pop()
            steps -= 1
        return self.curr
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)