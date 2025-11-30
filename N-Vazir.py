import numpy as np

def chess_map(n) :

    matrix1 = np.zeros((n , n))
    n1 = [0 , 1]
    n2 = [n-1 , n-2]
    for _ in range (n//2-1) :

        matrix1[n1[0]][n1[1]] = 1
        matrix1[n2[0]][n2[1]] = 1
        n1[0] += 1
        n1[1] += 2
        n2[0] -= 1
        n2[1] -= 2

    return matrix1

x = int(input('>>>'))
result = chess_map(x)
print(result)
