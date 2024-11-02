from manim import *

WAIT_TIME = 0.5


class VectorConcepts(Scene):
    def construct(self):
        # Slide 1: Title and Subtitle
        title = Text("Vector", font_size=48)
        subtitle = Text("Vector Perspectives",
                        font_size=36).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(WAIT_TIME)

        # Indicate slide change
        self.next_section(
            name="Introduction to Vector Perspectives", skip_animations=False)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(WAIT_TIME)

        # Slide 2: Physics Example - Vector as an Arrow
        label = Text("Physics: Vector as an Arrow",
                     font_size=36).shift(UP * 3)
        physics_vector_1 = Vector(RIGHT * 3, color=BLUE).shift(RIGHT + DOWN)
        physics_vector_2 = Vector(UP * 2 + RIGHT * 3, color=RED).shift(LEFT)
        physics_vector_3 = Vector(DOWN * 2 + LEFT * 2, color=GREEN)
        physics_group = VGroup(
            physics_vector_1, physics_vector_2, physics_vector_3, label
        )

        self.play(FadeIn(physics_group))
        self.next_section(name="Computer Science Vector",
                          skip_animations=False)
        self.play(FadeOut(physics_group))
        self.wait(WAIT_TIME)

        # Slide 3: Computer Science Example - Vector as a List
        label = Text("Computer Science: Vector as a List",
                     font_size=36).shift(UP * 3)
        cs_vector_1 = Matrix([[1], [0], [-1], [2]],
                             left_bracket="(", right_bracket=")").shift(LEFT * 2)
        cs_vector_2 = Matrix([[1], [2], [3], [4]],
                             left_bracket="(", right_bracket=")")
        cs_vector_3 = Matrix([[1], [0], [0], [1]],
                             left_bracket="(", right_bracket=")").shift(RIGHT * 2)
        cs_group = VGroup(cs_vector_1, cs_vector_2, cs_vector_3, label)

        self.play(FadeIn(cs_vector_1), FadeIn(cs_vector_2),
                  FadeIn(cs_vector_3), Write(label))

        self.next_section(name="Mathematics Vector", skip_animations=False)
        self.play(FadeOut(cs_group))
        self.wait(WAIT_TIME)

        # Slide 4: Mathematics Example - Vector with a Transforming Grid
        label = Text("Mathematics: Abstract Vector Space",
                     font_size=36).shift(UP * 3)
        grid = NumberPlane(
            x_range=[-20, 20], y_range=[-20, 20],
            background_line_style={"stroke_opacity": 0.4}
        )

        math_vector_u = Vector(2 * RIGHT, color=GREEN)
        math_annotation_u = MathTex(r"\vec{u} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}").next_to(
            math_vector_u.get_end()
        )
        math_vector_v = Vector(2 * UP, color=YELLOW)
        math_annotation_v = MathTex(r"\vec{v} = \begin{bmatrix} 0 \\ 2 \end{bmatrix}").next_to(
            math_vector_v.get_end()
        )

        self.play(
            FadeIn(grid),
            FadeIn(math_vector_u), FadeIn(math_annotation_u),
            FadeIn(math_vector_v), FadeIn(math_annotation_v),
            Write(label)
        )

        # Transforming Grid Example
        self.next_section(name="Transforming Grid Example",
                          skip_animations=False)
        transform_matrix = [[0, 1], [1, 0]]  # Simple rotation/flip matrix

        self.play(
            grid.animate.apply_matrix(transform_matrix),
            math_vector_u.animate.apply_matrix(transform_matrix),
            math_vector_v.animate.apply_matrix(transform_matrix),
            math_annotation_u.animate.move_to(math_vector_v.get_end()),
            math_annotation_v.animate.move_to(math_vector_u.get_end())
        )

        # Final Slide: Fade Out All Elements
        self.next_section(name="Wait", skip_animations=False)
        self.play(
            FadeOut(grid), FadeOut(math_vector_u), FadeOut(math_vector_v),
            FadeOut(math_annotation_u), FadeOut(math_annotation_v)
        )
        self.wait(WAIT_TIME)


