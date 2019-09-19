from collections import defaultdict
import os
import time
from random import uniform


TEST = os.environ.get('TEST', None)


class Robot:
    def __init__(self):
        self.warehouses = defaultdict(lambda: 0)

    def _sleep(self, duration):
        if TEST is None:
            time.sleep(duration)

    def move(self):
        self._sleep(5)

    def mine_foo(self):
        self._sleep(1)
        self.warehouses['foo'] += 1

    def mine_bar(self):
        mining_duration = uniform(0.5, 2)
        self._sleep(mining_duration)
        self.warehouses['bar'] += 1

    def build_foobar(self):
        pass
