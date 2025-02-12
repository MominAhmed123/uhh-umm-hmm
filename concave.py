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
        total = Group(group1, group2)
        self.play(total.animate.shift(RIGHT*2))
        duplicate = group2.copy()
        self.add(duplicate)
        self.play(duplicate.animate.shift(LEFT*5))
        duplicate2 = duplicate.copy()
        self.add(duplicate2)
        self.play(duplicate2.animate.rotate(PI).shift(UP*1.03 + RIGHT*0.25))
        self.wait()
        self.play(FadeOut(duplicate), FadeOut(duplicate2), total.animate.shift(LEFT*2))
        self.wait()
        self.remove(duplicate, duplicate2)
        #horizontal = Line([0,0], [1,0])
        rangle = l2.get_angle() 
        print(rangle)
        self.play(FadeOut(group1), group2.animate.rotate(PI - rangle))
        self.wait()
        a = Dot(color = WHITE).move_to(trace2.point_from_proportion(0))
        b = Dot(color = WHITE).move_to(trace2.point_from_proportion(1))
        A = always_redraw(lambda: Text("a").next_to(a, RIGHT))
        B = always_redraw(lambda: Text("b").next_to(b, LEFT))
        self.add(a,b,A,B)
        self.wait() 
        c = Dot(color = RED).move_to(trace2.point_from_proportion(0.5))
        C = Text("c", color = RED).next_to(c, UP)
        self.play(Create(c), Write(C))
        self.wait()
        lab = always_redraw(lambda: Line(c.get_center(), b.get_center(), color = RED))
        lac = always_redraw(lambda: Line(a.get_center(), c.get_center(), color = RED))
        lbc = always_redraw(lambda: Line(b.get_center(), c.get_center(), color = RED))
        self.play(Create(lac), Create(lbc))
        self.wait()
        triangle = always_redraw(lambda: Polygon(a.get_center(), b.get_center() , c.get_center(), color = RED).set_fill(color = RED, opacity = 0.5))
        bc =  VMobject().set_points([trace2.point_from_proportion(0)])
        for n in np.linspace(0,1/2,15):
            bc.add_smooth_curve_to(trace2.point_from_proportion(n))
        bc.set_stroke(color=TEAL, width=3, opacity=1).set_fill(color = TEAL)
        bc.set_fill(color = TEAL, opacity = 0.5)
        ac =  VMobject().set_points([trace2.point_from_proportion(1/2)])
        for n in np.linspace(1/2,1,15):
            ac.add_smooth_curve_to(trace2.point_from_proportion(n))
        ac.set_stroke(color=TEAL, width=3, opacity=1).set_fill(color = TEAL)
        ac.set_fill(color = TEAL, opacity = 0.5)
        self.add(triangle, bc, ac)
        self.remove(group2)
        self.wait()
        angle = always_redraw(lambda: Angle(lbc,lac, radius = 0.5, quadrant = (-1,-1) ).set_color(WHITE))
        value = always_redraw(lambda: DecimalNumber( Angle(lbc,lac, quadrant = (-1,-1)).get_value(degrees=True), unit="^{\circ}").next_to(angle, DOWN))
        self.add(angle,value)
        self.wait(2)
        self.play(Rotate(ac, about_point = c.get_center(), angle = -10*DEGREES), Rotate(bc, about_point = c.get_center(), angle = 10*DEGREES), Rotate(b, about_point = c.get_center(), angle = -10*DEGREES), Rotate(a, about_point = c.get_center(), angle = 10*DEGREES), runtime = 3)
        self.wait()
        self.play(Rotate(ac, about_point = c.get_center(), angle = 20*DEGREES), Rotate(bc, about_point = c.get_center(), angle = -20*DEGREES), Rotate(b, about_point = c.get_center(), angle = 20*DEGREES), Rotate(a, about_point = c.get_center(), angle = -20*DEGREES), runtime = 3)
        self.wait()
        self.play(Rotate(ac, about_point = c.get_center(), angle = -8.435*DEGREES), Rotate(bc, about_point = c.get_center(), angle = 8.435*DEGREES), Rotate(b, about_point = c.get_center(), angle = -8.435*DEGREES), Rotate(a, about_point = c.get_center(), angle = 8.435*DEGREES), runtime = 3)
        self.wait()


        

        
