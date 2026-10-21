import numpy as np
def init_matrix(a, b, gap=-2):
      matrix= np.zeros((len(a) + 1, len(b)+1), dtype =int)
      for i in range(len(a)+1):
            matrix[i][0]= i * gap
            
      for j in range(len(b)+1):
          matrix[0][j]= j *  gap
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
def fill_matrix(a, b, match=1, mismatch=-1, gap=-2):
      matrix= init_matrix(a,b, gap)
      for i in range (1, len(a)+1):
            for j in range(1, len(b)+1):
                  matrix[i][j]=cell_value(a, b, matrix, i,j, match, mismatch, gap)

      return matrix
def traceback(a, b, matrix, match=1, mismatch=-1, gap=-2):
      i=len(a)
      j=len(b)
      aligned_a=""
      aligned_b=""

      while i>0 or j>0:
            diagonal_ok=False
            if i>0 and j>0:
                  s=match if a[i-1]==b[j-1] else mismatch
                  diagonal_ok= matrix[i][j]== matrix[i-1][j-1] + s
            if diagonal_ok:
                  aligned_a=a[i-1]+ aligned_a
                  aligned_b=b[j-1]+ aligned_b
                  i-=1
                  j-=1

            elif i>0 and matrix[i][j]== matrix[i-1][j]+ gap :
                  aligned_a=a[i-1]+ aligned_a
                  aligned_b="-" + aligned_b
                  i-=1
            else:
                  aligned_a= "-" + aligned_a
                  aligned_b=b[j-1]+ aligned_b
                  j-=1
      return aligned_a, aligned_b

def needleman_wunsch(a, b, match=1, mismatch=-1, gap=-2):
      matrix= fill_matrix(a, b, match, mismatch, gap)
      aligned_a, aligned_b= traceback(a,b, matrix, match, mismatch, gap)
      i=len(a)
      j=len(b)
      score=matrix[i][j]
      return aligned_a, aligned_b, score

def show_alignment(aligned_a, aligned_b, score):
    middle=""
    for x, y in zip(aligned_a, aligned_b):
       if x==y:
           middle+="|"
       elif x=="-" or y=="-":
             middle +=" "
       else:
             middle += " "
             
    print(aligned_a)
    print(middle)
    print(aligned_b)
    print("Score:", score)

x, y, score = needleman_wunsch("GAT", "GT")
show_alignment(x, y, score)

x, y, score = needleman_wunsch("ATGCTAGC", "ATGCGAGC")
show_alignment(x, y, score)
