from typing import List

def print_a(a):
  for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

def count_bombs(r: int, c: int, m3: List[int], NN: int):
  bombs = 0                   #for r in range(rr):
       #for c in range(cc):
  if (r-1 >= 0 and c-1 >= 0 and m3[r-1][c-1]=="B"): 
      bombs=bombs+1   
  if (r-1 >= 0 and m3[r-1][c]=="B"): 
      bombs=bombs+1 
  if (r-1 >= 0 and c+1 <= NN-1 and m3[r-1][c+1]=="B"): 
      bombs=bombs+1 
  if (c-1 >= 0 and m3[r][c-1]=="B"): 
      bombs=bombs+1 
  if (c+1 <= NN-1 and m3[r][c+1]=="B"): 
      bombs=bombs+1 
  if (r+1 <= NN-1 and c-1 >= 0 and m3[r+1][c-1]=="B"): 
      bombs=bombs+1 
  if (r+1 <= NN-1 and m3[r+1][c]=="B"): 
      bombs=bombs+1 
  if (r+1 <= NN-1 and c+1 <= NN-1 and m3[r+1][c+1]=="B"): 
      bombs=bombs+1                
      
  xxx = bombs
  return xxx

def solution(N: int, R: List[int], C: List[int], M: int)->None:
  print("\n1)")
  a = [[0] * N for i in range(N)]
  print_a(a)
  
  print("\n2)")
  for i in range(M):
        a[R[i]][C[i]]="B"

  print_a(a)
  
  print("\n3)")
  for i in range(N):
    for j in range(N):

      if a[i][j]!="B":
        a[i][j]=count_bombs(r=i, c=j, m3=a, NN=N)

  print_a(a)  

N = 3
R = [2, 1, 0, 2] 
C = [0, 2, 1, 2]
M = 4

solution(N, R, C, M)
