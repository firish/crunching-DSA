# Breadth First Search for a 2D array in Python
# Use a queue
# Maintain a separate data structure to see if a node has been already visited

Mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]  # Matrix to be traversed via BFS
M, N = len(Mat), len(Mat[0])  # M is no of rows, N is no of cols
visited = [[False for i in range(N)] for i in range(M)]  # keeps track of visited nodes


# Every point in a Matrix has 4 next points according to BFS
# these are [row-1, col], [row, col+1], [row+1, col] and [row, col-1] in clockwise direction
dir_row = [-1, 0, 1, 0]
dir_col = [0, 1, 0, -1]

# Import inbuilt queue
from collections import deque as queue


# Function checks if a point is to be visited/added to queue
def isValid(visited, row, col):
    if row < 0 or col < 0 or row >= M or col >= N:
        return False
    if visited[row][col]:
        return False
    return True


def BFS(visited, row, col, Mat):
    q = queue()
    q.append((row, col))
    visited[row][col] = True

    while len(q) > 0:
        point = q.popleft()
        r, c = point[0], point[1]
        # This is where every node is visited in BFS order
        print(Mat[r][c], end="-> ")

        # Add neighbors to the queue
        for i in range(4):  # 4 as any given points is checked for 4 neighbors
            adj_r, adj_c = r + dir_row[i], c + dir_col[i]
            if isValid(visited, adj_r, adj_c):
                q.append((adj_r, adj_c))
                visited[adj_r][adj_c] = True


BFS(visited, 0, 0, Mat)
