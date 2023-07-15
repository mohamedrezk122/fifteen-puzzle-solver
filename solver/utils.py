import copy


def pretty_print(state):
    for row in state: 
        for element in row :
            if len(str(element)) == 1: 
                print(element,"  ", end="")
            else:
                print(element," ", end="")
        print()
    print("-"*15)


def shape(state):

    tst = state 
    shape = []
    while type(tst) in [list, tuple]:
        shape.append(len(tst))
        tst = tst[0]

    return tuple(shape)

def swap(state , pt1 , pt2):   
    if type(state) == tuple : 
        state = [[y for y in x] for x in state]
    test_state =  copy.deepcopy(state)
    size = len(shape(state))
    if  size == 2 :
        tmp = test_state[pt1[0]][pt1[1]]
        test_state[pt1[0]][pt1[1]] = test_state[pt2[0]][pt2[1]]
        test_state[pt2[0]][pt2[1]] = tmp 
    elif size == 1 :
        state[pt2], state[pt1] = state[pt1] , state[pt2]
    return test_state


def where(state , tile):
    for y, row in enumerate(state): 
        for x, element in enumerate(row) :
            if element == tile :
                return y,x


def transpose(state):
    transposed = copy.deepcopy(state)
    for y, row in enumerate(state): 
        for x, element in enumerate(row) :
            transposed[y][x] =  state[x][y]
    return transposed


def flatten(state):     
    vector = []
    for row in state: 
        vector += row 
    return vector

def state_to_string(state):
    string_reper = ""
    for row in state:
        for tile in row :
            string_reper += str(tile)
            string_reper += " "
    return string_reper

def state_to_tuple(function):
    def wrapper(*args):
        args = [tuple([tuple(y) for y in x]) if type(x) == list else x for x in args]
        result = function(*args)
        result = tuple(result) if type(result) == list else result
        return result
    return wrapper

def get_tile_neighbours(coord_x , coord_y , shape_x , shape_y):
    neighbours = set()
    if coord_x - 1 >= 0 :
        neighbours.add((coord_y , coord_x-1 ))
    if coord_x + 1 < shape_x :
        neighbours.add((coord_y , coord_x+1 ))
    if coord_y - 1 >= 0 : 
        neighbours.add(( coord_y-1 , coord_x ))
    if coord_y + 1 < shape_y :
        neighbours.add((coord_y+1 , coord_x))

    return neighbours

def get_blank_coordinates(state):
    shape_y , shape_x = shape(state) 
    return where(state , shape_x * shape_y ) 

def get_blank_neighbours(state):
    shape_y , shape_x = shape(state) 
    blank_y , blank_x = get_blank_coordinates(state)
    return get_tile_neighbours(blank_x, blank_y, shape_x, shape_y)


@state_to_tuple
def test(state):
    return state
if __name__ == "__main__" :
    end_test   =        [[ 1  , 2  , 3  , 4  ],
                    [ 5  , 6  , 7  , 8  ],
                    [ 9  , 10 , 11 , 12 ],
                    [ 13 , 14 , 15 , 16 ]]

    # print(shape(end_test))
    # pretty_print(end_test)
    # print(get_blank_coordinates(end_test))
    # print(state_to_string(end_test))
    print(test(end_test))
    # flatten(end_test)
    # print(transpose(end_test))
    # print(where(end_test, 16))
    # pretty_print(swap(end_test , (3,3) , (1,1)))
    # pretty_print(end_test)