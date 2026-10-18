import numpy as np
def init_matrix(a, b, gap=-2):
      matrix= np.zeros((len(a) + 1, len(b)+1), dtype =int)
      for i in range(len(a)+1):
            matrix[i][0]= i * gap
            
      for j in range(len(b)+1):
          matrix[0][j]= j *gap
      return matrix    

print(init_matrix("GAT", "GT"))