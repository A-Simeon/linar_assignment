print("quadratic equation formular")
import math
a = input(input("Enter the coefficient a: "))
b = input(input("Enter the coefficient b': "))
c = input(input("Enter the coefficient c: "))

"""" In python when calculating quadratic equation the following condition must be consider,
The roots of a quadratic equation can be classified as: 
*  If b*b > 4*a*c, then roots are real and different

*  If b*b == 4*a*c, then roots are real, and both roots are the same.

*  If b*b < 4*a*c, then roots are complex"""

dis= b ** 2 - 4 * a * c

"""check condition for the discriminant if is positive, negative or zero as stated earlier from line 7 to 13"""

if dis> 0:
    root1 = (-b + math.sqrt(dis)) / (2 * a)
    root2 = (-b - math.sqrt(dis)) / (2 * a)
    print("Two real roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)
    
elif dis == 0:
    root1 = -b / (2 * a)
    print("One real root:")
    print("Root 1:", root1)
    
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(dis)) / (2 * a)
    print("Complex roots:")
    print("Root 1:", real_part, "+", imaginary_part, "i")
    print("Root 2:", real_part, "-", imaginary_part, "i")