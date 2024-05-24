import cmath
while(True):
    print("\na.) Display Reverse-Palindrome.")
    print("b.) Display Armstrong.")
    print("c.) Display Factorial.")
    print("d.) Display Fibonacci.")
    print("e.) Display Perfect No.")
    print("f.) Display Perfect Square.")
    print("g.) Display Square Root.")
    print("h.) Display Prime No.")
    print("i.) Display Swap the Value.")
    print("j.) Display Largest No.")
    print("k.) Display LCM.")
    print("l.) Display GCD.")
    print("m.) Display Odd And Even No.")
    print("n.) Display Roots of Quadratic Equation")
    print("o.) Display Week Day.")
    print("s.) Check Vowel/Consonant/White Spaces.")
    print("p.) Exit.\n")
    choice = input("Enter Your Choice : ")
    if(choice == 'a'):
        # Reverse Number : 123, 321, 456, 654
        # Palindrome Number : 121, 101, 111
        # String Palindrome Words : malayalam, dad, level, mom, anna, civic, kayak, madam, noon, racecar, wow, tenet, solos, rotor, radar, redder, refer, stats, rotator.
        """
        str = input("Enter a String & Number : ")
        string = str[::-1]
        print(str,"Reverse is",string)
        if(str == string):
            print(str,"is a Palindrome.")
        else:
            print(str,"is not a Palindrome.")
        """
        num = int(input("Enter a Number : "))
        temp = num
        rev = 0
        while(temp != 0):
            rem = temp % 10
            rev = rev * 10 + rem
            temp = int(temp / 10)
            print(num,"Reverse is",rev)
        if(num == rev):
            print(num,"is a Palindrome.")
        else:
            print(num,"is not a Palindrome.")
    elif(choice == 'b'):
        # all are armstrong number : 153, 370, 371, 407, 1634 = no of digit : (4)
        # 153 = no of digit = (3) : 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3
        num = int(input("Enter a Number : "))
        temp = num
        sum = 0
        rem = 0
        while (temp != 0):
            rem = temp % 10
            sum = sum + rem ** 3    # sum = sum + rem * rem * rem
            temp = int(temp / 10)
        if(num == sum):
            print(num,"is a Armstrong.")
        else:
            print(num, "is not a Armstrong.")
    elif(choice == 'c'):
        num = int(input("Enter a Number : "))
        fact = 1
        if (num >= 0):
            for i in range(1, num + 1):
                fact = fact * i
                print(num, "! =", fact)
        else:
            print("Invalid Input !")
    elif(choice == 'd'):
        num = int(input("Enter a Number : "))
        if(num == 1):
            n1 = 0
            print("Fibonacci Series : ",n1,end = " ")
        else:
            n1 = 0
            n2 = 1
            print("Fibonacci Series : ",n1,n2,end = " ")
            for i in range(2,num):
                n3 = n1 + n2
                n1 = n2
                n2 = n3
                print(n3,end = " ")
    elif(choice == 'e'):
        # perfect number : 6, 28, 496
        num = int(input("Enter a Number : "))
        sum = 0
        for i in range(1,num):
            if(num % i == 0):
                sum = sum + i
                print(i," ")
        if(sum == num):
            print(num,"is Perfect Number.")
        else:
            print(num,"is not a Perfect Number.")
    elif(choice == 'f'):
        num = int(input("Enter a Number : "))
        square = cmath.sqrt(num)
        if(square ** 2 == num):
            print(num,"is a Perfect Square.")
        else:
            print(num,"is not a Perfect square.")
    elif(choice == 'g'):
        num = int(input("Enter a Integer Number : "))
        num1 = float(input("Enter a Float Number : "))
        if(num >= 1 and num1 >= 1):
            print("Square Root of Integer Number : ", num, "is", cmath.sqrt(num))
            print("Square Root of Float Number : ", num1, "is", cmath.sqrt(num1))
        else:
            print("Invalid Input Number !")
    elif(choice == 'h'):
        """
        start = int(input("Enter a Start Number : "))
        last = int(input("Enter a Last Number : "))
        print("Prime numbers between", start, "and", last, "are : ")
        for num in range(start, last + 1):
            if (num >= 1):
                for i in range(2, num):
                    if (num % i) == 0:
                        break
            else:
                print(num)
        for num in range(2, num):
            prime = True
            for i in range(2, num):
                if (num % i == 0):
                    prime = False
                    if prime:
                        print(num)
        for num in range(2, num):
            if all(num % i != 0 for i in range(2, num)):
                print(num)
        """
        n = int(input("Enter the Number : "))
        flag = True
        if(n >= 1):
            for i in range(2, n):
                if (n % i == 0):
                    flag = False
                    break
        if flag:
            print(n,"is a Prime Number.")
        else:
            print(n,"is not a Prime Number.")
    elif(choice == 'i'):
        a = int(input("Enter the number A : "))
        b = int(input("Enter the number B : "))
        c = int(input("Enter the number C : "))
        print("Before Swap Value : ", a, b, c)
        # t = a;
        # a = b;
        # b = t;
        # a,b = b,a;
        a, b, c = b, c, a;
        print("After Swap Value : ", a, b, c);
    elif(choice == 'j'):
        num1 = int(input("Enter the 1st value : "));
        num2 = int(input("Enter the 2nd value : "));
        num3 = int(input("Enter the 3rd value : "));
        if(num1 > num2):
            {
                print(num1,"is a greater.")
            }
        elif(num2 > num3):
            {
                print(num2,"is a greater.")
            }
        else:
            {
                print(num3,"is a greater.")
            }
    elif(choice == 'k'):
        num1 = int(input("Enter a first number : "))
        num2 = int(input("Enter a second number : "))
        if(num1 > num2):
            l = num1
        else:
            l = num2
        while(True):
            if(l % num1 == 0 and l % num2 == 0):
                print("LCM of : ",l)
                break
            l = l + 1
    elif(choice == 'l'):
        m = int(input("Enter a Number : "))
        n = int(input("Enter a number : "))
        while(n != 0):
            r = m % n
            m = n
            n = r
        print("GCD of : ",m)
    elif(choice == 'm'):
        num = int(input("Enter the number : "))
        if(num % 2 == 0):
            {
                print(num,"Even Number.")
            }
        else:
            {
                print(num,"Odd Number.")
            }
    elif(choice == 'n'):
        a = int(input("Enter a number for A : "))
        b = int(input("Enter a number for B : "))
        c = int(input("Enter a number for C : "))
        # calculating discriminant using formula.
        dis = b * b - 4 * a * c
        dis_val = cmath.sqrt(dis)
        # checking condition for discriminant.
        if(dis > 0):
            print("The root are Real and Distinct.")
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
    elif(choice == 'o'):
        while(True):
            print("1.) Sunday\n2.) Monday\n3.) Tuesday\n4.) Wednesday\n5.) Thursday\n6.) Friday\n7.) Saturday\n8.) Exit")
            week = input("Enter Your Choice for Day : ")
            if(week == '1'):
                print("Sunday.")
            elif(week == '2'):
                print("Monday.")
            elif(week == '3'):
                print("Tuesday.")
            elif(week == '4'):
                print("Wednesday.")
            elif(week == '5'):
                print("Thursday.")
            elif(week == '6'):
                print("Friday.")
            elif(week == '7'):
                print("Saturday.")
            elif(week == '8'):
                print("Exit.")
                break
            else:
                print("Invalid Choice !")
    elif(choice == 's'):
        string = input("Enter Your String : ")
        vowel = 0
        consonant = 0
        for ch in string:
            if((ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U') or (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u')):
                vowel = vowel + 1
            else:
                consonant = consonant + 1
        print("Vowel in String : ", vowel)
        print("Consonant i String : ", consonant)
        print("Blank Sapce in String : ", string.count(' '))
    elif(choice == 'p'):
        print("Exit.")
        break
    else:
        print("Invalid Choice !")


