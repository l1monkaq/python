import sys
from datetime import datetime

class Logger:
    def __init__(self, out_stream=sys.stderr, time_formatter='%Y-%m-%d %H:%M:%S'):
        self.out_stream = out_stream
        self.time_formatter = time_formatter

    def log(self, message: str):
        current_time = datetime.now().strftime(self.time_formatter)
        formatted_message = f"В{current_time} {message}"
        print(formatted_message, file=self.out_stream)

out_stream = sys.stderr
time_formatter = '%Y-%m-%d %H:%M:%S'
logger = Logger(out_stream, time_formatter)

logger.log('Hello World!')

