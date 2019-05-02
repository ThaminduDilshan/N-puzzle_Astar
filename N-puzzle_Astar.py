import sys
import copy


# get heuristic value on no of misplaced tiles
def heu_no_of_misplaced(st, gl):
    heu = 0
    for l_no in range(0, len(st), 1):
        for v_no in range(0, len(st[l_no]), 1):
            ele = st[l_no][v_no]
            if( ele != '-' and ele != gl[l_no][v_no] ):
                heu += 1
    
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


# A* algorithm to reach goal
def A_star(st1, gl):
    # moves_taken = []
    moves_taken = ""
    evaluating_puzzle = st1
    breakFlag = False
    
    while(not breakFlag):
        min_move_puzz = None
        min_move_direction = None
        min_move_element = None

        empty_slots = getEmptySlots(evaluating_puzzle)                 # get empty slots
        for slot in empty_slots:
            moves = possible_move(evaluating_puzzle, slot)             # move each empty slot if possible
            if( len(moves) != 0 ):
                for move in moves:                      # for each move
                    new_puzzle = moved_puzzle(evaluating_puzzle, slot, move)
                    heuristic = heu_no_of_misplaced(new_puzzle, gl)
                    if( min_move_puzz == None ):            # if at initial move of current iteration
                        min_move_puzz = [new_puzzle, heuristic]
                        min_move_direction = move[2]        # moved direction (actual element)
                        min_move_element = move[3]          # moved element (actual element)
                    elif( heuristic < min_move_puzz[1] ):       # if current heu is less than previous minimum hue
                        min_move_puzz = [new_puzzle, heuristic]
                        min_move_direction = move[2]        # moved direction (actual element)
                        min_move_element = move[3]          # moved element (actual element)
                    if(heuristic == 0):
                        breakFlag = True
                        break

        evaluating_puzzle = min_move_puzz[0]
        moves_taken += '(' + str(min_move_element) + ',' + str(min_move_direction) + ')' + ', '    # append move actually taken
        # moves_taken.append( (min_move_element, min_move_direction) )    # move actually taken
        # print( (min_move_element, min_move_direction) )

        if min_move_element == None:
            breakFlag = True

    return moves_taken



## executing N puzzle problem
start = []
goal = []

try:
    # read command line arguments
    start_file = (sys.argv)[1]
    goal_file = (sys.argv)[2]

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
    moveStr = A_star(start, goal)
    moveStr = moveStr[:-2]
    print(moveStr)

    # write output to 'output.txt'
    with open('output.txt', 'w') as fo:
        fo.write(moveStr)

except IndexError:
    print("[ERROR] Invalid command line arguments !!!")
except FileNotFoundError:
    print("[ERROR] File not found !!!")
except:
    print("[ERROR] Error during execution !!!")
