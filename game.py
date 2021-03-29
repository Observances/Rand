import random
from random import randint

user1_chosen = []
user2_chosen = []
rannum = []

def solve(s0, s1):
    counter = 0
    n = s0
    m = s1
    for items in n:
        items=int(items)
        for items2 in m:
            items2=int(items2)
            if items == items2:
                counter += 1
    
    return counter

while len(user1_chosen) != 5:
    print("Player 1, input your numbers")
    a = input()
    user1_chosen.append(a)

while len(user2_chosen) != 5:
    print("Player 2, input your numbers")
    a = input()
    user2_chosen.append(a)

while len(rannum) != 5:
    c = random.randint(1, 10)
    rannum.append(c)

ra = solve(user1_chosen, rannum)
rb = solve(user2_chosen, rannum)

if ra > rb:
    print('Player 1 won!')
    print("The numbers were...\n")
    print(f"Your chosen number, {user1_chosen}")
    print(f"The opponent's number, {user2_chosen}")
    print(f"and random numbers, {rannum}")
elif rb > ra:
    print('Player 2 won!')
    print("The numbers were...\n")
    print(f"Your chosen number, {user2_chosen}")
    print(f"The opponent's number, {user1_chosen}")
    print(f"and random numbers, {rannum}")
else:
    print("Draw!")
    print(user1_chosen)
    print(user2_chosen)
    print(rannum)
