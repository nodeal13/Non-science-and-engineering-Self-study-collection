#circular structure
"""
#example
import time
print("hello_world")
time.sleep(3)
"""


#for-in(if we know how many times)

"""
#no.1
import time

for i in range(1989):
    print("taylor_swift")
    time.sleep(1)#(0-1988)
#no.2
import time

for _  in range(1989):
    print("taylor_swift")
    time.sleep(1)
"""
"""
examples of the use of range
    range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
    range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
    range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
    range(100,0,-2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。 
"""
#the sum of 1-100

#one by one
total=0
for i in range(1,101):
    total += i
print(total)

#even number
#1
total1=0
for i in range(1,101):
    if i %2 == 0:
        total1 += i
print(total1)

#2
total2=0
for i in range(2,101,2):
    total2 += i
print(total2)
#3
total3=0
for i in range(0,101,2):
    total3 += i
print(total3)

#4
print(sum(range(2,101,2)))




#while(if u don't know how many times you should cycle and you really wanna built a circular structure)

#the sum of 1-100
total4 = 0
i = 1
while i <=100:
    total4 += i
    i += 1
print(total4)
#even
total5 = 0
i = 2
while i <= 100:
    total5 += i
    i += 2
print(total5)
#odd number
total6 = 0
i = 1
while i <= 100:
    total6 += i
    i += 2
print(total6)

#break and continue

#even
total7 = 0
i = 2
while True:#construct a loop with a condition that is always true (infinite loop=endless loop))
    total7 += i
    i += 2
    if i >100:
        break
print(total7)


total8 = 0
for i in range(1,101):
    if i %2 != 0:
        continue
    total8 += i
print(total8)


#nested loop structure (we're going to comprehend the whole thing in this part)
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}x{j}={i * j}", end="\t")#end="\t" is to make the new line not just switch to the next line like...just like the ninety-nine multiplication table we used to see when we're in the primary school haha
    print()#to achieve the effect of new lines

"""
#how to apply

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

#2 find the greatest common divisor(GCD)(Euclidean algorithm)
x = int(input("x = "))
y = int (input("y = "))
while y % x != 0:
    x, y = y % x, x
print(f"GCD:{x}")
"""
#3 guess the number game
import random

answer = random.randrange(1,101)
counter = 0
while True:
    counter += 1
    num = int(input("tell me your answer:"))
    if num < answer:
        print("more")
    elif num > answer:
        print("less")
    else:
        print("yeeeees!")
        break
print(f"you total guess {counter}")


#以上截止2025.12.14的练习记录
































