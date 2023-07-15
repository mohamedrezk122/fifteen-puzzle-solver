import pyglet
import math
from pyglet import shapes
import time
WIDTH= 600
HEIGHT= 600
TILE_WIDTH = 50
TILE_HEIGHT = 50 
TILE_COLOR = (255, 97, 97)
BORDER_COLOR = (0 , 0 ,0 )

window = pyglet.window.Window(WIDTH, HEIGHT)
batch = pyglet.graphics.Batch()

class Tile:
    def __init__(self, x,y,number, batch):
        self.x = x 
        self.y = y 
        self.tile = shapes.Rectangle(self.x, self.y, TILE_WIDTH, 
                            TILE_HEIGHT, color=TILE_COLOR, batch= batch)

        self.label = pyglet.text.Label( str(number),
                          font_name='Times New Roman', font_size=20,
                          x=self.x+ 0.5* TILE_WIDTH, y=self.y+ 0.5* TILE_HEIGHT,
                          anchor_x='center', anchor_y='center', batch=batch)
        self.last_x = 0 
        self.last_y = 0 
        self.is_moving = True

    def move_a_unit(self,direction):
        MOVES = {"UP"   : (self.x , self.y+TILE_HEIGHT),
                 "DOWN" : (self.x , self.y-TILE_HEIGHT) ,
                 "RIGHT": (self.x +TILE_WIDTH, self.y)  ,
                 "LEFT" : (self.x-TILE_WIDTH, self.y)  }

        move_x, move_y = MOVES[direction]

        step_size = 30
        step_x = (move_x - self.x) / step_size
        step_y = (move_y - self.y) / step_size

        # if self.is_moving:

        distance_x = move_x - self.x 
        distance_y = move_y - self.y
        # Check if the shape has reached the target position
        # if abs(distance_x) <= abs(step_x) and abs(distance_y) <= abs(step_y):
        if (tile.x == move_x) and (tile.y == move_y):
            self.x = move_x 
            self.y = move_y
            self.is_moving = False
            print("Shape has reached the target position. Movement stopped.")
        else:
            # Move the shape towards the target position
            if abs(distance_x) > abs(step_x):
                # self.x += step_x
                self.tile.x += step_x
                self.label.x += step_x
            if abs(distance_y) > abs(step_y):
                # self.y += step_y
                self.tile.y += step_y
                self.label.y += step_y

    def draw(self):
        self.tile.draw()
        self.label.draw()

    @staticmethod
    def distance(pt1, pt2):
        return math.sqrt((pt1[0]-pt2[0])**2 +  (pt1[1]-pt2[1])**2)


tile = Tile(200, 200, 12, batch)


@window.event
def on_draw():
    window.clear()
    # tile.move_a_unit("UP")
    # time.sleep(.2)
    # tile.move_a_unit("DOWN")
    
    batch.draw()

def update(dt):
    # tile.move_a_unit("UP")
    # time.sleep(.5)
    tile.move_a_unit("RIGHT")
    # tile.is_moving = True
    # tile.move_a_unit("RIGHT")
    
pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()