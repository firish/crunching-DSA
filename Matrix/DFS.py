# Depth First Search for a 2D array in Python
# Use a Stack
# Maintain a separate data structure to see if a node has been already visited

Mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix to be traversed via DFS
M, N = len(Mat), len(Mat[0])
visited = [[False for i in range(N)] for j in range(M)]
for row in Mat: print(row)

def is_valid(visited, row, col, M, N):
    if row < 0 or col < 0 or row >= M or col >= N or visited[row][col]: return False
    else: return True

# Every point in a Matrix has 4 next points according to DFS
# these are left-down-right-up [row, col-1] [row+1, col], [row, col+1] [row-1, col] in anticlockwise direction
dir_row = [0, 1, 0, -1]
dir_col = [-1, 0, 1, 0]


def DFS(Mat):
    stack = []
    stack.append([0, 0])
    while len(stack) > 0:
        point = stack.pop()
        r, c = point[0], point[1]

        if not is_valid(visited, r, c, M, N): continue
        visited[r][c] = True
        print(Mat[r][c], end=" ")

        for i in range(4):
            x, y = r + dir_row[i], c + dir_col[i]
            stack.append([x, y])


DFS(Mat)





