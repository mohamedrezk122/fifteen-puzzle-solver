import numpy as np
from check import is_solvable
from heuristics import *
from utils   import *
import random
from check import is_solvable

def convert_coordinates_to_directions(coordinates):

    moves = []
    for i in range(1 , len(coordinates)) : 
        past  =  coordinates[i-1]
        coord =  coordinates[i]
        if coord[0] == past[0] : 
            if (coord[1] - past[1]) == 1 :
                moves.append("UP")
            else:
                moves.append("DOWN")
        elif coord[1] == past[1] :
            if (coord[0] - past[0]) == 1  : 
                moves.append("LEFT")
            else:
                moves.append("RIGHT")
    return moves 

def compute_randomness_coefficient(state):
    
    shape_y , shape_x = shape(state) 
    coeff = 0
    for y , row in enumerate(state) : 
        for x, element in enumerate(row) : 
            for neighbour in get_tile_neighbours(x, y, shape_x, shape_y) :
                coeff += abs(element - state[neighbour[0]][neighbour[1]])
    return coeff

def choose_tile_to_move(goal_state, blank_x, blank_y , tiles):

    max_coeff = 0
    tile = None
    for tile_y , tile_x in tiles :
        test_state = swap(goal_state , (blank_y,blank_x) , (tile_y,tile_x))
        coeff_value = compute_randomness_coefficient(test_state)

        if coeff_value > max_coeff : 
            max_coeff = coeff_value
            tile = (tile_y, tile_x)

    return tile

def shuffle_puzzle(goal_state):
    _state = copy.deepcopy(goal_state)
    
    while True:
        random.shuffle(_state)
        for row in _state :
            random.shuffle(row)

        # print(is_solvable(_state, goal_state))
        if is_solvable(_state, goal_state):
            break
    print(compute_randomness_coefficient(_state))
    return _state


def generate_random_puzzle(goal_state, depth):
    
    shape_y , shape_x = shape(goal_state) 
    moves_in_order = []

    for i in range(depth):
        # get blank square coordinates 
        blank_y , blank_x = get_blank_coordinates(goal_state)
        if i == 0 : 
            moves_in_order.append((blank_y,blank_x))

        tiles_to_move  = get_blank_neighbours(goal_state)
        tile_y , tile_x = choose_tile_to_move(goal_state, blank_x, blank_y , tiles_to_move)
        goal_state = swap(goal_state , (blank_y,blank_x) , (tile_y,tile_x))
        moves_in_order.append((tile_y , tile_x))

    return goal_state , moves_in_order[::-1]
