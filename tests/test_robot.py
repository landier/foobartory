from foobartory.robot import Robot


def test_mine_foo():
    # Given
    robot = Robot()

    # When
    robot.mine_foo()

    # Then
    assert robot.warehouses['foo'] == 1


def test_mine_foo_twice():
    # Given
    robot = Robot()

    # When
    robot.mine_foo()
    robot.mine_foo()

    # Then
    assert robot.warehouses['foo'] == 2


def test_mine_bar():
    # Given
    robot = Robot()

    # When
    robot.mine_bar()

    # Then
    assert robot.warehouses['bar'] == 1


def test_mine_bar_twice():
    # Given
    robot = Robot()

    # When
    robot.mine_bar()
    robot.mine_bar()

    # Then
    assert robot.warehouses['bar'] == 2
