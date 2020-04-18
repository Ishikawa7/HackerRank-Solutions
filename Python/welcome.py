'''
Mat size must be N*M. (N is an odd natural number, and is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Input Format
A single line containing the space separated values of N and M. 
'''


N,M = list(map(int,input().split()))

p=".|."
np = 1
nc = int(N/2)

for i in range(0,nc):
    print( (int(3*(N-np)/2))*"-" + np * p + (int(3*(N-np)/2))*"-" )
    np = np+2
print(int((3*N-7)/2)*"-"+"WELCOME"+int((3*N-7)/2)*"-")
for i in range(0,nc):
    np = np-2
    print( (int(3*(N-np)/2))*"-" + np * p + (int(3*(N-np)/2))*"-" )