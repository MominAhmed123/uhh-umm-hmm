from manim import *
class concave(Scene):
    def construct(self):
        plane = PolarPlane()
        r = lambda theta: np.sin(theta) + 2
        graph = plane.plot_polar_graph(r , [0, 2*PI], color = RED)
        self.play(Create(graph))
