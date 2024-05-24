                                                # Lab Experiments
                                                    # Part - A
""" 
1. Demonstrate runtime reading of Strings.
            i) Illustrate the concept of String Slicing.
            ii) Also demonstrate a minimum of 5 functions defined on Strings.
"""

str = input("Enter a String : ")
print(str)
print(str[1:5])
print(str[-1])
print(str[5:-1])
print(str[1:8:2])

print(len(str))
print(str.upper())
print(str.lower())
print(str.count('p'))
print(str.title())

print(str.swapcase())
print(str.find('n'))
print(str.startswith('hi'))
print(str.endswith('byy'))
print(str.capitalize())

"""
2. Write a program to add two integers and print the result on the screen. Accept the values at runtime.
"""

num1 = int(input("Enter a First Number : "))
num2 = int(input("Enter a Second  Number : "))
result = num1 + num2
print("Addition of Two Number : ",result)

"""
3. Demonstrate the usage of math and cmath module.(For Ex. Program to find the roots of a Quadratic Equation)
"""

import cmath
a = int(input("Enter a number for A : "))
b = int(input("Enter a number for B : "))
c = int(input("Enter a number for C : "))
# calculating discriminant using formula.
dis = b * b - 4 * a * c
dis_val = cmath.sqrt(dis)
# checking condition for discriminant.
if dis > 0:
    print("The Root are Real and Distinct.")
    print((-b + dis_val) / (2 * a))
    print((-b - dis_val) / (2 * a))
elif(dis == 0):
    print("The Root are Real and Equal.")
    print(-b / (2 * a))
# when discriminant is less than 0.
else:
    print("The Root are Imaginary and Complex.")
    print(-b / (2 * a), " +i", dis_val)
    print(-b / (2 * a), " -i", dis_val)

"""
4. Illustrate the usage of files with the help of different functions defined on Files(such as write, read(demonstrate all four forms), open, and close(use both the forms of closing a file)
"""

# Write the File.
file = open("Operation.txt",'w')
file.write("Reva university in bangalore.")
file.close()

# Read the File.
file = open("Operation.txt",'r')
data = file.read()
print(data)
file.close()

# READING NUMBER OF LINES IN A FILE.

file = open("Operation.txt", "a")
data = file.writelines("\n python programming \n perl programming \n web programming")
file.close()

# Read the File.
file = open("Operation.txt",'r')
data = file.read()
print(data)
print(len(data))
file.close()

"""
5. Write a program to find the largest of two numbers.
6. Write a program to find the biggest of three numbers.
"""

num1 = int(input("Enter the 1 no : "));
num2 = int(input("Enter the 2 no : "));
if(num1 > num2):
    print(num1,"is a Largest.")
else:
    print(num2,"is a Largest.")


num1 = int(input("Enter the 1 no : "));
num2 = int(input("Enter the 2 no : "));
num3 = int(input("Enter the 3 no : "));
if(num1 > num2):
    print(num1,"is a Biggest.")
elif(num2 > num3):
    print(num2,"is a Biggest.")
else:
    print(num3,"is a Biggest.")

"""
7. Design a menu driven program to check whether the number is : 
        i)A perfect number or not.
        ii)Armstrong number or not.
        iii)Palindrome or not.
"""

while(True):
    print("1.) Perfect Number or Not.")
    print("2.) ArmStrong Number or Not.")
    print("3.) Paliondrome Number or Not.")
    print("4.) Exit.")
    choice = int(input("Enter Your Choice : "))
    if(choice == 1):
        # perfect number : 6, 28, 496
        num = int(input("Enter a Number : "))
        sum = 0
        for i in range(1, num):
            if(num % i == 0):
                sum = sum + i
                print(i," ")
        if(sum == num):
            print(num,"is Perfect Number.")
        else:
            print(num,"is not a Perfect Number.")
    elif(choice == 2):
        # all are armstrong number : 153, 370, 371, 407, 1634 = no of digit : (4)
        # 153 = no of digit = (3) : 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3
        num = int(input("Enter a Number : "))
        temp = num
        sum = 0
        rem = 0
        while(temp != 0):
            rem = temp % 10
            sum = sum + rem ** 3
            temp = int(temp / 10)
        if(num == sum):
            print(num,"is a Armstrong.")
        else:
            print(num, "is not a Armstrong.")
    elif(choice == 3):
        str = input("Enter a String : ")
        string = str[::-1]
        print(str,"Reverse is",string)
        if(string == str):
            print(str,"is a Palindrome.")
        else:
            print(str,"is not a Palindrome.")
            
    elif(choice == 4):
        print("Exit")
        break
    else:
        print("Invalid Choice !")

"""
8. Show the different operations defined on Lists, Tuples and Dictionaries
"""

list = ['python','java','perl','PHP','C','ruby']
list.insert(4,'C++')
list.append('Program')
list.remove('C++')
list.extend("Programming")
print(list)
list.clear()
print(list)

tup = (10,20,30)
a,b,c = tup
print(a)
print(b)
print(c)

tup = ('Alex','Prince','Caspian','Sinha')
print(tup)
print(tup[3])
print(tup[1:3])
print(tup * 3)

tup = (10,20)
tup = a + b
a = b
b = tup

print(a)
print(b)
print(type)
print(tup)
print(type(tup))

dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'july', 8: 'August',9: 'September', 10: 'October', 11: 'November', 12: 'December'}
dict.update({13: 'Alex'})
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get(9))
print(dict[1][0])

"""
9. Write a program to find the factorial of a number using functions and without using functions. Accept the input at runtime.
"""

def fact(num):
    fact = 1
    if(num > 0):
        for i in range(1, num + 1):
            fact = fact * i
        return fact
    else:
        print("Invalid Input !")

num = int(input("Enter a Number : "))
print(num, "! =", fact(num))

"""
10. Demonstrate the i) Designing of a class ii) Creation of Object of that class iii) accessing the methods and instance variables in the class. The student is at the liberty of choosing their own Description of the object for designing the class.
"""

# Class Creation.
class Human:
    attr1 = "Mammal"
    attr2 = "Human"
    def fun(self):
        print(f"I am a {self.attr1}")
        print(f"I am a {self.attr2}")
# Object Creation.
Prince = Human()
#Accessing the methods and Insatnce Variable of that Class.
print(Prince.attr1)
print(Prince.attr2)
Prince.fun()

