import sys
from datetime import datetime
from abc import ABC, abstractmethod

class Formatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass

class SimpleFormatter(Formatter):
    def format(self, message: str) -> str:
        return message

class TimestampFormatter(Formatter):
    def __init__(self, time_format='%Y-%m-%d %H:%M:%S'):
        self.time_format = time_format

    def format(self, message: str) -> str:
        timestamp = datetime.now().strftime(self.time_format)
        return f"[{timestamp}] {message}"

class Handler(ABC):
    @abstractmethod
    def handle(self, message: str):
        pass

class StreamHandler(Handler):
    def __init__(self, stream=sys.stderr):
        self.stream = stream

    def handle(self, message: str):
        self.stream.write(message + '\n')

class FileHandler(Handler):
    def __init__(self, filename):
        self.file = open(filename, 'a')

    def handle(self, message: str):
        self.file.write(message + '\n')

    def __del__(self):
        self.file.close()

class Logger:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter
        self.handlers = []

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)

    def log(self, message: str):
        formatted = self.formatter.format(message)
        for handler in self.handlers:
            handler.handle(formatted)

formatter = TimestampFormatter('%Y-%m-%d %H:%M:%S')
logger = Logger(formatter)
logger.add_handler(StreamHandler(sys.stdout))
logger.log("Test log message")
