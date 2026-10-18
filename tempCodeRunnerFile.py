import numpy as np
def init_matrix(a, b, gap=-2):
      matrix= np.zeros((len(a) + 1, len(b)+1), dtype =int)
      for i in range(len(a)+1):
            matrix[i][0]= i * gap
            
      for j in range(len(b)+1):
          matrix[0][j]= j *gap
      return matrix    
def cell_value(a, b, matrix, i , j, match=1, mismatch=-1, gap=-2):
         if a[i-1]==b[j-1]:
               s=match
         else:
               s=mismatch

         diagonal=matrix[i-1][j-1] + s
         up= matrix[i-1][j] + gap
         left=matrix[i][j-1]+ gap

         return max(diagonal, up, left)
m=init_matrix("GAT", "GT")
print(cell_value("GAT", "GT", m, 1, 1))