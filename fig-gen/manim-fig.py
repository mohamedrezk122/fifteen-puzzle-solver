from manim import * 
import networkx as nx 

class Scene1(Scene):

    def box(self , arr):

        group =  VGroup()
        coords = [.5,0, -.5 , -1]
        for i , row in enumerate(arr):
            for j,entry in enumerate(row): 
                color = RED
                if entry == len(arr) * len(row) :
                    color = GREY
                elif entry % 2 ==0 :
                    color = BLUE
                square = Square(stroke_color = color , side_length=.5).shift(UP*coords[i] + RIGHT*coords[::-1][j])
                square.set_fill(color,opacity=1)
                text = Tex(str(entry)).move_to(square.get_center()).scale(.6)
                group.add(square, text)

        return group 


    def construct(self): 

        arr_1 = [ [1 ,2 , 3, 4],
        [5 , 6 , 7, 8],
        [9, 10, 11, 12],
        [13 , 14 , 15, 16]]

        arr_2 = [ [1 ,2 , 3, 4],
        [5 , 6 , 7, 8],
        [9, 10, 11, 12],
        [13 , 15 , 14, 16]]

        arrow = Arrow(start=1 * LEFT, end=.75 * RIGHT, 
                max_stroke_width_to_length_ratio=3.5,
                max_tip_length_to_length_ratio=.2).shift(DOWN*.25).set_color(GREY)

        mark = Tex("??").next_to(arrow, UP*.75).set_color(GREY)

        box_1 = self.box(arr_1).shift(LEFT*-2.5).scale(1.2)
        box_2 = self.box(arr_2).shift(LEFT*2.5).scale(1.2)
        self.add(box_1 , box_2 , arrow, mark)


class Tree(Scene):

    def box(self , arr):

        group =  VGroup()
        coords = [.5,0, -.5 , -1]
        for i , row in enumerate(arr):
            for j,entry in enumerate(row): 
                color = RED
                if entry == len(arr) * len(row) :
                    color = GREY
                elif entry % 2 ==0 :
                    color = BLUE
                square = Square(stroke_color = color , side_length=.5).shift(UP*coords[i] + RIGHT*coords[::-1][j])
                square.set_fill(color,opacity=1)
                text = Tex(str(entry)).move_to(square.get_center()).scale(.6)
                group.add(square, text)

        return group 




    def construct(self): 

        arr_1 = [   [1 ,2 , 3],
                    [4, 9 , 6],
                    [7, 8,  5]]

        arr_2 = [   [1 ,2 , 3],
                    [9, 4 , 6],
                    [7, 8,  5]]

        arr_3 = [   [1 ,2 , 3],
                    [4, 6 , 9],
                    [7, 8,  5]]

        arr_4 = [   [1 ,9 , 3],
                    [4, 2 , 6],
                    [7, 8,  5]]

        arr_5 = [   [1 ,2 , 3],
                    [4, 8 , 6],
                    [7, 9,  5]]


        box_1 = self.box(arr_1).shift(UP*1+LEFT*-.2).scale(.6)
        box_2 = self.box(arr_2).shift(DOWN + LEFT*-2.5).scale(.6)
        box_3 = self.box(arr_3).shift(DOWN + LEFT*-1).scale(.6)
        box_4 = self.box(arr_4).shift(DOWN + LEFT*0.5).scale(.6)
        box_5 = self.box(arr_5).shift(DOWN + LEFT*2).scale(.6)

        group = VGroup(Line(box_1.get_center(), box_2.get_center() , color= GREY) ,
                        Line(box_1.get_center(), box_3.get_center(), color= GREY) ,
                        Line(box_1.get_center(), box_4.get_center(), color= GREY) ,
                        Line(box_1.get_center(), box_5.get_center(), color= GREY)  )

        self.add(group, box_1 , box_2 , box_3, box_4 , box_5)