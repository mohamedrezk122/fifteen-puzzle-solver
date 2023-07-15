from instances import shuffle_puzzle ,generate_random_puzzle
from heuristics import compute_heuristic
from iterative_deepening import  iterative_deepening_algorithm 
from utils import *
from performance import * 
from check import is_solvable



start_test =        [  [ 1  , 2  , 3  , 4  ],
                    [ 5  , 16  , 6  , 8  ],
                    [ 9  , 10 , 7 , 12 ],
                    [ 13 , 14 , 11 , 15 ]]


start_test3 =       [[15 , 16  ,14 , 13],
                    [1   ,3  , 2  , 4],
                    [7  , 8  , 6  , 5],
                    [11  ,9 ,  10 , 12]]


start_test2 =       [[ 12  , 1  , 3  , 4  ],
                    [ 2  , 13  , 14  , 5  ],
                    [ 11  , 10 , 8 , 6 ],
                    [ 9 , 15 , 7 , 16 ]]

end_test   =        [[ 1  , 2  , 3  , 4  ],
                    [ 5  , 6  , 7  , 8  ],
                    [ 9  , 10 , 11 , 12 ],
                    [ 13 , 14 , 15 , 16 ]]


# pretty_print(start_test)
# print(is_solvable(start_test2 , end_test))
# print(is_solvable(start_test , end_test))
# test = shuffle_puzzle(end_test )
# pretty_print(test)
print(compute_heuristic(start_test3, end_test , "manhattan distance"))
pretty_print(start_test3)
print(iterative_deepening_algorithm(start_test3 , end_test, "manhattan distance"))
# # print(iterative_deepening_algorithm(test , end_test, "hamming distance"))
# # print(iterative_deepening_algorithm(test , end_test, "gaschnig heuristic"))