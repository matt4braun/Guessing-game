import random
number = 101
goal = random.randint(1,100)
while number != goal:
    number = int(input("guess a number"))
    if number>goal:
        print("lower")
    elif number<goal:
        print("higher")
    else:
        print("CORRECT")
    
    
