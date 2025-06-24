import time
from services.logs import Logging


class ContextManager:
    def __init__(self, name, connect_func, disconnect_func):
        self._logging = Logging()
        self.name = name
        self.connect_func = connect_func
        self.disconnect_func = disconnect_func
        self.resource = None
        self.start_time = None

    @property
    def logging(self):
        return self._logging

    def __enter__(self):
        self.logging.info(f"[{self.name}] Connecting to resource...")
        self.start_time = time.perf_counter()
        self.resource = self.connect_func()
        self.logging.info(f"[{self.name}] Connected successfully.")
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        duration = time.perf_counter() - self.start_time

        if exc_type:
            self.logging.error(f"[{self.name}] Error occurred: {exc_value}")

        self.logging.info(f"[{self.name}] Disconnecting resource after {duration:.2f}s")
        self.disconnect_func(self.resource)
        self.logging.info(f"[{self.name}] Disconnected.")
