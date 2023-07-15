from utils import * 

PARITY = {  0: "EVEN" ,  1: "ODD"  }

def get_transpositions_parity(initial_state , final_state): 

    number_of_transpositions =  0 
    
    while initial_state != final_state : 
        for i in range(len(initial_state)) :
            for j in range(len(initial_state[0])):
                if initial_state[i][j] == final_state[i][j]:
                    continue
                initial_state = swap(initial_state , (i,j), where(final_state, initial_state[i][j]))
                # pretty_print(initial_state)
                number_of_transpositions += 1
                if  initial_state == final_state : 
                    
                    return PARITY[int(number_of_transpositions) % 2]
    
def get_blank_square_parity(initial_state , final_state):

    blank_initial_y , blank_initial_x = get_blank_coordinates(initial_state)
    blank_final_y   , blank_final_x   = get_blank_coordinates(final_state)
    blank_manhattan_distance = (abs(blank_final_x - blank_initial_x) + 
                                abs(blank_final_y - blank_initial_y))
    print("b" , blank_manhattan_distance)
    blank_parity = PARITY[blank_manhattan_distance % 2]
    return blank_parity 


def is_solvable(initial_state , final_state):

    blank_parity = get_blank_square_parity(initial_state , final_state)
    transpositions_parity = get_transpositions_parity(initial_state , final_state)
    return blank_parity == transpositions_parity


