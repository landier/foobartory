import time
from collections import defaultdict


class Robot:
    def __init__(self):
        self.warehouses = defaultdict(lambda: 0)

    def move(self):
        pass

    def mine_foo(self):
        time.sleep(1)
        self.warehouses['foo'] += 1

    def mine_bar(self):
        pass

    def build_foobar(self):
        pass
