

def rotate_90(matrix: list):
    
    matrix.reverse()
    
    for i in range(len(matrix)):
        for j in range(i):
           matrix[i][j],  matrix[j][i]  =  matrix[j][i], matrix[i][j]
    
    print(matrix)
    
    return matrix


matrix = [
    [1,2,3],
    [1,2,3],
    [1,5,3],
]

for x in rotate_90(matrix):
    print(x)
