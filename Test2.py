# for i in range (1,5):
#     print(i)
#     if(i == 3):    # if(i == 3):
#         break      # break
#
# else:
#     print("I am Exhausted !")
# print("I am in the Loop !")


# l = [1,2,3,4,5,6,7,8,9,10,"Prince","Caspian",'A','L','E','X','A']
# for i in l:
#     print(i,end = " ")      # print(i);


# l = [1,2,3,4,5,6,7,8,9,10,"Prince","Caspian",'A','L','E','X','A']
# for i in range(len(l)):
#     print(i)


# l = [1,2,3,4,5,6,7,8,9,10,"Prince","Caspian",'A','L','E','X','A']
# for i in range(len(l)):
#     # print(l[i])
#     print(l[i],end = " ")


# t = (179,"Prince","Caspian",'P','C','A')
# for i in t:
#     print(t)

# s = "Hello ! Prince Kumar "
# for i in s:
#     print(s)

# s = "Hello ! Prince Kumar "
# for i in range(len(s)):
#     print(s)

# d = dict()
# d["SRN"] = "R21DE179"
# d["Name"] = "Prince Kumar"
# d['S'] = 179
# for i in d:
#     print("Key = {0} & Value = {1}".format(i,d[i]))


# n1 = int(input("Enter the Number : "))
# n2 = int(input("Enter the Number : "))
# n3 = int(input("Enter the Number : "))
# if(n2 >= n1):
#     n1 = n2
# if(n3 >= n1):
#     n1 = n3
# print("Greatest Number :",n1)


# str = input("Enter the String / Number : ")
# string = str[::-1]
# print(str,"Reverse",string)
# if(str == string):
#     print(str,"Palindrome Number !")
# else:
#     print(str,"Not Palindrome Number !")


# n, f = int(input("Enter the Number : ")),0
# for i in range(1,n+1):
#     if(n % i == 0):
#         f += 1      # f = f + 1
# if(f == 2):
#     print(n,"Prime Number !")
# else:
#     print(n,"Not Prime Number !")


# num = int(input("Enter the Numnber : "))
# fact = 1
# if(num != 0):
#     for i in range(1,num + 1):
#         fact = fact * i
#     print(num,"!=",fact)
# else:
#     print("Invalid Input !")


# num = int(input("Enter the Number : "))
# a = 0
# b = 1
# if(num != 0):
#     print(a)
#     print(b)
#     for i in range(num):
#         c = a + b
#         print(c)
#         a = b
#         b = c


# num = int(input("Enter the Number : "))
# rem = 0
# sum = 0
# temp = num
# if(num != 0):
#     rem = temp % 10
#     sum = sum + rem ** 3
#     temp = temp // 10
# if(num == sum):
#     print(num,"ArmStrong Number !")
# else:
#     print(num,"Not ArmStrong Number !")



# num1 = int(input("Enter the 1 Number : "))
# num2 = int(input("Enter the 2 Number : "))
# num3 = int(input("Enter the 3 Number : "))
# sum = num1 + num2 + num3
# avg = num1 + num2 + num3 / 3
# print(sum)
# print(avg)


# i = 0
# # str = "Python"
# str = "Prince"
# while(i < len(str)):
#     # print(i)
#     # break
#     if(str[i] == 'r'):      # if(str[i] == 't'):
#         i += 1
#         break
#     print("Current Letter : ",str[i])
#     i += 1
#
#
# for val in "Caspian Prince Kumar !":
#     if(val == 'i'):
#        print(i)


# import numpy
# n = numpy.array([10,20,30,40])
# print(n)


# n1 = numpy.array([10,20,30,40],[50,60,70,80])
# print(type(n1))


# arr = [5]
# n = int(input("Enter the Elements : "))
# for i in range(0,5):
#     list = int(input())
#     arr.append(list)
# print(arr)
    #arr.pop()
    #arr.sort(True)


# write a program to a generic number, generic the calender of the year, compute the q.E all possible equ., generic in fibonacci series,
# armstrong number.
# anny. fun. square root of and square of the Number.

# power of number using recursion.
# sort the element using lambda function.
# compute the number of occurances the odd number in the given number(7,6,8,5,4).


# import Calender
# y = int(input("Enter the Year : "))
# m = int(input("Enter the Month : "))
# # print("Calender : ", Calender.month(y, m))

# import random
# print(random.randint(0, 99999))

# import cmath
#
# n = int(input("Enter the Number : "))
# dis_val = cmath.sqrt(n)
# print("Square Root of the Number :",dis_val)

# a = int(input(" "))
# s = lambda n : n ** 2
# print("Square : ",s)
# sq = lambda n : math.sqrt(n)
# print("Square : Root : ",sq)

















