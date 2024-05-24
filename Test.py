"""
import array
import array as arr



dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'july', 8: 'August',9: 'September', 10: 'October', 11: 'November', 12: 'December'}
print(dict.keys())
print(dict.values())


str = input("Enter a String : ")
string = str[::-1]
print(str,"Reverse is",string)
if(string == str):
    print(str,"is a Palindrome.")
else:
    print(str,"is not a Palindrome.")


num = [1,2,3,4,5]
for item in num:
    print(item)


i = 0
while(i < len(num)):
    print(num[i])
    i = i + 1


i = 1
while(i <= 5):
    print(i * '*')
    i = i + 1


for i in range(10):
    print(i)


for i in range(1,11):
    print(i)


for i in range(1,10,2):
    print(i)


lst = [10,20,30]
for i in lst:
    print(i)
    # print(lst)

"""

# for i in range (9):
#     if(i > 3):
#         break
#         print(i)
#
#
# for i in range(9):
#     if(i > 3):
#         break
#     print(i)
#
#
# i = 1
# while(i < 6):
#     pass
#     i = i + 1
#
#
# str = "Caspian Prince"
# for i in str:
#     if(i == ' '):
#         continue
#     print(i)
#
#
# str = "CaspianPrince"
# for i in str:
#     if(i == 's'):
#         continue
#     print(i)
#
#
# a, b = 47, 45
# if(a < b):
#     pass
# else:
#     print("b < a")
#
#
# a, b, c = 25, 35, 50
# if(a > b or a > c):
#     print("Execute.")
# else:
#     print("Not Execute.")


"""
num = int(input("Enter a Number : "))
sum = 0
for i in range(1,num):
    sum = sum + num
    num = num + i
    print(sum)


def rev(str):
    return str[::-1]

str = input("Enter a Number : ")
print(str,"Reverse Number is : ",rev(str))


arr = [1,2,3,4,5,6]
print("Array Elements")
for i in range(0,len(arr)):
    print(arr[i],end = " ")


a = int(input("Enter the Size of Array : "))
n = list(map(int, input("Enter the Elements : ").strip().split()))
print(n)


arr = []
n = int(input("Enter the Elements : "))
for i in range(0,n):
    list = int(input())
    arr.append(list)
print(arr)


def LCM(num1,num2):
    if(num1 > num2):
        l = num1
    else:
        l = num2
    while(True):
        if(l % num1 == 0 and l % num2 == 0):
            break
        l = l + 1
    return l

num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
print("LCM of : ",LCM(num1,num2))


def GCD(m,n):
    while(n != 0):
        r = m % n
        m = n
        n = r
    return m

m = int(input("Enter a Number : "))
n = int(input("Enter a number : "))
print("GCD of : ",GCD(m,n))


arr = []
n = int(input("Enter the Size of Array : "))
for i in range(0,n):
    list = int(input("Enter the Elements : "))
    arr.append(list)
    arr.sort()
print(arr)



def max(n1, n2 = 120):
    if(n1 > n2):
        print(n1)
    else:
        print(n2)
print(max(12))


def display(*alex):
    print(alex)
    print(alex[0])
    print(alex[1])
    print(alex[2])
display(12,13,14)


def sum(*alex):
    print(alex[0])
    print(alex[1])
    sum1 = alex[0] + alex[1]
    return sum1
print(sum(10,20))



string = "good luck"
print(string)
print(len(string))
print("good luck " * 3)
#s = "good luck " * 3
#print(s)
print(string[::2])
print(string[::-1])
print(string.replace('o','u'))
print(string[:])
print(string[3:])
print(string[:9])
print(string[1:5])
print(string[0:9:2])

"""
