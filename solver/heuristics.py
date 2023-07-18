import numpy as np 
from instances   import * 
from utils       import *
from performance import *
import math

def hamming_heuristic(state, goal):
    """
    misplaced tiles heuristic
    """
    misplaced_tiles          = 0 
    for y , row in enumerate(state) :
        for x , tile in enumerate(row) :
            if goal[y][x] != tile :  
                misplaced_tiles += 1

    return misplaced_tiles


def gaschnig_heuristic(state, goal):

    misplaced_tiles          = 0
    shape_y, shape_x = shape(state)

    for y in range(shape_y):
        for x in range(shape_x):
            if goal[y][x] != state[y][x] :  
                blank_y , blank_x = where(state ,  shape_x * shape_y)
                state = swap(state , (blank_x,blank_y) , (x,y))
                misplaced_tiles +=1
                if state ==  goal:
                    return misplaced_tiles

    return misplaced_tiles

# @timeit
def manhattan_heuristic(initial_state , final_state):
    """
    a generalized sum of manhattan distances for each tile given an initial 
    state and final state, which does not need to be the ordered one 
    """
    sum_of_manhattan_distances = 0 
    shape_y, shape_x = shape(initial_state)
    for y in range(shape_y):
        for x in range(shape_x):
            tile = initial_state[y][x]
            if tile == final_state[y][x]:
                continue
            y_final , x_final = (tile//shape_x) , tile%shape_x -1
            if tile%shape_x  == 0 : 
                y_final = tile//shape_x -1
            if tile//shape_x - tile/shape_x == 0 : 
                x_final = shape_x - 1
            # print(  tile , y_final, x_final)
            sum_of_manhattan_distances += (abs(x_final - x) + abs(y_final - y))

    return sum_of_manhattan_distances


def linear_conflict_heuristic(initial_state , final_state):
    """
    manhattan distance with linear conflict correction 
    """
    raise NotImplementedError()

def walking_distance_heuristic(initial_state, final_state):
    raise NotImplementedError()

def inversion_distance_heuristic(initial_state, final_state):
    raise NotImplementedError()


def compute_heuristic(initial_state, final_state , method):

    methods = { "hamming distance"   : hamming_heuristic,
                "gaschnig heuristic" : gaschnig_heuristic , 
                "manhattan distance" : manhattan_heuristic , 
                "linear conflict"    : linear_conflict_heuristic,
                "walking distance"   : walking_distance_heuristic , 
                "inversion distance" : inversion_distance_heuristic}


    return methods[method](initial_state , final_state)

    

