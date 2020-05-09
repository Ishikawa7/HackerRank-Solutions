from collections import Counter

n_shoes = int(input())
counter_sizes = Counter(input().split(" "))
n_customers = int(input())

money_earned = 0

for i in range(0,n_customers):
    customer_want = input().split(" ")
    if counter_sizes.get(customer_want[0], 0) != 0 :
        money_earned += int(customer_want[1])
        counter_sizes[customer_want[0]] -= 1

print(money_earned)

