# 4N-3 colums
# 2N-1 rows

def print_rangoli(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rows = 2*n-1
    colums = 4*n-3
    m=0 #rows to bypass
    
    matrix = [["-" for i in range(0,colums)] for i in range(0,rows)]

    for i in range(n-1,-1,-1):
        letter = alphabet[i]
        j= int(colums/2)
        k= j
        for r in range(0+m,int(rows/2)+1):
            matrix[r][j] = letter
            matrix[r][k] = letter
            j=j+2
            k=k-2
        j=j-2
        k=k+2
        for r in range(int(rows/2)+1,rows-m):
            j=j-2
            k=k+2
            matrix[r][j] = letter
            matrix[r][k] = letter
        m=m+1
        
    for i in range(0,rows):
        for j in range(0,colums):
            print(matrix[i][j],end="")
        print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)