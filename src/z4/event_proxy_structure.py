from datetime import datetime


class LogLine:
    def __init__(self, timestamp: datetime, source: str, message: str):
        self.message = message
        self.source = source
        self.timestamp = timestamp

    def __repr__(self):
        return f'LogLine[{self.timestamp}, src: {self.source}, message={self.message}]'


class EventTarget:
    def publishEvent(self, line: LogLine):
        raise NotImplementedError()


class EventProcessor:
    def acceptEvent(self, line: LogLine):
        # whole logic on what to do with inbound `line`;
        # finally: go over all/selected event targets and call `publishEvent` on them
        raise NotImplementedError()

    def register_target(self, target: EventTarget):
        pass


class EventSource:
    def register_processor(self, processor: EventProcessor):
        raise NotImplementedError()

    def onEvent(self, line: LogLine):
        # go through all registered processors and call acceptEvent with `line`
        raise NotImplementedError()


