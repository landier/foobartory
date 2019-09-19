import os
import time
from random import randrange, uniform
from uuid import uuid4


TEST = os.environ.get('TEST', None)


class Robot:
    def __init__(self, warehouses, id=None):
        self._id = id
        self._warehouses = warehouses
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
        elif activity == 'sell_foobars' and self._last_action in [None, 'sell_foobars', 'move']:
            self._last_action = 'sell_foobars'
            self._get_busy_for(10)
            return True
        else:
            self._last_action = 'move'
            self._get_busy_for(5)
            return False

    def mine_foo(self):
        if self._execute_action_or_move('mine_foo'):
            self._warehouses['foo'].append(uuid4())

    def mine_bar(self):
        if self._execute_action_or_move('mine_bar'):
            self._warehouses['bar'].append(uuid4())

    def assemble_foobar(self, success_threshold=60):
        if self._execute_action_or_move('assemble_foobar'):
            foo = self._warehouses['foo'].pop()
            if randrange(100) <= success_threshold:
                bar = self._warehouses['bar'].pop()
                self._warehouses['foobar'].append((foo, bar))

    def sell_foobars(self):
        if self._execute_action_or_move('sell_foobars'):
            sold_foobars = min(len(self._warehouses['foobar']), 5)
            for i in range(sold_foobars):
                self._warehouses['foobar'].pop()
            self._warehouses['money'] += sold_foobars

    def _is_foo_stock_low(self):
        return len(self._warehouses['foo']) == 0

    def _is_bar_stock_low(self):
        return len(self._warehouses['bar']) == 0

    def _can_assemble_foobar(self):
        return not (self._is_foo_stock_low() or self._is_bar_stock_low())

    def _can_sell_foobars(self):
        return len(self._warehouses['foobar']) >= 5

    def next_action(self, success_threshold=60):
        if self._can_sell_foobars():
            self.sell_foobars()
        elif self._is_foo_stock_low():
            self.mine_foo()
        elif self._is_bar_stock_low():
            self.mine_bar()
        elif self._can_assemble_foobar():
            self.assemble_foobar(success_threshold)
