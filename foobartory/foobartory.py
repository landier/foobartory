from collections import defaultdict
from robot import Robot


INITIAL_NB_ROBOTS = 2
FINAL_NB_ROBOTS = 30


class Foobartory:
    def __init__(self):
        self._robots = []
        self._warehouses = defaultdict(list)

    def _display_stats(self):
        print("-"*20)
        print(f"robots: {len(self._robots)}")
        print(f"foo: {len(self._warehouses['foo'])}")
        print(f"bar: {len(self._warehouses['bar'])}")
        print(f"foobar: {len(self._warehouses['foobar'])}")
        print("#"*20)

    def run(self):
        for id in range(INITIAL_NB_ROBOTS):
            self._robots.append(Robot(self._warehouses, id))

        while len(self._robots) < FINAL_NB_ROBOTS:
            for robot in self._robots:
                print(f"Robot {robot._id} acting")
                robot.next_action()
                self._display_stats()


if __name__ == '__main__':
    foobartory = Foobartory()
    foobartory.run()
