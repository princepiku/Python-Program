"""
i = 1
while(i < 6):
    #pass
    print(i)
    i = i + 1

str = "Caspian Prince"
for i in str:
    if(i == ' '):
        continue
    print(i)

for i in range(9):
    if(i > 3):
        break
    print(i)
"""


str = "javaprogram"
for i in str:
    if(i == 'p'):
        continue
    print(i)


a, b = 47, 45
if(a < b):
    pass
else:
    print("b < a")


a, b, c = 25, 35, 50
if(a > b or a > c):
    print("Execute.")
else:
    print("Not Execute.")


num = int(input("Enter a Number : "))
sum = 0
for i in range(1,num):
    sum = sum + num
    print(sum)
    num = num + i
