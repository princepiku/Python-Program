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
elif dis == 0:
    print("The Root are Real and Equal.")
    print(-b / (2 * a))
# when discriminant is less than 0.
else:
    print("The Root are Imaginary and Complex.")
    print(-b / (2 * a), " +i", dis_val)
    print(-b / (2 * a), " -i", dis_val)
