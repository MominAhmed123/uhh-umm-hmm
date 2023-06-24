from manim import *
class Convex(Scene):
    def construct(self):
            plane = PolarPlane()
            r = lambda theta: 2*(np.sin(theta) + 1)
            convex_graph = plane.plot_polar_graph(r, [0, 2 * PI], color=RED).shift(DOWN*1)
            self.play(Create(convex_graph))
            convex_graph.set_fill(color = RED, opacity = 1)
            self.wait()
            temp = 2*np.sin((7/6)*PI) + 2
            p1 = Dot(plane.polar_to_point(temp, 7/6*PI)).shift(DOWN)
            p2 = Dot(plane.polar_to_point(temp, 11/6*PI)).shift(DOWN)
            l1 = Line(p1,p2, color = YELLOW)
            self.add(p1, p2)
            self.play(Create(l1))
            self.wait()
            r_2 = lambda theta: -2*np.sin(theta) -2
            concave_part = plane.plot_polar_graph(r_2, [(7/6)*PI , (11/6)*PI], color = GREEN).shift(DOWN*2)
            convex1 = plane.plot_polar_graph(r, [(-1/6)*PI, (7/6)*PI], color = RED).shift(DOWN*1)
            convex2 = plane.plot_polar_graph(r, [(11/6), 2*PI], color = RED).shift(DOWN*1)
            concave_group = Group(convex1, concave_part, convex2)
            self.play(Create(concave_part))
            concave_part.set_fill(color = BLUE, opacity = 0.5)
            self.wait()
            self.add(convex1)
            
            convex1.set_fill(color = BLUE, opacity = 0.5)
            
            self.wait()
            
    