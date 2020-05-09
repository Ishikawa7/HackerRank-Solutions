from itertools import product

first_line = input()
second_line = input()
list1 = map(int,first_line.split(" "))
list2 = map(int,second_line.split(" "))

print(*product(list1,list2))
