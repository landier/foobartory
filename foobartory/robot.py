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
        if TEST is None:
            time.sleep(duration)

    def _execute_action_or_move(self, activity):
        self._nb_actions += 1
        if activity == 'mine_foo' and self._last_action in [None, 'mine_foo', 'move']:
            self._last_action = 'mine_foo'
            self._get_busy_for(1)
            return True
        elif activity == 'mine_bar' and self._last_action in [None, 'mine_bar', 'move']:
            self._last_action = 'mine_bar'
            mining_duration = uniform(0.5, 2)
            self._get_busy_for(mining_duration)
            return True
        elif activity == 'assemble_foobar' and self._last_action in [None, 'assemble_foobar', 'move']:
            self._last_action = 'assemble_foobar'
            self._get_busy_for(2)
            return True
        else:
            self._last_action = 'move'
            self._get_busy_for(5)
            return False

    def mine_foo(self):
        if self._execute_action_or_move('mine_foo'):
            self.warehouses['foo'].append(uuid4())

    def mine_bar(self):
        if self._execute_action_or_move('mine_bar'):
            self.warehouses['bar'].append(uuid4())

    def assemble_foobar(self, success_threshold=60):
        if self._execute_action_or_move('assemble_foobar'):
            foo = self.warehouses['foo'].pop()
            if randrange(100) <= success_threshold:
                bar = self.warehouses['bar'].pop()
                self.warehouses['foobar'].append((foo, bar))

    def _is_foo_stock_low(self):
        return len(self.warehouses['foo']) == 0

    def _is_bar_stock_low(self):
        return len(self.warehouses['bar']) == 0

    def _can_assemble_foobar(self):
        return not (self._is_foo_stock_low() or self._is_bar_stock_low())

    def next_action(self, success_threshold=60):
        if self._is_foo_stock_low():
            self.mine_foo()
        elif self._is_bar_stock_low():
            self.mine_bar()
        elif self._can_assemble_foobar():
            self.assemble_foobar(success_threshold)
