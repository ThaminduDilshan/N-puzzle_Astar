import Npuzzle_Astar as Astar
from random import randint


# returns a random puzzle string for given n, N
def random_puzzle(n, N):
    array = []
    for st in range(1, N+1, 1):
        array.append(str(st))
    array.append('-')
    array.append('-')

    puzzle = []
    for i in range(0, n, 1):
        row = []
        for j in range(0, n, 1):
            row.append( array.pop(randint(0, len(array)-1)) )
        puzzle.append(row)

    return puzzle



# check efficiency for 100 test cases
final_result = ''

for test in range(1, 101, 1):
    print( "testing : " + ('%03d' % test) )
    n = randint(4, 4)
    N = (n**2) - 2
    start = random_puzzle(n ,N)
    goal = random_puzzle(n, N)

    print("\n=====================================================")
    print(start)
    print(goal)

    # no of misplaced tiles heuristic
    moveStr = Astar.A_star(start, goal, 'misplaced')
    moveStr = moveStr[:-2]
    no_of_moves_mis = len( moveStr.split(',') )

    # manhatten heuristic
    moveStr = Astar.A_star(start, goal, 'manhatten')
    moveStr = moveStr[:-2]
    no_of_moves_man = len( moveStr.split(',') )

    # append result to output
    final_result += "test" + ('%03d' % test) + "\t\t" + str(no_of_moves_mis) + "\t" + str(no_of_moves_man) + "\n"

with open('evaluation_result.txt', 'w') as fe:
    fe.write(final_result)

print(final_result)


# n = 3, 4, 5, 
# N = 7, 14, 23
# N = (n**2) - 2