class VectorAddition(Scene):
    def construct(self):
        # Slide 1: Title and Subtitle
        title = Text("Vector Addition", font_size=48)
        subtitle = Text("Combining Vectors Geometrically",
                        font_size=36).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(WAIT_TIME)

        # Indicate slide change
        self.next_section(
            name="Introduction to Vector Addition", skip_animations=False)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(WAIT_TIME)

        # Slide 2: Explanation of Vector Addition
        explanation = Text(
            "Vector addition is performed by aligning\n"
            "the tail of one vector to the tip of another,\n"
            "creating a new vector representing the\n"
            "combined movement.", font_size=24
        ).shift(UP * 3)

        self.play(Write(explanation))
        self.wait(WAIT_TIME)

        self.next_section(name="Vector Addition Animation",
                          skip_animations=False)
        self.wait(WAIT_TIME)
        self.play(FadeOut(explanation))

        # Slide 3: Example of Vector Addition
        vector_A = Vector(3 * RIGHT, color=BLUE)
        vector_A_annotation = MathTex(
            r"\vec{A} = \begin{bmatrix} 3 \\ 0 \end{bmatrix}").next_to(vector_A.get_end())

        vector_B = Vector(2 * UP, color=GREEN)
        vector_B_annotation = MathTex(
            r"\vec{B} = \begin{bmatrix} 0 \\ 2 \end{bmatrix}").next_to(vector_B.get_end())

        vector_sum = Vector(vector_A.get_end() +
                            vector_B.get_end(), color=YELLOW)
        vector_sum_annotation = MathTex(
            r"\vec{A} + \vec{B} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}").next_to(vector_sum.get_end())

        grid = NumberPlane()

        # Creating the arrows
        self.play(GrowArrow(vector_A), GrowArrow(vector_B), FadeIn(grid),
                  Write(vector_A_annotation), Write(vector_B_annotation))

        self.next_section(name="Vector Addition Animation",
                          skip_animations=False)
        self.play(vector_B.animate.shift(vector_A.get_end()))
        self.wait(WAIT_TIME)

        self.next_section(name="Vector Addition Animation",
                          skip_animations=False)
        self.play(GrowArrow(vector_sum), Write(vector_sum_annotation))
        self.wait(WAIT_TIME)

        # Slide 4: Another Example of Vector Addition
        vector_C = Vector(3 * DOWN, color=RED)
        vector_C_annotation = MathTex(
            r"\vec{C} = \begin{bmatrix} 0 \\ -3 \end{bmatrix}").next_to(vector_C.get_end(), RIGHT)

        vector_D = Vector(2 * LEFT, color=ORANGE)
        vector_D_annotation = MathTex(
            r"\vec{D} = \begin{bmatrix} -2 \\ 0 \end{bmatrix}").next_to(vector_D.get_end(), LEFT)

        vector_sum_2 = Vector(vector_C.get_end() +
                              vector_D.get_end(), color=PURPLE)
        vector_sum_2_annotation = MathTex(
            r"\vec{C} + \vec{D} = \begin{bmatrix} -2 \\ -3 \end{bmatrix}").next_to(vector_sum_2.get_end(), LEFT)

        self.play(GrowArrow(vector_C), GrowArrow(vector_D),
                  Write(vector_C_annotation), Write(vector_D_annotation))

        self.next_section(name="Vector Addition Animation",
                          skip_animations=False)
        self.play(vector_D.animate.shift(vector_C.get_end()))
        self.wait(WAIT_TIME)

        self.next_section(name="Vector Addition Animation",
                          skip_animations=False)
        self.play(GrowArrow(vector_sum_2), Write(vector_sum_2_annotation))
        self.wait(WAIT_TIME)

        # Final Slide: Clear All
        self.next_section(name="Clear Everything", skip_animations=False)
        self.play(FadeOut(vector_A), FadeOut(vector_B), FadeOut(vector_sum), FadeOut(vector_C),
                  FadeOut(vector_D), FadeOut(vector_sum_2),
                  FadeOut(vector_A_annotation), FadeOut(
                      vector_B_annotation), FadeOut(vector_C_annotation),
                  FadeOut(vector_D_annotation), FadeOut(
                      vector_sum_annotation), FadeOut(vector_sum_2_annotation),
                  FadeOut(grid))
        self.wait(WAIT_TIME)


