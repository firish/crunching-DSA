# for each point, you must visit all 8 neighbors, if applicable

Mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]  # Matrix to be traversed
M, N = len(Mat), len(Mat[0])  # M is no of rows, N is no of cols

dir_row = [-1, -1, 0, 1, 1, 1, 0, -1]
dir_col = [0, 1, 1, 1, 0, -1, -1, -1]


def toVisit(M, N, row, col):
    if row < 0 or col < 0 or row >= M or col >= N: return False
    else: return True


for row in range(M):
    for col in range(N):
        neighbors = []
        for i in range(8):
            x, y = row + dir_row[i], col + dir_col[i]
            if toVisit(M, N, x, y):
                neighbors.append(Mat[x][y])
        print("Matrix element ::: " + str(Mat[row][col]) + " has neighbors ::: " + str(neighbors))
