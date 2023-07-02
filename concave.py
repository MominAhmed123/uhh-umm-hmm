from manim import *
class concave(Scene):
    def construct(self):
        plane = PolarPlane()
        r = lambda theta: np.sin(theta) + 2
        graph = plane.plot_polar_graph(r , [0, 2*PI], color = RED)
        self.play(Create(graph))
        self.wait()             
        prop = ValueTracker(0)
        dot = always_redraw(lambda:
            Dot(color=TEAL).move_to(graph.point_from_proportion(prop.get_value()))
        )
        self.add(dot)
        self.play(prop.animate.set_value(1), run_time  = 2)
        self.wait()

        trace1 = VMobject().set_points([graph.point_from_proportion(0)])
        for n in np.linspace(0,1/2,30):
            trace1.add_smooth_curve_to(graph.point_from_proportion(n))
        
        trace1.set_stroke(color=YELLOW, width=3, opacity=1)
        self.add(trace1)

        trace2 = VMobject().set_points([graph.point_from_proportion(1/2)])
        for n in np.linspace(1/2,1,30):
            trace2.add_smooth_curve_to(graph.point_from_proportion(n))
        
        trace2.set_stroke(color=TEAL, width=3, opacity=1)
        self.add(trace2)
        self.wait()
        self.remove(graph)
        self.remove(dot)
        l1 = Line(graph.point_from_proportion(0), graph.point_from_proportion(1/2))
        l1.set_stroke(color=YELLOW, width=3, opacity=1)
        group1 = Group(trace1, l1)
        l2 = Line(graph.point_from_proportion(1/2), graph.point_from_proportion(1))
        l2.set_stroke(color=TEAL, width=3, opacity=1)
        group2 = Group(trace2, l2)
        
        self.play(Create(l1), Create(l2))
        
        
        trace1.set_fill(color = YELLOW, opacity = 0.5)
        trace2.set_fill(color = TEAL, opacity = 0.5)
        self.wait()
        self.play(group1.animate.shift(UP*0.5), group2.animate.shift(DOWN*0.5))
        self.wait()
        