class ScalarMultiplication(Scene):
    def construct(self):
        # Slide 1: Title and Subtitle
        title = Text("Scalar Multiplication", font_size=48)
        subtitle = Text("Scaling Vectors",
                        font_size=36).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(WAIT_TIME)

        # Indicate slide change
        self.next_section(
            name="Introduction to Scalar Multiplication", skip_animations=False)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(WAIT_TIME)

        # Slide 2: Explanation of Scalar Multiplication
        explanation = Text(
            "Scalar multiplication alters a vector's length\n"
            "without changing its direction unless the scalar\n"
            "is negative, in which case it reverses direction.",
            font_size=24
        ).shift(UP * 3)

        self.play(Write(explanation))
        self.wait(WAIT_TIME)

        self.next_section(name="Scalar Multiplication Examples",
                          skip_animations=False)
        self.play(FadeOut(explanation))

        # Slide 3: Example of Scalar Multiplication
        grid = NumberPlane()
        vector = Vector(2 * RIGHT + 1 * UP, color=BLUE)
        vector_annotation = MathTex(
            r"\vec{v} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}").next_to(vector.get_end(), RIGHT)

        scalar_2 = Vector(2 * (2 * RIGHT + 1 * UP), color=GREEN)
        scalar_2_annotation = MathTex(
            r"2 \cdot \vec{v} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}").next_to(scalar_2.get_end(), RIGHT)

        scalar_neg_1 = Vector(-2 * (2 * RIGHT + 1 * UP), color=RED)
        scalar_neg_1_annotation = MathTex(
            r"-2 \cdot \vec{v} = \begin{bmatrix} -2 \\ -1 \end{bmatrix}").next_to(scalar_neg_1.get_end(), DOWN)

        self.play(GrowArrow(vector), FadeIn(grid))
        self.play(Write(vector_annotation))
        self.wait(WAIT_TIME)

        self.next_section(name="Scalar Multiplication Examples",
                          skip_animations=False)
        self.play(Transform(vector, scalar_2),
                  Transform(vector_annotation, scalar_2_annotation))
        self.wait(WAIT_TIME)

        self.next_section(name="Scalar Multiplication Examples",
                          skip_animations=False)
        self.play(Transform(vector, scalar_neg_1),
                  Transform(vector_annotation, scalar_neg_1_annotation))
        self.wait(WAIT_TIME)

        self.next_section()
        self.play(GrowArrow(scalar_2), Write(scalar_2_annotation))
        self.wait(WAIT_TIME)

        # Final Slide: Clear All
        self.next_section(name="Clear Everything", skip_animations=False)
        self.play(FadeOut(vector), FadeOut(scalar_2),
                  FadeOut(scalar_neg_1), FadeOut(vector_annotation),
                  FadeOut(scalar_2_annotation), FadeOut(
                      scalar_neg_1_annotation),
                  FadeOut(grid))
        self.wait(WAIT_TIME)


