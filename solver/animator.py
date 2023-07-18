from manim import * 
from utils import shape , generate_default_goal
from instances import convert_coordinates_to_directions

config["frame_height"] = 2
config["frame_width"] = 3

SQUARE_LEN = .3 
scale_factor = 1.2

class Animation(Scene):

    def box(self , arr):
        grid =  VGroup()
        coords_top =  [2*SQUARE_LEN ,SQUARE_LEN,0, -SQUARE_LEN]
        coords_right = [2*SQUARE_LEN*1.1 ,SQUARE_LEN*1.2,0, -SQUARE_LEN*.95]
        for i , row in enumerate(arr):
            line = VGroup()
            for j,entry in enumerate(row): 
                color = RED
                if entry == len(arr) * len(arr[0]) :
                    line.add(VGroup())
                    continue
                if entry % 2 ==0 :
                    color = BLUE
                square = Square(stroke_color = color ,
                         side_length=SQUARE_LEN).shift(DOWN*SQUARE_LEN*i*1.15 + RIGHT*j*SQUARE_LEN*1.15)
                # print(square.get_center())
                # print(RIGHT)
                square.set_fill(color,opacity=1)
                text = Tex(str(entry)).move_to(square.get_center()).scale(.4)
                line.add(VGroup(square, text))
            grid.add(line)
        return grid  
    
    def move_tile_a_unit(self, tile ,direction):

        TILE_LEN = tile[0].side_length *1.15
        x, y,_ =  tile.get_center()
        MOVES = {"UP"   : [x , y+TILE_LEN,0],
                 "DOWN" : [x , y-TILE_LEN,0],
                 "RIGHT": [x +TILE_LEN, y,0] ,
                 "LEFT" : [x -TILE_LEN, y,0] }

        return tile.animate.move_to(MOVES[direction])

    def construct(self):
        start =        [[15 , 16  ,14 , 13],
                        [1   ,3  , 2  , 4],
                        [7  , 8  , 6  , 5],
                        [11  ,9 ,  10 , 12]]

        grid = self.box(start)
        moves = iterative_deepening_algorithm(start , 
                            generate_default_goal(shape(start)) , "manhattan distance")["moves"]
        self.add(grid.shift(UP*.5+ LEFT*.4))
        directions = convert_coordinates_to_directions(moves)
        directions.insert(0,1)
        for i in range(1, len(moves)):
            past = moves[i-1]
            coord = moves[i]
            direction = directions[i]
            tile = grid[coord[0]][coord[1]]

            self.play(self.move_tile_a_unit(tile, direction), run_time=.3)

            grid[past[0]][past[1]] , grid[coord[0]][coord[1]] =  \
            grid[coord[0]][coord[1]] , grid[past[0]][past[1]] 
            
