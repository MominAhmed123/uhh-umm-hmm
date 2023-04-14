import math
import numpy as np

from typing import Tuple, List

Point = Tuple[float, float, float]

class Reflection:

    def __init__(self, line_point_1: Point, line_point_2: Point) -> None:
        self.line_point_1 = np.asarray(line_point_1, dtype=np.float128)
        self.line_point_2 = np.asarray(line_point_2, dtype=np.float128)
        self.gradient = self._get_gradient()
        self.intercept = self._get_intercept(self.line_point_1, self.gradient)
        self.norm_gradient = -1 / self.gradient


    def _get_gradient(self) -> float:
        dif = self.line_point_1 - self.line_point_2
        grad = dif[1] / dif[0]
        return grad


    def _get_intercept(self, point: np.array, gradient: float) -> float:
        return point[1] - gradient * point[0]


    def _normal_line_intersect(self, point: Point) -> Point:

        point = np.asarray(point, dtype=np.float128)
        new_intercept = self._get_intercept(point, self.norm_gradient)

        x = (self.intercept - new_intercept) / (self.norm_gradient - self.gradient)
        y = self.norm_gradient * x + new_intercept

        return (x, y, 0)


    def reflect(self, point: Point) -> Point:

        normal_line_intersect = self._normal_line_intersect(point)

        x = 2 * normal_line_intersect[0] - point[0]
        y = 2 * normal_line_intersect[1] - point[1]

        return (x, y, 0)


    def reflect_poly(self, points: List[Point]) -> List[Point]:

        reflected_points = []
        for point in points:
            reflected_points.append(self.reflect(point))
        reflected_points = reflected_points[::-1]

        return reflected_points
