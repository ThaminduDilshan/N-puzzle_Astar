# import sys
import copy


# get heuristic value based on no of misplaced tiles for puzzle
def heu_no_of_misplaced(st, gl):
    heu = 0
    for l_no in range(0, len(st), 1):
        for v_no in range(0, len(st[l_no]), 1):
            ele = st[l_no][v_no]
            if( ele != '-' and ele != gl[l_no][v_no] ):
                heu += 1
    
    return heu


# get heuristic based on manhatten distance for given node
def heu_node(node, current_loc, goal_puz):
    desired = None
    for i in range(0, len(goal_puz), 1):
        if str(node) in goal_puz[i]:
            desired = [ i, goal_puz[i].index(str(node)) ]
            break
    heu = abs(int(current_loc[0]) - int(desired[0])) + abs(int(current_loc[1]) - int(desired[1]))
    return heu

# get heuristic value based on manhatten distance for puzzle
def heu_manhatten(st, gl):
    heu = 0
    for rw_no in range(0, len(st), 1):
        for ind in range(0, len(st[rw_no]), 1):
            if(st[rw_no][ind] != '-'):
                heu += heu_node( st[rw_no][ind], [rw_no, ind], gl )
    return heu


# get possible move of a empty node
def possible_move(puzzle, node_id):         # node_id = [row][column]
    moves = []
    if node_id[0] == 0:         # at top row
        if node_id[1] == 0:        # at top left
            # possible moves => down, right
            if( puzzle[node_id[0]+1][node_id[1]] != '-' ):     # move down
                moves.append( [node_id[0]+1, node_id[1], 'up', puzzle[node_id[0]+1][node_id[1]]] )
            if( puzzle[node_id[0]][node_id[1]+1] != '-' ):     # move right
                moves.append( [node_id[0], node_id[1]+1, 'left', puzzle[node_id[0]][node_id[1]+1]] )
        elif node_id[1] == len(puzzle)-1:        # at top right
            # possible moves => down, left
            if( puzzle[node_id[0]+1][node_id[1]] != '-' ):     # move down
                moves.append( [node_id[0]+1, node_id[1], 'up', puzzle[node_id[0]+1][node_id[1]]] )
            if( puzzle[node_id[0]][node_id[1]-1] != '-' ):     # move left
                moves.append( [node_id[0], node_id[1]-1, 'right', puzzle[node_id[0]][node_id[1]-1]] )
        else:       # top but not at an edge
            # possible moves => left, right, down
            if( puzzle[node_id[0]+1][node_id[1]] != '-' ):     # move down
                moves.append( [node_id[0]+1, node_id[1], 'up', puzzle[node_id[0]+1][node_id[1]]] )
            if( puzzle[node_id[0]][node_id[1]+1] != '-' ):     # move right
                moves.append( [node_id[0], node_id[1]+1, 'left', puzzle[node_id[0]][node_id[1]+1]] )
            if( puzzle[node_id[0]][node_id[1]-1] != '-' ):     # move left
                moves.append( [node_id[0], node_id[1]-1, 'right', puzzle[node_id[0]][node_id[1]-1]] )

    elif node_id[0] == len(puzzle)-1:        # at bottom row
        if node_id[1] == 0:        # at bottom left
            # possible moves => up, right
            if( puzzle[node_id[0]-1][node_id[1]] != '-' ):     # move up
                moves.append( [node_id[0]-1, node_id[1], 'down', puzzle[node_id[0]-1][node_id[1]]] )
            if( puzzle[node_id[0]][node_id[1]+1] != '-' ):     # move right
                moves.append( [node_id[0], node_id[1]+1, 'left', puzzle[node_id[0]][node_id[1]+1]] )
        elif node_id[1] == len(puzzle)-1:        # at bottom right
            # possible moves => up, left
            if( puzzle[node_id[0]-1][node_id[1]] != '-' ):     # move up
                moves.append( [node_id[0]-1, node_id[1], 'down', puzzle[node_id[0]-1][node_id[1]]] )
            if( puzzle[node_id[0]][node_id[1]-1] != '-' ):     # move left
                moves.append( [node_id[0], node_id[1]-1, 'right', puzzle[node_id[0]][node_id[1]-1]] )
        else:       # bottom but not at an edge
            # possible moves => up, left, right
            if( puzzle[node_id[0]-1][node_id[1]] != '-' ):     # move up
                moves.append( [node_id[0]-1, node_id[1], 'down', puzzle[node_id[0]-1][node_id[1]]] )
            if( puzzle[node_id[0]][node_id[1]-1] != '-' ):     # move left
                moves.append( [node_id[0], node_id[1]-1, 'right', puzzle[node_id[0]][node_id[1]-1]] )
            if( puzzle[node_id[0]][node_id[1]+1] != '-' ):     # move right
                moves.append( [node_id[0], node_id[1]+1, 'left', puzzle[node_id[0]][node_id[1]+1]] )
    else:           # at middle
        if node_id[1] == 0:        # at middle left edge
            # moves => up, down, right
            if( puzzle[node_id[0]-1][node_id[1]] != '-' ):     # move up
                moves.append( [node_id[0]-1, node_id[1], 'down', puzzle[node_id[0]-1][node_id[1]]] )
            if( puzzle[node_id[0]+1][node_id[1]] != '-' ):     # move down
                moves.append( [node_id[0]+1, node_id[1], 'up', puzzle[node_id[0]+1][node_id[1]]] )
            if( puzzle[node_id[0]][node_id[1]+1] != '-' ):     # move right
                moves.append( [node_id[0], node_id[1]+1, 'left', puzzle[node_id[0]][node_id[1]+1]] )
        elif node_id[1] == len(puzzle)-1:        # at middle right edge
            # moves => up, down, left
            if( puzzle[node_id[0]-1][node_id[1]] != '-' ):     # move up
                moves.append( [node_id[0]-1, node_id[1], 'down', puzzle[node_id[0]-1][node_id[1]]] )
            if( puzzle[node_id[0]+1][node_id[1]] != '-' ):     # move down
                moves.append( [node_id[0]+1, node_id[1], 'up', puzzle[node_id[0]+1][node_id[1]]] )
            if( puzzle[node_id[0]][node_id[1]-1] != '-' ):     # move left
                moves.append( [node_id[0], node_id[1]-1, 'right', puzzle[node_id[0]][node_id[1]-1]] )
        else:       # not at an edge
            # moves => up, down, left, right
            if( puzzle[node_id[0]-1][node_id[1]] != '-' ):     # move up
                moves.append( [node_id[0]-1, node_id[1], 'down', puzzle[node_id[0]-1][node_id[1]]] )
            if( puzzle[node_id[0]+1][node_id[1]] != '-' ):     # move down
                moves.append( [node_id[0]+1, node_id[1], 'up', puzzle[node_id[0]+1][node_id[1]]] )
            if( puzzle[node_id[0]][node_id[1]-1] != '-' ):     # move left
                moves.append( [node_id[0], node_id[1]-1, 'right', puzzle[node_id[0]][node_id[1]-1]] )
            if( puzzle[node_id[0]][node_id[1]+1] != '-' ):     # move right
                moves.append( [node_id[0], node_id[1]+1, 'left', puzzle[node_id[0]][node_id[1]+1]] )
    
    return moves


