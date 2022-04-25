def checkDiagonal(p, k):
    p
    i, j = p[0], p[1]
    ki, kj = k[0], k[1]
    while i >= 0 and j >= 0:
        if i == ki and j == kj:
            return 1
        i-=1
        j-=1
    i, j = p[0], p[1]
    while i < 8 and j < 8:
        if i == ki and j == kj:
            return 1
        i-=1
        j+=1

def checkHorsy(p, k):
    i, j = p[0], p[1]
    if [i-1, j+2] == k:
        return ['knight']
    elif [i-1, j-2] == k:
        return ['knight']
    elif [i-2, j-1] == k:
        return ['knight']
    elif [i-2, j+1] == k:
        return ['knight']
    else:
        return []

def promotion(board):
    # Do some botato :)
    i = 0
    p = []
    k = []
    check = []
    while i < 8:
        j = 0
        while j < 8:
            if board[i][j] == 'P':
                p.append(i)
                p.append(j)
            if board[i][j] == 'K':
                k.append(i)
                k.append(j)
            j+=1
        print(board[i])
        i+=1
    if p == [] or k == []:
        return check
    if p[0] != 7:
        return check
    if p[0] == k[0] or p[1] == k[1]:
        check += ['queen', 'rook']
    elif checkDiagonal(p, k) == 1:
        check += ['queen', 'bishop']
    else:
        check = checkHorsy(p, k)
    return check

print(promotion([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'P', ' ', 'K', ' ', ' ']]))
print(promotion([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'K', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ']]))
print(promotion([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'K', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ']]))
print(promotion([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'K', ' ', ' '], [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ']]))

