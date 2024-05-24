# def add(a,b):
#     c = a + b
#     return(c)
# print(add(10,20))


# list = [10,20,30]
# print(list)
# list1 = int(input("Enter the no : "))
# list.append(list1)
# print(list)


# n = int(input("Enter the Number : "))
# for x in range(n):
# for x in range(2,n):
# for x in range(2,n+1):
# for x in range(n):
#     print(x)
# else:
#     print("Very Good !")
#
# for x in range(n):
#     if(x == 3):     # if(x == 3): break # (if the loop will breaks, then else block will be not executed.)
#         break
#     print(x)
# else:
#     print("Very Good !")


# a = []
# # a1 = int(input("Enter the No : "))
# # a.append(a1)
# a.append(12)
# a.append(20)
# print(type(a))
# print(a)



a = [7,15,20,25,5,3]
print("Length of the Array : ", len(a))
prime = list() # prime = []
nonprime = list()
for j in range(0,len(a)):
    f = True
    for i in range(2, a[j] // 2 + 1):
        if(a[j] % i== 0):
            f = False
            break
    if(f == True):
        prime.append(a[j])
    else:
        nonprime.append(a[j])

print("Prime : ", end = " ")
for x in prime:
    print(x, end = " ")

print("\nNon-Prime : ", end = " ")
for y in nonprime:
    print(y, end = " ")










