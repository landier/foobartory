from collections import defaultdict
import unittest
from uuid import UUID
from foobartory.robot import Robot


class RobotTest(unittest.TestCase):
    def setup_method(self, test_method):
        warehouses = defaultdict(list)
        warehouses['robot'] = []
        warehouses['money'] = 0
        self.robot = Robot(warehouses)
        self.foo = UUID('62c0727a-0938-44d9-a268-66b84baf4ff6')
        self.bar = UUID('f9d527e1-4b86-4f54-8579-e5b9b3432362')

    def test_mine_foo(self):
        # Given

        # When
        self.robot.mine_foo()

        # Then
        assert len(self.robot._warehouses['foo']) == 1

    def test_mine_foo_twice(self):
        # Given

        # When
        self.robot.mine_foo()
        self.robot.mine_foo()

        # Then
        assert len(self.robot._warehouses['foo']) == 2

    def test_mine_bar(self):
        # Given

        # When
        self.robot.mine_bar()

        # Then
        assert len(self.robot._warehouses['bar']) == 1

    def test_mine_bar_twice(self):
        # Given

        # When
        self.robot.mine_bar()
        self.robot.mine_bar()

        # Then
        assert len(self.robot._warehouses['bar']) == 2

    def test_assemble_foobar_when_success(self):
        # Given
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["bar"].append(self.bar)

        # When
        self.robot.assemble_foobar(success_threshold=100)

        # Then
        assert len(self.robot._warehouses['foo']) == 0
        assert len(self.robot._warehouses['bar']) == 0
        assert len(self.robot._warehouses['foobar']) == 1
        assert self.robot._warehouses['foobar'][0] == (self.foo, self.bar)

    def test_assemble_foobar_when_failure(self):
        # Given
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["bar"].append(self.bar)

        # When
        self.robot.assemble_foobar(success_threshold=0)

        # Then
        assert len(self.robot._warehouses['foo']) == 0
        assert len(self.robot._warehouses['bar']) == 1
        assert self.robot._warehouses['bar'][0] == self.bar
        assert len(self.robot._warehouses['foobar']) == 0

    def test_mine_foo_then_mine_bar_should_not_mine_bar_but_move(self):
        # Given

        # When
        self.robot.mine_foo()
        self.robot.mine_bar()

        # Then
        assert len(self.robot._warehouses['foo']) == 1
        assert len(self.robot._warehouses['bar']) == 0
        assert self.robot._last_action == 'move'

    def test_mine_bar_then_mine_foo_should_not_mine_foo_but_move(self):
        # Given

        # When
        self.robot.mine_bar()
        self.robot.mine_foo()

        # Then
        assert len(self.robot._warehouses['foo']) == 0
        assert len(self.robot._warehouses['bar']) == 1
        assert self.robot._last_action == 'move'

    def test_can_assemble_foobar_when_no_foo_but_bar(self):
        # Given
        self.robot._warehouses["bar"].append(self.bar)

        # When & Then
        assert self.robot._can_assemble_foobar() is False

    def test_can_assemble_foobar_when_foo_but_no_bar(self):
        # Given
        self.robot._warehouses["foo"].append(self.foo)

        # When & Then
        assert self.robot._can_assemble_foobar() is False

    def test_can_assemble_foobar_when_less_than_5_foo(self):
        # Given
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["bar"].append(self.bar)

        # When & Then
        assert self.robot._can_assemble_foobar() is False

    def test_can_assemble_foobar_when_more_than_5_foo_and_1_bar(self):
        # Given
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["bar"].append(self.bar)

        # When & Then
        assert self.robot._can_assemble_foobar() is True

    def test_next_action_when_no_bar_then_mine_bar(self):
        # Given

        # When
        self.robot.next_action()

        # Then
        assert len(self.robot._warehouses['foo']) == 0
        assert len(self.robot._warehouses['bar']) == 1
        assert len(self.robot._warehouses['foobar']) == 0

    def test_next_action_when_no_foo_then_mine_bar(self):
        # Given

        # When
        self.robot.next_action()

        # Then
        assert len(self.robot._warehouses['foo']) == 0
        assert len(self.robot._warehouses['bar']) == 1
        assert len(self.robot._warehouses['foobar']) == 0

    def test_next_action_when_foo_but_no_bar_then_mine_bar(self):
        # Given
        self.robot._warehouses["foo"].append(self.foo)

        # When
        self.robot.next_action()

        # Then
        assert len(self.robot._warehouses['foo']) == 1
        assert len(self.robot._warehouses['bar']) == 1
        assert len(self.robot._warehouses['foobar']) == 0

    def test_next_action_when_foo_and_bar_then_assemble_foobar(self):
        # Given
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["foo"].append(self.foo)
        self.robot._warehouses["bar"].append(self.bar)

        # When
        self.robot.next_action(success_threshold=100)

        # Then
        assert len(self.robot._warehouses['foo']) == 5
        assert len(self.robot._warehouses['bar']) == 0
        assert len(self.robot._warehouses['foobar']) == 1
        assert self.robot._warehouses['foobar'][0] == (self.foo, self.bar)
