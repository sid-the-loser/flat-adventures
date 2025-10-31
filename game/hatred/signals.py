class Publisher:
    def __init__(self) -> None:
        self.subscribers: list[Subscriber] = []

    def notify(self):
        for sub in self.subscribers:
            sub.trigger()

class Subscriber:
    def __init__(self) -> None:
        pass

    def trigger(self) -> None:
        pass