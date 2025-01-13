import math
import numpy as np
import cmath

def one(num, op):
    if op==1:
        print(f"The Square of {num} is: {num*num}")
        return num*num
    elif op==2:
        a=math.sqrt(num)
        print(f"The Square Root of {num} is {a}")
        return a
    elif op==3:
        print(f"The Cube of {num} is: {num*num*num}")
        return num*num*num
    elif op==4:
        a=math.cbrt(num)
        print(f"The Cube Root of {num} is: {a}")
        return a
    elif op==5:
        try:
            if num==0:
                raise ValueError
            else:
                a=1/num
        except ValueError:
            print("Value Error; Invalid Entry; We can not divide by 0.")
            return None
        print(f"The value of {num} in form of 1/num is {a}")
        return a
    elif op==6:
        a=math.exp(num)
        print(f"The Euler's Value of {num} is {a}")
        return a
    elif op==7:
        a=10**num
        print(f"The 10s Power of {num} is: {a}")
        return a
    elif op==8:
        a = math.factorial(int(num))
        print(f"The Factorial of {num} is: {a}")
        return a
    elif op==9:
        if num<0:
            a=abs(num)
            print(f"Sign Conversion of {num} is: {a}")
            return a
        elif num>0:
            a=num-(2*num)
            print(f"Sign Conversion of {num} is: {a}")
            return a
        else:
            print(f"Sign COnversion of {num} is {num}")
            return num
    else:
        print("Invalid Input!")
        return None
        
def two(num1, num2, op):
    if op==1:
        a=math.fmod(num1, num2)
        print(f"Mod of {num1} and {num2} is: {a}")
        return a
    elif op==2:
        a=math.log(num1, num2)
        print(f"Log of {num1} base {num2}: {a}")
        return a
    elif op==3:
        a=np.log(num1)/np.log(num2)
        print(f"ln of {num1} base {num2} is: {a}")
        return a
    elif op==4:
        a=(num1/num2)*100
        print(f"The Percentage of {num1} in respect to {num2} is: {a}")
        return a
    elif op==5:
        a=math.ceil(num1)
        b=math.ceil(num2)
        print(f"The Ceiling Values of {num1} and {num2} are: {a}, {b}")
        return (a,b)
    elif op==6:
        a=math.floor(num1)
        b=math.floor(num2)
        print(f"The Floor Values of {num1} and {num2} are: {a}, {b}")
        return (a,b)
    else:
        print("Invalid Input Entered.")
        return None

def three(num1, num2, op):
    if op==1:
        a=(num1)+(num2)
        print(f"Complex Addition is: {a}")
        return a
    elif op==2:
        a=(num1)-(num2)
        print(f"Complex Subtraction is: {a}")
        return a
    elif op==3:
        a=(num1)*(num2)
        print(f"Complex Multiplication is: {a}")
        return a
    elif op==4:
        try:
            if num2!=0:
                a=(num1)/(num2)
                print(f"Complex Division is: {a}")
                return a
        except ValueError:
            print("Zero Divison, The Denomenator must not be 0.")
            return None
    elif op==5:
        a=(num1.conjugate())
        b=(num2.conjugate())
        print(f"The Conjugates are: {a} and {b}")
        return (a,b)
    elif op==6:
        a=abs(num1)
        b=abs(num2)
        print(f"The Modulus are: {a} and {b}")
        return (a,b)
    elif op==7:
        a=cmath.phase(num1)
        b=cmath.phase(num2)
        print(f"The Phases are: {a} and {b}")
        return (a,b)
    elif op==8:
        a=cmath.polar(num1)
        b=cmath.polar(num2)
        print(f"The Exponential forms are: {a} and {b}")
        return (a,b)