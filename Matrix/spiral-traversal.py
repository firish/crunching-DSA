# Visit the matrix in spiral manner
# Traverse clock wise around the other edges of MAT

Mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]  # Matrix to be traversed
M, N = len(Mat), len(Mat[0])  # M is no of rows, N is no of cols
visited = [[0 for col in range(N)] for row in range(M)]  # To check if element is visited

# Right -> Down -> left -> Top
dir_row = [0, 1, 0, -1]
dir_col = [1, 0, -1, 0]
# direction can be 0, 1, 2, 3 for different directions
direction = 0

row = col = 0
count = 1
print("Elements traversed in spiral order:")
print("start", end=": ")
while count <= M * N:
    print(Mat[row][col], end="-> ")
    visited[row][col] = 1
    count += 1
    # r and c are used to access the next indices for going in a spiral pattern
    # we use modulo, so r or c can not be greater than len of row/col, and we don't get an index error
    r = abs(row + dir_row[direction]) % M
    c = abs(col + dir_col[direction]) % N

    # we have hit an edge, so change direction
    # use mod 4, as after 4th direction, we have to go back to first direction
    # and keep changing directions in a circular pattern
    if visited[r][c] != 0: direction = (direction + 1) % 4

    # move actual row and column indices based on direction
    row += dir_row[direction]
    col += dir_col[direction]
print("end")