# get new puzzle by moving given empty slot
def moved_puzzle(puzzle, empty_loc, move):
    new_puz = copy.deepcopy(puzzle)
    new_puz[move[0]][move[1]] = '-'
    new_puz[empty_loc[0]][empty_loc[1]] = move[3]
    return new_puz


# get empty slots of the puzzle
def getEmptySlots(puzzle):
    empty = []
    for row in range(0, len(puzzle), 1):
        if '-' in puzzle[row]:
            empty.append( [row, (puzzle[row]).index('-')] )

    return empty


# get puzzle with minimum f(n)
def get_min(arr):            # [[val, puzzle], ..]
    new_arr = copy.deepcopy(arr)
    min_ = new_arr.pop(0)       # pop first element
    while(len(new_arr)!=0):
        ele = new_arr.pop()
        if( ele[0] < min_[0] ):
            min_ = ele
    index = arr.index( [min_[0], min_[1], min_[2], min_[3], min_[4], min_[5]] )
    return [min_, index]


# check if f(n) has decreased
def check_decreased(arr, puzzle, fn):
    new_arr = copy.deepcopy(arr)
    puz_list = []
    val_list = []

    while(len(new_arr)!=0):
        ele = new_arr.pop(0)
        puz_list.append(ele[1])         # add puzzles to an array
        val_list.append(ele[0])         # add f(n) values to an array

    if( puz_list.count(puzzle) != 0 ):      # if exist in puzzle list
        index = puz_list.index(puzzle)      # get index of puzzle
        val = val_list[index]               # get f(n) of relevent puzzle
        if( int(val) < int(fn) ):
            return [True, val, index]
        elif( int(val) == int(fn) ):
            return [True, 'same']
        else:
            return [False, 'in']
    else:
        return [False, 'not']


