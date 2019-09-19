from collections import defaultdict
import os
import time
from random import randrange, uniform
from uuid import uuid4


TEST = os.environ.get('TEST', None)


class Robot:
    def __init__(self):
        self.warehouses = defaultdict(list)
        self._last_action = None
        self._nb_actions = 0

    def _get_busy_for(self, duration):
        self._nb_actions += 1
        if TEST is None:
            time.sleep(duration)

    def move(self):
        self._get_busy_for(5)

    def mine_foo(self):
        self._get_busy_for(1)
        self.warehouses['foo'].append(uuid4())

    def mine_bar(self):
        mining_duration = uniform(0.5, 2)
        self._get_busy_for(mining_duration)
        self.warehouses['bar'].append(uuid4())

    def assemble_foobar(self, success_threshold=60):
        self._get_busy_for(2)
        foo = self.warehouses['foo'].pop()
        if randrange(100) < success_threshold:
            bar = self.warehouses['bar'].pop()
            self.warehouses['foobar'].append((foo, bar))
