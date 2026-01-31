class FakeLogger:
    def __init__(self):
        self.messages = []

    def debug(self, msg, *args):
        self.messages.append(("DEBUG", msg % args if args else msg))

    def info(self, msg, *args):
        self.messages.append(("INFO", msg % args if args else msg))

    def error(self, msg, *args):
        self.messages.append(("ERROR", msg % args if args else msg))
