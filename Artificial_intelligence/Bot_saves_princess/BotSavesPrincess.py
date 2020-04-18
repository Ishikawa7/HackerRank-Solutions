#input
n = int(input())
matrix = input()

for i in range(0,n-2): #skip useles rows
    input()

matrix = matrix + input()
combinations = ["",""]

#detect princess position and set the proper "zig-zag" combinations
if matrix[0] == 'p':
    combinations[0] = "UP"
    combinations[1] = "LEFT"
else:
    if matrix[n-1] == 'p':
        combinations[0] = "UP"
        combinations[1] = "RIGHT"
    else:
        if matrix[n] == 'p':
            combinations[0] = "DOWN"
            combinations[1] = "LEFT"
        else:
            combinations[0] = "DOWN"
            combinations[1] = "RIGHT"

#move towards the princess
for i in range(0,int((n-1)/2)):
    print (combinations[0])
    print (combinations[1])