from event_proxy_structure import *


class InputSource(EventSource):
    def __init__(self):
        self.processors: list[EventProcessor] = []

    def register_processor(self, processor: EventProcessor):
        self.processors.append(processor)

    def onEvent(self, line: LogLine):
        for p in self.processors:
            p.acceptEvent(line)

    def run(self):
        while True:
            msg = input('msg> ')
            line = LogLine(datetime.now(), 'console_input', msg)
            self.onEvent(line)


class DefaultEventProcessor(EventProcessor):

    def __init__(self):
        self.targets: list[EventTarget] = []

    def acceptEvent(self, line: LogLine):
        for t in self.targets:
            t.publishEvent(line)

    def register_target(self, target: EventTarget):
        self.targets.append(target)


class ConsoleTarget(EventTarget):
    def publishEvent(self, line: LogLine):
        print(line)

class FileTarget(EventTarget):

    def __init__(self, file_name: str):
        self.file_name = file_name

    def publishEvent(self, line: LogLine):
        with open(self.file_name, 'a') as f:
            f.write(line.__repr__() + '\n')



if __name__ == '__main__':
    processor = DefaultEventProcessor()
    source = InputSource()
    source.register_processor(processor)

    target = ConsoleTarget()
    processor.register_target(target)
    file_target = FileTarget('our_log.log')
    processor.register_target(file_target)

    # teraz uruchamiamy system
    source.run()
