from collections import deque
from heuristics  import compute_heuristic
from utils       import *
from performance import * 
from functools   import lru_cache 
import time
import json 

func_time = 0
neighbours_table = {}

def dynamic_weighting_function():
    # naive implementation for now
    return 81 , 19 

def equals_from_move(state_1 , state_2, move):
    blank_y , blank_x = where(state_1, shape(state_1)[0]*shape(state_1)[1])
    modified_state    = swap(state_1 , (blank_y,blank_x), move)
    return modified_state == state_2

def get_neighbour_configurations(state):
    global func_time, neighbours_table
    s = time.time()
    key = state_to_string(state)
    if key in neighbours_table:
        return neighbours_table[key]
    blank_y , blank_x = get_blank_coordinates(state) 
    neighbours = []
    for tile_y, tile_x in get_blank_neighbours(state) :
        neighbours.append(((tile_y, tile_x) , 
                            swap(state , (tile_y,tile_x), (blank_y,blank_x))))
    
    neighbours_table[key] =  neighbours
    func_time += (time.time()-s)
    return neighbours

def contains(path, node):
    for _, state in path : 
        if state == node :
            return True
    return False

def search(path,expanded_nodes, goal, g, bound, heuristic_method, weighted):

    W_h, W_g = 1 , 1
    expanded_nodes[0] += 1 
    state = path[0][1]
    if weighted :
        W_h,W_g = dynamic_weighting_function()
        
    f = W_g*g + W_h*compute_heuristic(state, goal, heuristic_method)

    if f > bound : 
        return "NOT YET", f

    if state == goal :
        return "FOUND" , bound

    min_f = float('inf')
    for tile , neighbour in get_neighbour_configurations(state) :
        if not contains(path,neighbour):
            path.appendleft((tile, neighbour))
            temp = search(path,expanded_nodes, goal, g+1, bound, heuristic_method, weighted)
            if temp[0] == "FOUND": 
                return "FOUND" , bound 

            if temp[0] == "NOT YET" and temp[1] < min_f:
                min_f = temp[1] 
            path.popleft()

    return "NOT YET", min_f

@timeit
def iterative_deepening_algorithm(start , goal , heuristic_method, weighted=False):

    path = deque([(get_blank_coordinates(start) , start)])
    bound = compute_heuristic(start, goal, heuristic_method)
    expanded_nodes = deque([0]) # get use of call by reference 
    while True:
        status, limit =  search(path,expanded_nodes, goal, 0, bound, heuristic_method, weighted)
        if status == "FOUND" :
            moves = list(zip(*path))[0][::-1]          # (y,x)
            print(" Neighbours function time", func_time)
            return  {"moves" : moves , "depth": len(moves)-1  , "expanded nodes": expanded_nodes[0]}
        elif limit == float('inf'):
            return "NO SOLUTION"
        bound = limit


