from instances import shuffle_puzzle ,generate_random_puzzle
from heuristics import compute_heuristic
from iterative_deepening import  iterative_deepening_algorithm 
from utils import *
from performance import * 
from check import is_solvable
import argparse
import sys


figlet = r"""
         _ ____                      _
        / | ___| _ __  _   _ _______| | ___
        | |___ \| '_ \| | | |_  /_  / |/ _ \
        | |___) | |_) | |_| |/ / / /| |  __/
        |_|____/| .__/ \__,_/___/___|_|\___|
                |_|

"""

def solve(start, end , heuristic_method, weighted):

    print(" start state:")
    pretty_print(start)
    print("-"*50)
    solvable = is_solvable(start, end)
    print(" Is solvable: ", solvable)
    if not solvable :
        return 

    print(" Heuristic method : ", heuristic_method)
    print("-"*50)
    print(" Heuristic value  : ", compute_heuristic(start, end, heuristic_method))
    print("-"*50)
    print(" Solving ...")
    solution = iterative_deepening_algorithm(start , end, heuristic_method, weighted)
    if weighted :
        print(" Weighted : ", weighted)
        print("-"*50)
    print(" Depth: ", solution["depth"] )
    print("-"*50)
    print(" Expanded nodes: ", solution["expanded nodes"])
    print("-"*50)
    print(" Effective branching factor : ", compute_effective_branching(solution["expanded nodes"], solution["depth"]))
    print("-"*50)
    print(" Moves : " , solution["moves"])



def main():
    try :
        from termcolor import colored
        print(colored(figlet, 'red'))
    except ImportError as ie:
        print(figlet)
    print("\tThis script is written by Mohamed Rezk.\n")
    parser = argparse.ArgumentParser(prog='pq puzzle solver')
    parser.add_argument('-f', '--filename' , type= str , help="file containing puzzle delimited with double space")           
    parser.add_argument('-r', '--random'   , action="store_true", help ="generate random instance from shape")  
    parser.add_argument('-s', '--shape'    , nargs='+', type = int, help ="shape of random instance default (4,4)")  
    parser.add_argument("-w", "--weighted", action="store_true",
                    help="use weights in IDA*")    
    args = parser.parse_args()
    if args.filename :
        start = read_state_from_file(args.filename)
        end   = generate_default_goal(shape(start)) 
    elif args.random : 
        if args.shape :
            end = generate_default_goal(args.shape)
        else:
            end = generate_default_goal((4,4))
        start = shuffle_puzzle(end)
    else:
        parser.print_help(sys.stderr)
        return

    solve(start, end, "manhattan distance", weighted=args.weighted)

main() 


