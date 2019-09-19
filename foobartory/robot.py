from collections import defaultdict
import os
import time
from random import randrange, uniform


TEST = os.environ.get('TEST', None)


class Robot:
    def __init__(self):
        self.warehouses = defaultdict(lambda: 0)
        self._nb_actions = 0

    def _get_busy_for(self, duration):
        self._nb_actions += 1
        if TEST is None:
            time.sleep(duration)

    def move(self):
        self._get_busy_for(5)

    def mine_foo(self):
        self._get_busy_for(1)
        self.warehouses['foo'] += 1

    def mine_bar(self):
        mining_duration = uniform(0.5, 2)
        self._get_busy_for(mining_duration)
        self.warehouses['bar'] += 1

    def assemble_foobar(self):
        self._get_busy_for(2)
        if randrange(100) < 60:
            self.warehouses['foo'] -= 1
            self.warehouses['bar'] -= 1
            self.warehouses['foobar'] += 1
        else:
            self.warehouses['bar'] -= 1
