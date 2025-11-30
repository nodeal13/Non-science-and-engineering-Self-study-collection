print("butdaddyilovehim!")
import math
print(math.log2(8))
a=-1
b=-2
c=3
#

s="apple"
print(s.upper())


shopping_list=["skateboard","skis"]
#add item to the list
shopping_list.append("screen")
#remove items from the list
shopping_list.remove("skis")
print(shopping_list)
#find max/min/sorted
num_list=[1,2,3,4,5,-11]
print(max(num_list))
print(min(num_list))
print(sorted(num_list))

print(type(shopping_list))
name_type =type(shopping_list)
print(name_type)

her_name = "Taylor_Swift"
born_year = "1989"
print(f"hi guys my name's {her_name} I was born in {born_year}")






#1
pi = 3.1415926
# 请在这里写两行代码
print("now we're going to %.3f" % pi)
print("%.3f" % pi )
print("%010.2f" % pi)
#2
rate = 0.028
# 请在这里写一行代码
print("汇率：%10.2f" % rate)

#3
salary = 123456.789
# 请在这里写一行代码

#4
ace=10
print(ace)

flag0 = 1==1
flag1 = 2>1
flag3 = 1>2
flag4 = flag1 and flag3
print(flag4)
"""
# let's convert fahrenheit to celsius
f = float(input("please enter fahrenheit:"))
c = (f - 32) / 1.8
print("%4.1f fahrenheit = % .1f celsius" % (f,c))
print(f"{f:.1f}fahrenheit={c:8.1f}celsius")
"""
# calculate the perimeter and area
import math
radius = float(input("please enter the radius:"))
perimeter=2 * math.pi * radius
print("%f is the perimeter" % perimeter)
print(f"{perimeter:f} is the perimeter")
print(f"{perimeter = :.2f}")

#judge whether it is a leap year
year = int(input("please enter the year:"))
#sth. I really don't figure out:maybe I don't know th rule（I COPY IT SOMEHOW...)
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0


#以上是截止2025.11.30的部分练习记录














