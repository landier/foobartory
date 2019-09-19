from uuid import UUID
from foobartory.robot import Robot


def test_mine_foo():
    # Given
    robot = Robot()

    # When
    robot.mine_foo()

    # Then
    assert len(robot.warehouses['foo']) == 1


def test_mine_foo_twice():
    # Given
    robot = Robot()

    # When
    robot.mine_foo()
    robot.mine_foo()

    # Then
    assert len(robot.warehouses['foo']) == 2


def test_mine_bar():
    # Given
    robot = Robot()

    # When
    robot.mine_bar()

    # Then
    assert len(robot.warehouses['bar']) == 1


def test_mine_bar_twice():
    # Given
    robot = Robot()

    # When
    robot.mine_bar()
    robot.mine_bar()

    # Then
    assert len(robot.warehouses['bar']) == 2


def test_assemble_foobar_when_success():
    # Given
    robot = Robot()
    foo = UUID('62c0727a-0938-44d9-a268-66b84baf4ff6')
    bar = UUID('f9d527e1-4b86-4f54-8579-e5b9b3432362')
    robot.warehouses["foo"].append(foo)
    robot.warehouses["bar"].append(bar)

    # When
    robot.assemble_foobar(success_threshold=100)

    # Then
    assert len(robot.warehouses['foo']) == 0
    assert len(robot.warehouses['bar']) == 0
    assert len(robot.warehouses['foobar']) == 1
    assert robot.warehouses['foobar'][0] == (foo, bar)


def test_assemble_foobar_when_failure():
    # Given
    robot = Robot()
    foo = UUID('62c0727a-0938-44d9-a268-66b84baf4ff6')
    bar = UUID('f9d527e1-4b86-4f54-8579-e5b9b3432362')
    robot.warehouses["foo"].append(foo)
    robot.warehouses["bar"].append(bar)

    # When
    robot.assemble_foobar(success_threshold=0)

    # Then
    assert len(robot.warehouses['foo']) == 0
    assert len(robot.warehouses['bar']) == 1
    assert robot.warehouses['bar'][0] == bar
    assert len(robot.warehouses['foobar']) == 0


def test_mine_foo_then_mine_bar_should_not_mine_bar_but_move():
    # Given
    robot = Robot()

    # When
    robot.mine_foo()
    robot.mine_bar()

    # Then
    assert len(robot.warehouses['foo']) == 1
    assert len(robot.warehouses['bar']) == 0
    assert robot._last_action == 'move'