# A* algorithm to reach goal
def A_star(st1, gl, heu_selector):
    evaluating_puzzle = st1
    breakFlag = False
    opened = []
    closed = []

    if(heu_selector=='manhatten'):          # manhatten heuristic
        fn = heu_manhatten(st1, gl) + 0
    else:               # no of misplaced tiles heuristic
        fn = heu_no_of_misplaced(st1, gl) + 0
    opened.append( [fn, evaluating_puzzle, 0, fn, None, None] )         # fourth parameter is heuristic (here it is same as fn)

    while(True):
        if( len(opened) == 0 ):         # terminate if opened is empty (no result)
            return ''
        
        # get min from opened and save in closed
        temp_data = get_min(opened)
        cur_data = temp_data[0]
        evaluating_puzzle = cur_data[1]
        poped = opened.pop(temp_data[1])
        closed.append( poped )
        
        # terminate condition (result success)
        if heu_no_of_misplaced(evaluating_puzzle, gl) == 0:     # goal reached
            fin_current = cur_data
            moved_path = ''
            while( fin_current[4] != None ):
                moved_path += '(' + str(fin_current[5][0]) + ', ' + str(fin_current[5][1]) + '), '
                fin_current = fin_current[4]
            return moved_path

        # get each successor for a given node
        empty_slots = getEmptySlots(evaluating_puzzle)                 # get empty slots
        for slot in empty_slots:
            moves = possible_move(evaluating_puzzle, slot)             # move each empty slot if possible
            if( len(moves) != 0 ):
                for move in moves:                      # for each move
                    new_puzzle = moved_puzzle(evaluating_puzzle, slot, move)
                    
                    if(heu_selector=='manhatten'):          # manhatten heuristic
                        heuristic = heu_manhatten(new_puzzle, gl)
                    else:               # no of misplaced tiles heuristic
                        heuristic = heu_no_of_misplaced(new_puzzle, gl)

                    check_open = check_decreased(opened, new_puzzle, heuristic+cur_data[2]+1)
                    if(check_open[0] == True):           # node with a lesser f(n) in the open
                        continue        # skip
                    else:
                        check_close = check_decreased(closed, new_puzzle, heuristic+cur_data[2]+1)
                        if(check_close[0] == True):         # node with a lesser f(n) in the closed
                            if(check_close[1] != 'same'):
                                ele_close = closed.pop(check_close[2])
                                opened.append(ele_close)
                        else:           # lesser node not in open or closed
                            gm = cur_data[2] + 1
                            fm = heuristic + gm
                            opened.append( [fm, new_puzzle, gm, heuristic, cur_data, (move[3], move[2])] )




## executing N puzzle problem
start = []
goal = []

try:
    # read command line arguments
    # start_file = (sys.argv)[1]
    # goal_file = (sys.argv)[2]
    inp = (input("Enter start config and goal config files : ")).split(' ')
    start_file = inp[0]
    goal_file = inp[1]

    # read start configuration file
    with open(start_file, 'r') as f_st:
        lines = f_st.read().split('\n')
        for line in lines:
            if line != '':
                start.append( line.split('\t') )

    # read goal configuration file
    with open(goal_file, 'r') as f_go:
        lines = f_go.read().split('\n')
        for line in lines:
            if line != '':
                goal.append(line.split('\t'))

    # execute A* algorithm
    moveStr = A_star(start, goal, 'manhatten')
    moveStr = moveStr[:-2]
    print("Input file : " + start_file + "\nGoal file : " + goal_file)
    print("Output : " + moveStr)
    print("Output file : output.txt")

    # write output to 'output.txt'
    with open('output.txt', 'w') as fo:
        fo.write(moveStr)
    print('success')


except IndexError:
    print("[ERROR] Invalid command line arguments !!!")
except FileNotFoundError:
    print("[ERROR] File not found !!!")
except:
    print("[ERROR] Error during execution !!!")


'''
TO RUN TYPE BELOW COMMAND
    python Npuzzle_Astar.py start.txt goal.txt

'''