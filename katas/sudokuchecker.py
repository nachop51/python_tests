def checkRowCol(board):
    l = []
    i, j = 0, 0
    while i < 9:
        l = [1,2,3,4,5,6,7,8,9]
        j = 0
        while j < 9:
            try:
                l.remove(board[i][j])
            except:
                return False
            j+=1
        l = [1,2,3,4,5,6,7,8,9]
        j = 0
        while j < 9:
            try:
                l.remove(board[j][i])
            except:
                return False
            j+=1
        i+=1
    return True

def checkSquare(square):
    l = [1,2,3,4,5,6,7,8,9]
    for i in square:
        try:
            l.remove(i)
        except:
            return False
    return True

def valid_solution(board):
    if checkRowCol(board):
        l, l2, l3 = [], [], []
        j = 0
        for i in range(9):
            for j in range(9):
                if j < 3:
                    l.append(board[i][j])
                elif j >= 3 and j < 6:
                    l2.append(board[i][j])
                else:
                    l3.append(board[i][j])
            if i == 2 or i == 5 or i == 8:
                cl = [l, l2, l3]
                for list in cl:
                    if checkSquare(list) == False:
                        return False
                l.clear()
                l2.clear()
                l3.clear()
        return True
    else:
        return False

board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]

board2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
          [6, 7, 2, 1, 9, 0, 3, 4, 9],
          [1, 0, 0, 3, 4, 2, 5, 6, 0],
          [8, 5, 9, 7, 6, 1, 0, 2, 0],
          [4, 2, 6, 8, 5, 3, 7, 9, 1],
          [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 0, 1, 5, 3, 7, 2, 1, 4],
          [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 0, 0, 4, 8, 1, 1, 7, 9]]

# print(checkRowCol(board))
# print(checkRowCol(board2))
print(valid_solution(board))
print(valid_solution(board2))