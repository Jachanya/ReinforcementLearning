from manim import *

class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)

class CreateCircle(Scene):
    def construct(self):

        circles = [Circle() for _ in range(10)]
        circles = list(map(lambda circle: circle.set_fill(PINK, opacity=0.5), circles))
        for index, circle in enumerate(circles):
            if index == 0:
                continue

            circle.next_to(circles[index-1], RIGHT, buff=0.5)

        circles = list(map(lambda circle: Create(circle), circles))

        tex = Tex(r'\[ x^n + y^n = z^n \]', font_size=144)

        code = '''from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        
        self.play(Create(rendered_code))

        tex.next_to(rendered_code, RIGHT, buff=0.2)
        self.play(Create(tex))

        self.play(*circles)  # show the circle on screen
