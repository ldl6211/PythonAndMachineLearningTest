from random import choice
from matplotlib.pyplot import *


class RandomWalk():
    def __init__(self, numPoint):
        self.numPoint = numPoint

    x_value = [0]
    y_value = [0]

    def fillWalk(self):
        while len(self.x_value) < self.numPoint:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x_next = self.x_value[-1] + x_step
            y_next = self.y_value[-1] + y_step

            self.x_value.append(x_next)
            self.y_value.append(y_next)

        return self.x_value, self.y_value


def main():
    rw = RandomWalk(5000)
    x_list, y_list = rw.fillWalk()
    figure(figsize=(10, 6))
    scatter(x_list[1:-1], y_list[1:-1], s=1, c='red', edgecolors='none')
    scatter(x_list[0], y_list[0], s=10, c='blue', edgecolors='none')
    scatter(x_list[-1], y_list[-1], s=10, c='green', edgecolors='none')
    # axes().get_xaxis().set_visible(False)
    # axes().get_yaxis().set_visible(False)
    show()


main()
