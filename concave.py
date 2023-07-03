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
        #horizontal = Line([0,0], [1,0])
        rangle = l2.get_angle() 
        print(rangle)
        self.play(FadeOut(group1), group2.animate.rotate(PI - rangle))
        self.wait()
        a = Dot(color = WHITE).move_to(trace2.point_from_proportion(0))
        b = Dot(color = WHITE).move_to(trace2.point_from_proportion(1))
        A = Text("a").next_to(a, RIGHT)
        B = Text("b").next_to(b, LEFT)
        self.add(a,b,A,B)
        self.wait() 
        c = Dot(color = RED).move_to(trace2.point_from_proportion(0.5))
        C = Text("c", color = RED).next_to(c, UP)
        self.play(Create(c), Write(C))
        self.wait()
        l3 = Line(trace2.point_from_proportion(0), c, color = RED)
        l4 = Line(trace2.point_from_proportion(1), c, color = RED)
        self.play(Create(l3), Create(l4))
        self.wait()
        triangle = Polygon(trace2.point_from_proportion(0), c.get_center(), trace2.point_from_proportion(1), color = RED).set_fill(color = RED, opacity = 0.3)
        self.add(triangle)
        self.wait()
        angle = Angle(l4,l3, radius = 0.5, quadrant = (-1,-1) ).set_color(WHITE)
        value = DecimalNumber(angle.get_value(degrees=True), unit="^{\circ}")
        value.next_to(angle, DOWN)
        print(angle)
        self.add(angle,value)
        self.wait(2)




        

        
