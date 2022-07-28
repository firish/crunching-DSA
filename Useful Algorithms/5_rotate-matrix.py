# This is a common algorith for matrix rotation
# (Not rotating elements by N, but rotating entire matrix)
# (90 degree, 180 degree, 270 degree and then back)


#  clockwise rotate
#  first reverse up to down, then swap the symmetry
#  1 2 3     7 8 9     7 4 1
#  4 5 6  => 4 5 6  => 8 5 2
#  7 8 9     1 2 3     9 6 3

# Rotate by 90
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
N = len(matrix)
i, j = 0, N - 1
while i < j:
    matrix[i], matrix[j] = matrix[j], matrix[i]
    i += 1;
    j -= 1

for i in range(N):
    for j in range(i + 1):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)

#  anticlockwise rotate
#  first reverse left to right, then swap the symmetry
#  1 2 3     3 2 1     3 6 9
#  4 5 6  => 6 5 4  => 2 5 8
#  7 8 9     9 8 7     1 4 7
