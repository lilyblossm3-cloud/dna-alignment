import numpy as np
def sw_fill(a, b, match=1, mismatch=-1, gap=-2):
    matrix= np.zeros((len(a)+1, len(b)+1), dtype=int)
    best=0
    best_pos=(0,0)
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1]==b[j-1]:
                s=match
            else:
                s=mismatch

            diagonal=matrix[i-1][j-1]+s
            up=matrix[i-1][j]+gap
            left=matrix[i][j-1]+gap
            matrix[i][j]= max(0, diagonal, up, left)
            if matrix[i][j]>best:
               best=matrix[i][j]
               best_pos=(i,j)
    return (matrix, best, best_pos)
def sw_traceback(a,b, matrix, best_pos, match=1, mismatch=-1, gap=-2):
    i, j= best_pos
    aligned_a=""
    aligned_b=""

    while i>0 and j>0 and matrix[i][j]>0:
        s=match if a[i-1]==b[j-1] else mismatch

        if matrix[i][j] == matrix[i-1][j-1] + s :
            aligned_a= a[i-1] + aligned_a
            aligned_b= b[j-1] + aligned_b
            i-=1
            j-=1
        elif matrix[i][j]==matrix[i-1][j] + gap:
            aligned_a= a[i-1] + aligned_a
            aligned_b="-"+ aligned_b
            i-=1
        else:
            aligned_a="-"+ aligned_a
            aligned_b=b[j-1] + aligned_b
            j-=1
    return aligned_a, aligned_b

matrix, best, best_pos=sw_fill("TTACG", "ACG")
x, y=sw_traceback("TTACG", "ACG", matrix, best_pos)
print(x)
print(y)
   