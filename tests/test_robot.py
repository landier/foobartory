from collections import defaultdict
from uuid import UUID
from foobartory.robot import Robot


def test_mine_foo():
    # Given
    robot = Robot(warehouses=defaultdict(list))

    # When
    robot.mine_foo()

    # Then
    assert len(robot._warehouses['foo']) == 1


def test_mine_foo_twice():
    # Given
    robot = Robot(warehouses=defaultdict(list))

    # When
    robot.mine_foo()
    robot.mine_foo()

    # Then
    assert len(robot._warehouses['foo']) == 2


def test_mine_bar():
    # Given
    robot = Robot(warehouses=defaultdict(list))

    # When
    robot.mine_bar()

    # Then
    assert len(robot._warehouses['bar']) == 1


def test_mine_bar_twice():
    # Given
    robot = Robot(warehouses=defaultdict(list))

    # When
    robot.mine_bar()
    robot.mine_bar()

    # Then
    assert len(robot._warehouses['bar']) == 2


def test_assemble_foobar_when_success():
    # Given
    robot = Robot(warehouses=defaultdict(list))
    foo = UUID('62c0727a-0938-44d9-a268-66b84baf4ff6')
    bar = UUID('f9d527e1-4b86-4f54-8579-e5b9b3432362')
    robot._warehouses["foo"].append(foo)
    robot._warehouses["bar"].append(bar)

    # When
    robot.assemble_foobar(success_threshold=100)

    # Then
    assert len(robot._warehouses['foo']) == 0
    assert len(robot._warehouses['bar']) == 0
    assert len(robot._warehouses['foobar']) == 1
    assert robot._warehouses['foobar'][0] == (foo, bar)


def test_assemble_foobar_when_failure():
    # Given
    robot = Robot(warehouses=defaultdict(list))
    foo = UUID('62c0727a-0938-44d9-a268-66b84baf4ff6')
    bar = UUID('f9d527e1-4b86-4f54-8579-e5b9b3432362')
    robot._warehouses["foo"].append(foo)
    robot._warehouses["bar"].append(bar)

    # When
    robot.assemble_foobar(success_threshold=0)

    # Then
    assert len(robot._warehouses['foo']) == 0
    assert len(robot._warehouses['bar']) == 1
    assert robot._warehouses['bar'][0] == bar
    assert len(robot._warehouses['foobar']) == 0


def test_mine_foo_then_mine_bar_should_not_mine_bar_but_move():
    # Given
    robot = Robot(warehouses=defaultdict(list))

    # When
    robot.mine_foo()
    robot.mine_bar()

    # Then
    assert len(robot._warehouses['foo']) == 1
    assert len(robot._warehouses['bar']) == 0
    assert robot._last_action == 'move'


def test_mine_bar_then_mine_foo_should_not_mine_foo_but_move():
    # Given
    robot = Robot(warehouses=defaultdict(list))

    # When
    robot.mine_bar()
    robot.mine_foo()

    # Then
    assert len(robot._warehouses['foo']) == 0
    assert len(robot._warehouses['bar']) == 1
    assert robot._last_action == 'move'


def test_can_assemble_foobar_when_no_foo_but_bar():
    # Given
    robot = Robot(warehouses=defaultdict(list))
    bar = UUID('f9d527e1-4b86-4f54-8579-e5b9b3432362')
    robot._warehouses["bar"].append(bar)

    # When & Then
    assert robot._can_assemble_foobar() is False


def test_can_assemble_foobar_when_foo_but_no_bar():
    # Given
    robot = Robot(warehouses=defaultdict(list))
    foo = UUID('62c0727a-0938-44d9-a268-66b84baf4ff6')
    robot._warehouses["foo"].append(foo)

    # When & Then
    assert robot._can_assemble_foobar() is False


def test_can_assemble_foobar_when_foo_and_bar():
    # Given
    robot = Robot(warehouses=defaultdict(list))
    foo = UUID('62c0727a-0938-44d9-a268-66b84baf4ff6')
    bar = UUID('f9d527e1-4b86-4f54-8579-e5b9b3432362')
    robot._warehouses["foo"].append(foo)
    robot._warehouses["bar"].append(bar)

    # When & Then
    assert robot._can_assemble_foobar() is True


def test_next_action_when_no_foo_then_mine_foo():
    # Given
    robot = Robot(warehouses=defaultdict(list))

    # When
    robot.next_action()

    # Then
    assert len(robot._warehouses['foo']) == 1
    assert len(robot._warehouses['bar']) == 0
    assert len(robot._warehouses['foobar']) == 0


def test_next_action_when_foo_but_no_bar_then_mine_bar():
    # Given
    robot = Robot(warehouses=defaultdict(list))
    foo = UUID('62c0727a-0938-44d9-a268-66b84baf4ff6')
    robot._warehouses["foo"].append(foo)

    # When
    robot.next_action()

    # Then
    assert len(robot._warehouses['foo']) == 1
    assert len(robot._warehouses['bar']) == 1
    assert len(robot._warehouses['foobar']) == 0


def test_next_action_when_foo_and_bar_then_assemble_foobar():
    # Given
    robot = Robot(warehouses=defaultdict(list))
    foo = UUID('62c0727a-0938-44d9-a268-66b84baf4ff6')
    bar = UUID('f9d527e1-4b86-4f54-8579-e5b9b3432362')
    robot._warehouses["foo"].append(foo)
    robot._warehouses["bar"].append(bar)

    # When
    robot.next_action(success_threshold=100)

    # Then
    assert len(robot._warehouses['foo']) == 0
    assert len(robot._warehouses['bar']) == 0
    assert len(robot._warehouses['foobar']) == 1
    assert robot._warehouses['foobar'][0] == (foo, bar)
