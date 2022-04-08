level = [
    '-*-*-'.split(),
    '--*--'.split(),
    '----*'.split(),
    '*----'.split()
]

"""SOLUTION = [
    '1*3*1',
    '12*32',
    '1212*',
    '*1011',
]"""

def amount_bombs(lis,i,j):
    """ Returns the amount of bombs around a position. """
    amount = 0
    if i > 0:
        if j > 0:
            if is_bomb(lis[i-1][j-1]):
                amount += 1
        if j < 4:
            if is_bomb(lis[i-1][j+1]):
                amount += 1
        if is_bomb(lis[i-1][j]):
            amount += 1
    
    if j > 0:
        if is_bomb(lis[i][j-1]):
            amount += 1
    if 4 > j:
        if is_bomb(lis[i][j+1]):    #Me tira error aca, IndexError: list index out of range
            amount += 1

    if i < 3:
        if j > 0:
            if is_bomb(lis[i+1][j-1]):
                amount += 1
        if j < 4:
            if is_bomb(lis[i+1][j+1]):
                amount += 1
        if is_bomb(lis[i+1][j]):
            amount += 1

    return amount

def is_bomb(pos):
    """ Returns True if there is a bomb in the position passed as an argument. """
    return pos == '*'

def make_solution (lis):
    """ Returns the solution. """
    for i in range(4):              # 4 como la cant de lineas
        for j in range(5):          # 5 como la cant de columnas
            if not is_bomb(lis[i][j]):
                #amount_bombs(list,i,j)
                lis[i][j] = amount_bombs(lis,i,j)

solution = level.copy()
print(make_solution(solution))