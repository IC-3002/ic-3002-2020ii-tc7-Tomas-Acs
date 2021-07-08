




N = 4
C = [ [ 0 for j in range(4) ] for i in range(4) ]


def encontrar_ruta(C):   
    R = [ [ 0 for j in range(4) ] for i in range(4) ] 
      
    if resolver(C, 0, 0, R) == False: 
        return False
    return True

def check( C, x, y ): 
      
    if x >= 0 and x < N and y >= 0 and y < N and C[x][y] == 0: 
        return True
      
    return False




      
def resolver(C, x, y, R): 
      

    if x == N-1 and y == N-1 and C[x][y]== 0: 
        R[x][y] = 1
        return True
          
    if check(C, x, y) == True: 
     
        R[x][y] = 1
          
  
        if resolver(C, x + 1, y, R) == True: 
            return True
     
        if resolver(C, x, y + 1, R) == True: 
            return True
          
     
        R[x][y] = 0
        return False


encontrar_ruta(C)
 







