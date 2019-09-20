from collections import defaultdict
from robot import Robot


INITIAL_NB_ROBOTS = 2
FINAL_NB_ROBOTS = 30


class Foobartory:
    def __init__(self):
        self._warehouses = defaultdict(list)
        self._warehouses['robot'] = []
        self._warehouses['money'] = 0

    def _display_stats(self):
        print("-"*20)
        print(f"robots: {len(self._warehouses['robot'])}")
        print(f"money: {self._warehouses['money']}")
        print(f"foo: {len(self._warehouses['foo'])}")
        print(f"bar: {len(self._warehouses['bar'])}")
        print(f"foobar: {len(self._warehouses['foobar'])}")

    def run(self):
        for i in range(INITIAL_NB_ROBOTS):
            self._warehouses['robot'].append(Robot(self._warehouses))

        while len(self._warehouses['robot']) < FINAL_NB_ROBOTS:
            for robot in self._warehouses['robot']:
                robot.next_action()
                self._display_stats()
                if len(self._warehouses['robot']) == FINAL_NB_ROBOTS:
                    break


if __name__ == '__main__':
    foobartory = Foobartory()
    foobartory.run()
