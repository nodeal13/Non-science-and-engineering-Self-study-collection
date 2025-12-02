from webbrowser import open_new

num1 = 5
num1+=5
print(num1)


#occupid blanks to make then together
#change into string
titlle = "is the one"
numA = 1
oath="taylor swift is %s" % numA
print(oath)
"""
#change into int
%d
#change into float
%f
"""
"""
# calculate if you're healthy!(if elif else)
height = (float(input("please enter your height(m):")))
weight = (float(input("please enter your weight(kg):")))
bmi = weight/(height**2)
print(f"{bmi = :.2f}")
if 18.5<= bmi <24:
    print(("GREAT!!!"))
else:
    print("you should be doing more.")

# match n case
taylor_album = str(input("please tell me your favorite album of taylor swift:"))
match taylor_album:
    case "taylor_swift": screen = "debut!good!"
    case "fearless": screen = "in a storm in my best dress fearless"
    case "speak now": screen = "I was enchanted to meet you"
    case "red": screen = "forgetting him was like trying to know sb. you never met"
print("your taylor oath is:", screen )
"""
#segment function
x = float(input(" x= "))
if x>1:
    y = 3 * x - 5
elif x>= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f"{y = }")

x = float(input(" x= "))
if x>1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = x * 5 + 3
print(f"{y = }")

score = float(input("please enter your score:"))
if score >= 95:
    grade = "A"
elif score >=60:
    grade = "P"
else:
    grade = "F"
print(f"{grade = }")

#calculate the area of the triangle(or if it's not a real triangle)
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a+b>c and a+c>b and b+c>a:
    perimeter = a + b + c
   #sorry I just forget the formula for calculating the area haha..
    print(f'周长: {perimeter}')
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'面积: {area}')

else:
    print("dude it's not a TRUE triangle...")

#以上截止2025.12.02的练习记录

















