from manim import *
import numpy as np

from momins_thing import coords
from perimeter import *
from chiakin import Object
from reflection import Reflection

class polygon(MovingCameraScene):
    def construct(self):
        obj = Object(coords)    
        Smoothed_obj = obj.Smooth_by_Chaikin(number_of_refinements = 3)
        if Smoothed_obj[0] == Smoothed_obj[-1]:
            print('work')
        just_coords = Smoothed_obj
        just_coords.pop()

        leng = find_half(Smoothed_obj)

        half_poly = Smoothed_obj[leng+1 : -1]
        discard_half = Smoothed_obj[: leng]
        line = Reflection(half_poly[0], half_poly[-1])
        reflected_half_poly = line.reflect_poly(half_poly)

        test = Polygon(*reflected_half_poly)
        half_poly_poly = Polygon(*half_poly).set_fill(GREEN, 0.5)
        poly = Polygon(*Smoothed_obj).set_fill(RED, 0.5)

        self.play(FadeIn(poly))
        self.wait(0.3)
        self.play(FadeIn(half_poly_poly))
        self.wait(0.3)
        self.play(half_poly_poly.animate(runtime=1).shift(RIGHT * 4))

        test.shift(RIGHT * 4)
        self.play(FadeIn(test))

        full_poly = half_poly + reflected_half_poly
        full_poly_polygon = Polygon(*full_poly).set_fill(BLUE, 0.5)
        full_poly_polygon.shift(RIGHT * 4)
        
        self.wait()

        animations = [FadeIn(full_poly_polygon),
                       FadeOut(half_poly_poly),
                       FadeOut(test)]
        self.wait()
        self.play(AnimationGroup(*animations), lag_ratio = 0.5)
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(full_poly_polygon))
        self.wait(0.3)

        
        next_poly = np.roll(full_poly, 1500).tolist()
        next_poly.append(next_poly[0])

        leng = find_half(next_poly)

        half_poly = next_poly[leng : -1]
        discard_half = next_poly[ : leng]
        line = Reflection(half_poly[0], half_poly[-1])
        reflected_half_poly = line.reflect_poly(half_poly)

        full_poly = half_poly + reflected_half_poly

        new_test = Polygon(*full_poly)
        new_half_poly_poly = Polygon(*half_poly)
        new_discard_poly = Polygon(*discard_half)
        new_half_poly_poly.shift(RIGHT * 4)
        self.add(new_half_poly_poly)
        self.play(new_half_poly_poly.animate().shift(RIGHT * 4))
        
        # self.play(new_test.animate(run_time=1, lag_ratio=0.1).shift(RIGHT * 2))