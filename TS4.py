#practice

#1  prime number within 100

for num in range(2,100):
    is_prime = True
    for i in range(2,int(num ** 0.5)):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
"""
   # to compare(from TS3)
    #1 prime number judgement
num = int(input("please enter a positive integer:"))
end = int(num ** 0.5)
is_prime = True
for i in range(2,end + 1):
    if num % i ==0:
        is_prime = False
        break
if is_prime:
    print(f"{num}is a prime number")
else:
    print(f"{num}is not a prime number")



#2 find Fibonacci sequence (within 20ge)
a,b = 0,1
for _ in range(20):
    a,b = b,a+b
    print(a)

#3 find narcissistic number
for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


# how to reverse a positive integer

num = int(input("please enter your number"))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10 #num = num // 10
print(reversed_num)
"""

# 100 dollars 100 chickens
for x in range(0,21):
    for y in range(0,34):
        for z in range(0,100,3):
            if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
                print(f"rooster{x},hen{y},chick{z}")

    # simpler
for x in range(0,21):
    for y in range(0,34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f"rooster{x},hen{y},chick{z}")

# craps game
import random

money = 1000
while money > 0:
    print(f"your total:{money}")
    while True:
        debt = int(input("please bet:"))
        if 0 < debt <= money:
            break
    first_point = random.randrange(1,7) + random.randrange(1,7)
    print(f"\n your number:{first_point}")
    if first_point == 7 or first_point == 11:
        print("player wins\n")
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print("The house wins.\n")
        money -= debt
    else:
        while True:
            current_number = random.randrange(1,7) + random.randrange(1,7)
            print(f"your number:{current_number}")
            if current_number == 7:
                print("The house wins.\n")
                money -= debt
                break
            elif current_number == first_point:
                print("player wins.\n")
                money += debt
                break
print("you’re broke!Game over！")

#i study this game for a week i almost die.i might completely forget about it someday but don't worry i will practice this somehow..haha no fun!



#以上截止2025.12.26的练习记录









