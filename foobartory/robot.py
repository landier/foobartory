from collections import defaultdict
import os
import time


TEST = os.environ.get('TEST', None)


class Robot:
    def __init__(self):
        self.warehouses = defaultdict(lambda: 0)

    def _sleep(self, duration):
        if TEST is None:
            time.sleep(duration)

    def move(self):
        pass

    def mine_foo(self):
        self._sleep(1)
        self.warehouses['foo'] += 1

    def mine_bar(self):
        self._sleep(1)
        self.warehouses['bar'] += 1

    def build_foobar(self):
        pass