class IntroToLinearTransformation(Scene):
    def construct(self):
        WAIT_TIME = 1  # Adjust the wait time as needed

        # Slide 1: Title and Definition
        title = Text("Intro to Linear Transformation", font_size=48)
        subtitle = Text("Definition of Linear Transformations",
                        font_size=36).next_to(title, DOWN)
        definition = Text(
            "Linear transformations map vectors to other vectors\n"
            "while preserving properties: lines remain straight,\n"
            "and the origin remains fixed.",
            font_size=24
        ).shift(DOWN * 2)

        self.play(Write(title), Write(subtitle))
        self.wait(WAIT_TIME)
        self.next_section(
            name="Definition of Linear Transformation", skip_animations=False)
        self.play(FadeIn(definition))
        self.wait(WAIT_TIME)

        # Slide 2: Visualizing Vectors and Grid
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(definition))
        self.next_section(name="Visualizing Transformation",
                          skip_animations=False)

        label = Text("Visualizing Linear Transformations",
                     font_size=36).shift(UP * 3)
        grid = NumberPlane(
            x_range=[-20, 20], y_range=[-20, 20],
            background_line_style={"stroke_opacity": 0.4}
        )

        # Initial vector
        vector_1 = Vector(2 * RIGHT + 1 * UP, color=BLUE)
        annotation_1 = MathTex(
            r"\vec{v}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}").next_to(vector_1.get_end())

        # Target vector after transformation
        vector_2 = Vector(3 * RIGHT + 1 * UP, color=GREEN)
        annotation_2 = MathTex(
            r"\vec{v}_2 = \begin{bmatrix} 3 \\ 1 \end{bmatrix}").next_to(vector_2.get_end())

        self.play(FadeIn(grid), GrowArrow(vector_1), Write(annotation_1))
        self.wait(WAIT_TIME)

        # Slide 3: Display Shear Transformation Matrix
        self.next_section(name="Shear Transformation Matrix",
                          skip_animations=False)

        # Define shear transformation matrix
        shear_matrix = [[1, 1], [0, 1]]
        matrix_tex = MathTex(
            r"\text{Shear Matrix: } \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}"
        ).to_corner(UL)

        self.play(Write(matrix_tex))
        self.wait(WAIT_TIME)

        # Slide 4: Apply Shear Transformation
        self.next_section(name="Applying Shear Transformation",
                          skip_animations=False)

        self.play(
            ReplacementTransform(vector_1, vector_2),
            ReplacementTransform(annotation_1, annotation_2),
            grid.animate.apply_matrix(shear_matrix)
        )
        self.wait(WAIT_TIME)

        conclusion = Text(
            "The shear matrix maps the first vector to the second", font_size=28).shift(DOWN * 2)

        self.next_section(name="Conclusion", skip_animations=False)
        self.play(Write(conclusion))

        # Slide 4: Display Rotation Matrix
        self.next_section(name="Rotation Matrix", skip_animations=False)
        self.play(FadeOut(grid), FadeOut(vector_2), FadeOut(
            annotation_2), FadeOut(matrix_tex), FadeOut(conclusion))
        self.wait(WAIT_TIME)

        grid = NumberPlane(
            x_range=[-20, 20], y_range=[-20, 20],
            background_line_style={"stroke_opacity": 0.4}
        )

        # Initial vector
        vector_1 = Vector(2 * RIGHT + 1 * UP, color=BLUE)
        annotation_1 = MathTex(
            r"\vec{v}_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}").next_to(vector_1.get_end())

        # Target vector after transformation
        vector_2 = Vector(-1 * RIGHT + 2 * UP, color=GREEN)
        annotation_2 = MathTex(
            r"\vec{v}_2 = \begin{bmatrix} -1 \\ 2 \end{bmatrix}").next_to(vector_2.get_end())

        self.play(FadeIn(grid), GrowArrow(vector_1), Write(annotation_1))
        self.wait(WAIT_TIME)

        # Define rotation transformation matrix
        rotation_matrix = [[0, -1], [1, 0]]  # 90 degrees counterclockwise
        matrix_tex = MathTex(
            r"\text{Rotation Matrix: } \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}"
        ).to_corner(UL)

        self.play(Write(matrix_tex))
        self.wait(WAIT_TIME)

        # Slide 5: Apply Rotation Transformation
        self.next_section(
            name="Applying Rotation Transformation", skip_animations=False)

        self.play(
            ReplacementTransform(vector_1, vector_2),
            ReplacementTransform(annotation_1, annotation_2),
            grid.animate.apply_matrix(rotation_matrix)
        )
        self.wait(WAIT_TIME)

        # Slide 6: Conclusion
        conclusion = Text(
            "The rotation matrix rotates the first vector to the second", font_size=28
        ).shift(DOWN * 2)

        self.next_section(name="Conclusion", skip_animations=False)
        self.play(Write(conclusion))
        self.wait(WAIT_TIME)
