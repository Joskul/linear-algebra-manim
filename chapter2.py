from manim import *

WAIT_TIME = 0.5


class IntroToLinearTransformation(Scene):
    def construct(self):

        # Slide 1: Title and Definition
        title = Text("Intro to Linear Transformation", font_size=48)
        subtitle = Text("Definition of Linear Transformations",
                        font_size=36).next_to(title, DOWN)
        definition = Text(
            "Linear transformations map vectors to other vectors\n"
            "while preserving properties: \n1. Lines remain straight,\n"
            "2. The origin remains fixed.",
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


class VisualizingTransformationsWithExternalImage(Scene):
    def construct(self):

        # Slide 1: Title and Intro
        title = Text(
            "Visualizing Transformations", font_size=48)
        intro = Text(
            "We can visualize transformations by observing their effect on a grid",
            font_size=24
        ).shift(DOWN * 2)

        self.play(Write(title))
        self.wait(WAIT_TIME)
        self.next_section(name="Introduction", skip_animations=False)
        self.play(Write(intro))
        self.wait(WAIT_TIME)

        # Slide 2: Grid and Image Setup
        grid = NumberPlane(
            x_range=[-20, 20], y_range=[-20, 20],
            background_line_style={"stroke_opacity": 0.4}
        )

        # Basis vectors
        i_hat = Vector(RIGHT, color=RED)
        j_hat = Vector(UP, color=BLUE)
        i_hat_label = MathTex(r"\hat{i}", color=RED).next_to(
            i_hat.get_end(), DOWN)
        j_hat_label = MathTex(r"\hat{j}", color=BLUE).next_to(
            j_hat.get_end(), LEFT)

        # External image as a sample object (assuming 'house.png' is in the working directory)
        shape_1 = Triangle().scale(0.5).set_color(YELLOW).shift(UP + RIGHT)
        shape_2 = Cube().scale(0.2).set_color(BLUE).shift(DOWN * 3 + RIGHT * 1.6)
        shape_3 = Square().scale(0.4).set_color(GREEN).shift(DOWN * 2.5 + LEFT * 1.2)
        shape_4 = Circle().scale(0.7).set_color(ORANGE).shift(UP * 2.8 + LEFT * 3)

        shape_group = VGroup(shape_1, shape_2, shape_3, shape_4)

        # Initial Display: Grid, Vectors, and Image
        self.play(FadeOut(title), FadeOut(intro))
        self.next_section(name="Grid and Image Setup", skip_animations=False)
        self.play(FadeIn(grid), GrowArrow(i_hat), GrowArrow(j_hat),
                  Write(i_hat_label), Write(j_hat_label), FadeIn(shape_group))
        self.wait(WAIT_TIME)

        # Slide 3: Applying Transformation

        # Shear matrix for transformation
        shear_matrix = [[1, 1], [0, 1]]

        # Define individual matrix elements with color
        shear_matrix_element_11 = MathTex(str(shear_matrix[0][0]), color=RED)
        shear_matrix_element_12 = MathTex(str(shear_matrix[0][1]), color=BLUE)
        shear_matrix_element_21 = MathTex(str(shear_matrix[1][0]), color=RED)
        shear_matrix_element_22 = MathTex(str(shear_matrix[1][1]), color=BLUE)

        # Arrange matrix elements in a grid structure to form a matrix
        shear_matrix_group = VGroup(
            MathTex("[").scale(3.0),
            VGroup(shear_matrix_element_11, shear_matrix_element_21).arrange(
                DOWN, buff=0.5),
            VGroup(shear_matrix_element_12, shear_matrix_element_22).arrange(
                DOWN, buff=0.5),
            MathTex("]").scale(3.0),
        ).arrange(RIGHT, buff=0.5).to_corner(UL)

        self.play(Write(shear_matrix_group))
        self.wait(WAIT_TIME)

        # Transform the grid, basis vectors, and image
        self.next_section(name="Applying Transformation",
                          skip_animations=False)
        self.play(
            ApplyMatrix(shear_matrix, shape_group),
            ApplyMatrix(shear_matrix, grid),
            ApplyMatrix(shear_matrix, i_hat),
            ApplyMatrix(shear_matrix, j_hat),
            i_hat_label.animate.move_to(i_hat.get_end() + DOWN * 0.3),
            j_hat_label.animate.move_to(j_hat.get_end() + LEFT * 0.3),
        )
        self.wait(WAIT_TIME)

        # Slide 4: Explanation
        explanation = Text(
            "The shear transformation modifies the entire grid, basis vectors, and image.",
            font_size=24
        ).shift(DOWN * 2)

        self.next_section(name="Transformation Explanation",
                          skip_animations=False)
        self.play(Write(explanation))
        self.wait(WAIT_TIME)

        self.next_section(name="More Transformations", skip_animations=False)
        self.play(FadeOut(explanation))

        rotation_matrix = [[0.7071, -0.7071], [0.7071, 0.7071]]

        rotation_matrix_element_11 = MathTex(
            r"\cos{\theta}", color=RED)
        rotation_matrix_element_12 = MathTex(
            r"\sin{\theta}", color=BLUE)
        rotation_matrix_element_21 = MathTex(
            r"-\sin{\theta}", color=RED)
        rotation_matrix_element_22 = MathTex(
            r"\cos{\theta}", color=BLUE)

        rotation_matrix_group = VGroup(
            MathTex("[").scale(3.0),
            VGroup(rotation_matrix_element_11, rotation_matrix_element_21).arrange(
                DOWN, buff=0.5),
            VGroup(rotation_matrix_element_12, rotation_matrix_element_22).arrange(
                DOWN, buff=0.5),
            MathTex("]").scale(3.0),
        ).arrange(RIGHT, buff=0.5).to_corner(UL)

        self.play(Write(rotation_matrix_group),
                  shear_matrix_group.animate.next_to(
                      rotation_matrix_group, RIGHT),
                  )
        self.wait(WAIT_TIME)

        self.next_section(name="Applying Rotation Transformation",
                          skip_animations=False)
        self.play(
            ApplyMatrix(rotation_matrix, shape_group),
            ApplyMatrix(rotation_matrix, grid),
            ApplyMatrix(rotation_matrix, i_hat),
            ApplyMatrix(rotation_matrix, j_hat),
            i_hat_label.animate.move_to(j_hat.get_end() + LEFT * 0.3),
            i_hat_label.animate.move_to(i_hat.get_end() + DOWN * 0.3),
        )
        self.wait(WAIT_TIME)

        # Slide 6: Conclusion
        conclusion = Text(
            "Multiple transformations can be applied",
            font_size=24
        ).to_edge(DOWN)

        self.next_section(name="Conclusion", skip_animations=False)
        self.play(Write(conclusion))
        self.wait(WAIT_TIME)
        self.play(
            FadeOut(grid), FadeOut(i_hat), FadeOut(
                j_hat), FadeOut(i_hat_label), FadeOut(j_hat_label),
            FadeOut(shear_matrix_group), FadeOut(
                conclusion), FadeOut(shape_group),
            FadeOut(rotation_matrix_group),
        )


class PropertiesOfLinearTransformations(MovingCameraScene):
    def construct(self):

        # Title
        title = Text("Properties of Linear Transformations",
                     font_size=40).to_edge(UP)
        self.play(Write(title))

        # Section 1: Fixed Origin (0,0)
        section1_text = Text(
            "1. Linear Transformations have a fixed origin (0,0)", font_size=30)
        section1_text.next_to(title, DOWN)

        self.play(Write(section1_text))

        # Setup grid and basis vectors
        grid = NumberPlane(
            x_range=[-30, 30], y_range=[-30, 30],
            background_line_style={"stroke_opacity": 0.4}
        )
        i_hat = Vector(RIGHT, color=RED)
        j_hat = Vector(UP, color=BLUE)
        i_hat_label = MathTex(r"\hat{i}", color=RED).next_to(
            i_hat.get_end(), DOWN)
        j_hat_label = MathTex(r"\hat{j}", color=BLUE).next_to(
            j_hat.get_end(), LEFT)

        # Initial Display
        self.play(FadeIn(grid), GrowArrow(i_hat), GrowArrow(
            j_hat), Write(i_hat_label), Write(j_hat_label))
        self.next_section(name="Fixed Origin", skip_animations=False)
        self.wait(WAIT_TIME)

        # Zoom in on the origin
        self.play(self.camera.frame.animate.set_width(3))
        self.next_section(name="Fixed Origin", skip_animations=False)
        self.wait(WAIT_TIME)

        # Apply a linear transformation
        shear_matrix_1 = [[1, 1], [0, 1]]
        self.play(
            ApplyMatrix(shear_matrix_1, grid),
            ApplyMatrix(shear_matrix_1, i_hat),
            ApplyMatrix(shear_matrix_1, j_hat),
            i_hat_label.animate.move_to(i_hat.get_end() + DOWN * 0.3),
            j_hat_label.animate.move_to(j_hat.get_end() + LEFT * 0.3),
        )
        self.next_section(name="Fixed Origin", skip_animations=False)
        self.wait(WAIT_TIME)

        # Apply another linear transformation
        shear_matrix_2 = [[1, 0], [1, 1]]
        self.play(
            ApplyMatrix(shear_matrix_2, grid),
            ApplyMatrix(shear_matrix_2, i_hat),
            ApplyMatrix(shear_matrix_2, j_hat),
            i_hat_label.animate.move_to(i_hat.get_end() + DOWN * 0.3),
            j_hat_label.animate.move_to(j_hat.get_end() + LEFT * 0.3),
        )
        self.next_section(name="Fixed Origin", skip_animations=False)
        self.wait(WAIT_TIME)

        # Zoom out to full grid
        self.play(self.camera.frame.animate.set_width(14))
        self.next_section(name="Fixed Origin", skip_animations=False)
        self.wait(WAIT_TIME)

        # Setup grid and basis vectors
        ghost_grid = grid.copy().set_opacity(0.5).set_color(GREY)

        # Show an example of non-linear transformation by shifting the grid
        self.play(grid.animate.shift(RIGHT * 2 + UP * 2),
                  i_hat.animate.shift(RIGHT * 2 + UP * 2),
                  j_hat.animate.shift(RIGHT * 2 + UP * 2),
                  j_hat_label.animate.shift(RIGHT * 2 + UP * 2),
                  i_hat_label.animate.shift(RIGHT * 2 + UP * 2),
                  )
        self.next_section(name="Fixed Origin", skip_animations=False)
        self.wait(WAIT_TIME)

        # Flash the original origin and the new origin
        origin_marker = Dot(ORIGIN, color=YELLOW)
        new_origin_marker = Dot(grid.get_center(), color=YELLOW)
        self.play(FadeIn(origin_marker), FadeIn(
            new_origin_marker), FadeIn(ghost_grid))
        self.play(Flash(origin_marker), Flash(new_origin_marker))
        self.next_section(name="Fixed Origin", skip_animations=False)
        self.wait(WAIT_TIME)

        # Show some explanations
        warn_text = Text("This is NOT a linear transformation!",
                         font_size=24).to_edge(DOWN)
        self.play(Write(warn_text))
        self.next_section(name="Fixed Origin", skip_animations=False)
        self.wait(WAIT_TIME)

        self.next_section(name="Fixed Origin", skip_animations=False)
        # Clear scene
        self.play(FadeOut(origin_marker), FadeOut(new_origin_marker), FadeOut(grid), FadeOut(i_hat), FadeOut(j_hat),
                  FadeOut(i_hat_label), FadeOut(j_hat_label), FadeOut(
                      section1_text), FadeOut(warn_text),
                  FadeOut(ghost_grid))

        # Section 2: Grid Lines Stay Straight and Parallel
        section2_text = Text(
            "2. Grid lines stay straight and parallel under linear transformations", font_size=30)
        section2_text.next_to(title, DOWN)

        self.play(Write(section2_text))

        # Reset grid and basis vectors
        grid = NumberPlane(
            x_range=[-30, 30], y_range=[-30, 30],
            background_line_style={"stroke_opacity": 0.4}
        )
        i_hat = Vector(RIGHT, color=RED)
        j_hat = Vector(UP, color=BLUE)
        i_hat_label = MathTex(r"\hat{i}", color=RED).next_to(
            i_hat.get_end(), DOWN)
        j_hat_label = MathTex(r"\hat{j}", color=BLUE).next_to(
            j_hat.get_end(), LEFT)

        # Display grid and highlight a line
        line = Line(grid.c2p(-1, -10), grid.c2p(-1, 10),
                    color=YELLOW, stroke_width=4)
        self.play(FadeIn(grid), GrowArrow(i_hat), GrowArrow(j_hat),
                  Write(i_hat_label), Write(j_hat_label), Create(line))
        self.next_section(name="Non-Linear Transformation",
                          skip_animations=False)
        self.wait(WAIT_TIME)

        # Apply a linear transformation to demonstrate lines remain straight and parallel
        shear_matrix_3 = [[1, 2], [0, 1]]
        self.play(
            ApplyMatrix(shear_matrix_3, grid),
            ApplyMatrix(shear_matrix_3, i_hat),
            ApplyMatrix(shear_matrix_3, j_hat),
            ApplyMatrix(shear_matrix_3, line),
            i_hat_label.animate.move_to(i_hat.get_end() + DOWN * 0.3),
            j_hat_label.animate.move_to(j_hat.get_end() + LEFT * 0.3),
        )
        self.wait(WAIT_TIME)

        self.next_section(name="Non-Linear Transformation",
                          skip_animations=False)

        # Apply a non-linear transformation and show lines no longer remain straight
        self.play(grid.animate.apply_function(
            lambda p: p + np.array([0.1 * p[1] ** 2, 0, 0])),
            i_hat.animate.apply_function(
                lambda p: p + np.array([0.1 * p[1] ** 2, 0, 0])),
            j_hat.animate.apply_function(
                lambda p: p + np.array([0.1 * p[1] ** 2, 0, 0])),
            line.animate.apply_function(
                lambda p: p + np.array([0.1 * p[1] ** 2, 0, 0])),
            Write(warn_text)
        )
        self.wait(WAIT_TIME)

        # Highlight the non-linear line
        self.play(line.animate.set_color(ORANGE))
        self.next_section(name="Non-Linear Transformation",
                          skip_animations=False)
        self.wait(WAIT_TIME)

        # Conclusion
        conclusion_text = Text(
            "Linear transformations preserve the origin\nand keep lines straight and parallel.", font_size=30)
        conclusion_text.to_edge(DOWN)
        self.play(Write(conclusion_text), warn_text.animate.shift(UP))
        self.next_section(name="Conclusion", skip_animations=False)
        self.wait(WAIT_TIME)

        # Clear scene
        self.play(FadeOut(grid), FadeOut(i_hat), FadeOut(j_hat), FadeOut(i_hat_label), FadeOut(j_hat_label), FadeOut(line),
                  FadeOut(conclusion_text), FadeOut(title), FadeOut(section2_text), FadeOut(warn_text))


class MatrixRepresentationOfTransformations(Scene):
    def construct(self):

        # Title
        title = Text("Matrix Representation of Transformations",
                     font_size=40).to_edge(UP)
        self.play(Write(title))
        self.next_section()  # Transition after title animation

        # Introduction Text
        intro_text = Text(
            "A linear transformation in two dimensions can be fully represented by a 2x2 matrix.\n"
            "The columns indicate where the basis vectors land after transformation.",
            font_size=20
        ).next_to(title, DOWN)
        self.play(Write(intro_text))
        self.next_section()  # Transition after intro text
        self.play(FadeOut(intro_text), FadeOut(title))

        # Setup grid and basis vectors
        grid = NumberPlane(
            x_range=[-10, 10], y_range=[-10, 10],
            background_line_style={"stroke_opacity": 0.4}
        )
        i_hat = Vector(RIGHT, color=RED)
        j_hat = Vector(UP, color=BLUE)
        i_hat_label = MathTex(r"\hat{i}", color=RED).next_to(
            i_hat.get_end(), DOWN)
        j_hat_label = MathTex(r"\hat{j}", color=BLUE).next_to(
            j_hat.get_end(), LEFT)

        # Display the grid and basis vectors
        self.play(FadeIn(grid), GrowArrow(i_hat), GrowArrow(
            j_hat), Write(i_hat_label), Write(j_hat_label))
        self.next_section()  # Transition after displaying grid and basis vectors

        # Define a transformation matrix
        transformation_matrix = [[2, 1], [1, 1]]

        # Show the transformation matrix with colored elements
        matrix_label = MathTex(r"\text{Transformation Matrix: }").to_corner(UL)
        self.play(Write(matrix_label))

        # Define individual matrix elements with colors for visual clarity
        matrix_element_11 = MathTex(
            str(transformation_matrix[0][0]), color=RED)
        matrix_element_12 = MathTex(
            str(transformation_matrix[0][1]), color=BLUE)
        matrix_element_21 = MathTex(
            str(transformation_matrix[1][0]), color=RED)
        matrix_element_22 = MathTex(
            str(transformation_matrix[1][1]), color=BLUE)

        # Arrange the matrix elements in grid structure to form the matrix
        matrix_group = VGroup(
            MathTex("[").scale(2.0),
            VGroup(matrix_element_11, matrix_element_21).arrange(
                DOWN, buff=0.3),
            VGroup(matrix_element_12, matrix_element_22).arrange(
                DOWN, buff=0.3),
            MathTex("]").scale(2.0),
        ).arrange(RIGHT, buff=0.5).next_to(matrix_label, RIGHT)

        self.play(Write(matrix_group))
        self.next_section()  # Transition after showing matrix representation

        # Apply the matrix transformation to the grid and basis vectors
        self.play(
            ApplyMatrix(transformation_matrix, grid),
            ApplyMatrix(transformation_matrix, i_hat),
            ApplyMatrix(transformation_matrix, j_hat),
            i_hat_label.animate.move_to(i_hat.get_end() + DOWN * 0.3),
            j_hat_label.animate.move_to(j_hat.get_end() + LEFT * 0.3),
        )
        self.next_section()  # Transition after applying matrix transformation

        # Clear scene with final message
        final_text = Text(
            "Matrix-vector multiplication allows us\nto calculate transformed coordinates easily.", font_size=30)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(WAIT_TIME)
        self.next_section()  # Transition after final message

        # Apply another matrix transformation to the grid and basis vectors
        transformation_matrix_2 = [[0, 1], [1, 0]]
        # Define individual matrix elements with colors for visual clarity
        t2_matrix_element_11 = MathTex(
            str(transformation_matrix_2[0][0]), color=RED)
        t2_matrix_element_12 = MathTex(
            str(transformation_matrix_2[0][1]), color=BLUE)
        t2_matrix_element_21 = MathTex(
            str(transformation_matrix_2[1][0]), color=RED)
        t2_matrix_element_22 = MathTex(
            str(transformation_matrix_2[1][1]), color=BLUE)

        # Arrange the matrix elements in grid structure to form the matrix
        t2_matrix_group = VGroup(
            MathTex("[").scale(2.0),
            VGroup(t2_matrix_element_11, t2_matrix_element_21).arrange(
                DOWN, buff=0.3),
            VGroup(t2_matrix_element_12, t2_matrix_element_22).arrange(
                DOWN, buff=0.3),
            MathTex("]").scale(2.0),
        ).arrange(RIGHT, buff=0.5).next_to(matrix_label, RIGHT)

        self.play(Write(t2_matrix_group),
                  matrix_group.animate.next_to(t2_matrix_group, RIGHT))
        self.next_section()  # Transition after showing matrix representation

        self.play(
            ApplyMatrix(transformation_matrix_2, grid),
            ApplyMatrix(transformation_matrix_2, i_hat),
            ApplyMatrix(transformation_matrix_2, j_hat),
            i_hat_label.animate.move_to(i_hat.get_end() + DOWN * 0.3),
            j_hat_label.animate.move_to(j_hat.get_end() + LEFT * 0.3),
        )
        self.next_section()  # Transition after applying second matrix transformation

        # Fade out all elements
        self.play(FadeOut(grid), FadeOut(i_hat), FadeOut(j_hat), FadeOut(i_hat_label), FadeOut(j_hat_label),
                  FadeOut(matrix_label), FadeOut(matrix_group), FadeOut(final_text), FadeOut(t2_matrix_group))


class MatrixRepresentationOfTransformations3D(ThreeDScene):
    def construct(self):
        WAIT_TIME = 1.5  # Adjust wait time as needed

        # Title
        title = Text("Matrix Representation of Transformations in 3D",
                     font_size=40).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.next_section()  # Transition after title animation

        # Introduction Text
        intro_text = Text(
            "A linear transformation in three dimensions can be fully represented by a 3x3 matrix.\n"
            "The columns indicate where the basis vectors land after transformation.",
            font_size=20
        ).next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(intro_text)
        self.play(Write(intro_text))
        self.next_section()  # Transition after intro text
        self.play(FadeOut(intro_text), FadeOut(title))

        # Set up 3D axes and basis vectors
        axes = ThreeDAxes(
            x_range=[-10, 10], y_range=[-10, 10], z_range=[-10, 10]
        )

        # Create a grid with smaller intervals for visual effect
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={"stroke_opacity": 0.2}
        ).set_opacity(0.3)
        grid_3d = VGroup(axes, grid)

        # Basis vectors in 3D
        i_hat = Vector([1, 0, 0], color=RED).set_opacity(0.8)
        j_hat = Vector([0, 1, 0], color=BLUE).set_opacity(0.8)
        k_hat = Vector([0, 0, 1], color=GREEN).set_opacity(0.8)
        i_hat_label = MathTex(r"\hat{i}", color=RED).next_to(
            i_hat.get_end(), DOWN)
        j_hat_label = MathTex(r"\hat{j}", color=BLUE).next_to(
            j_hat.get_end(), LEFT)
        k_hat_label = MathTex(r"\hat{k}", color=GREEN).next_to(
            k_hat.get_end(), RIGHT)

        # Add axes, grid, and basis vectors
        self.play(FadeIn(grid_3d), GrowArrow(i_hat), GrowArrow(j_hat), GrowArrow(k_hat),
                  Write(i_hat_label), Write(j_hat_label), Write(k_hat_label))
        self.next_section()  # Transition after displaying grid and vectors

        # Define a transformation matrix for 3D
        transformation_matrix_3d = [[1, 0.5, 0], [0.5, 1, 0], [0, 0, 1.5]]

        # Matrix Display with Colored Elements
        matrix_label = MathTex(r"\text{Transformation Matrix: }").to_corner(
            UL).shift(DOWN * 0.2)
        self.add_fixed_in_frame_mobjects(matrix_label)
        self.play(Write(matrix_label))

        # Define individual matrix elements with colors for visual clarity
        matrix_element_11 = MathTex(
            str(transformation_matrix_3d[0][0]), color=RED)
        matrix_element_12 = MathTex(
            str(transformation_matrix_3d[0][1]), color=BLUE)
        matrix_element_13 = MathTex(
            str(transformation_matrix_3d[0][2]), color=GREEN)
        matrix_element_21 = MathTex(
            str(transformation_matrix_3d[1][0]), color=RED)
        matrix_element_22 = MathTex(
            str(transformation_matrix_3d[1][1]), color=BLUE)
        matrix_element_23 = MathTex(
            str(transformation_matrix_3d[1][2]), color=GREEN)
        matrix_element_31 = MathTex(
            str(transformation_matrix_3d[2][0]), color=RED)
        matrix_element_32 = MathTex(
            str(transformation_matrix_3d[2][1]), color=BLUE)
        matrix_element_33 = MathTex(
            str(transformation_matrix_3d[2][2]), color=GREEN)

        # Arrange the matrix elements in a grid to form the matrix
        matrix_group = VGroup(
            MathTex("[").scale(3.0),
            VGroup(matrix_element_11, matrix_element_21,
                   matrix_element_31).arrange(DOWN, buff=0.3),
            VGroup(matrix_element_12, matrix_element_22,
                   matrix_element_32).arrange(DOWN, buff=0.3),
            VGroup(matrix_element_13, matrix_element_23,
                   matrix_element_33).arrange(DOWN, buff=0.3),
            MathTex("]").scale(3.0),
        ).arrange(RIGHT, buff=0.5).next_to(matrix_label, RIGHT)

        self.add_fixed_in_frame_mobjects(matrix_group)
        self.play(Write(matrix_group))
        self.next_section()  # Transition after matrix display

        # Rotate camera around before transformation
        self.move_camera(phi=75 * DEGREES, theta=30 *
                         DEGREES, zoom=1)  # Set initial view
        # Slowly rotate the camera around
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(WAIT_TIME)  # Give viewers time to observe the 3D layout

        # Apply matrix transformation to the grid, axes, and basis vectors
        self.play(
            ApplyMatrix(transformation_matrix_3d, grid_3d),
            ApplyMatrix(transformation_matrix_3d, i_hat),
            ApplyMatrix(transformation_matrix_3d, j_hat),
            ApplyMatrix(transformation_matrix_3d, k_hat),
            i_hat_label.animate.move_to(i_hat.get_end() + DOWN * 0.3),
            j_hat_label.animate.move_to(j_hat.get_end() + LEFT * 0.3),
            k_hat_label.animate.move_to(k_hat.get_end() + RIGHT * 0.3),
        )
        self.next_section()  # Transition after applying matrix transformation

        # Clear all elements and stop camera rotation
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(grid_3d), FadeOut(i_hat), FadeOut(j_hat), FadeOut(k_hat),
                  FadeOut(i_hat_label), FadeOut(
                      j_hat_label), FadeOut(k_hat_label),
                  FadeOut(matrix_label), FadeOut(matrix_group))
