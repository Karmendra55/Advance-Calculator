import math
import numpy as np
import scipy
import sympy
import scipy.stats
import random, string

def Statistics(data, pick):
    if pick==1:
        mean = np.mean(data)
        print(f"The mean of {data} is: {mean}")
        return "Mean", mean
    elif pick==2:
        median = np.median(data)
        print(f"The median of {data} is: {median}")
        return "Median", median
    elif pick==3:
        mode = scipy.stats.mode(data)
        print(f"The Mode of {data} is: {mode.mode[0]} (Frequency: {mode.count[0]})")
        return "Mode", mode
    elif pick==4:
        range_value = np.ptp(data)
        print(f"The Range of {data} is: {range_value}")
        return "Range", range_value
    elif pick==5:
        variance = np.var(data)
        print(f"The Variance of {data} is: {variance}")
        return "Variance", variance
    elif pick==6:
        std = np.std(data)
        print(f"The Standard Deviation is: {std}")
        return "Standard Deviation", std
    else:
        print("Wrong Entered Value.")
        return None, None
        

def Area(Shape, a, b=0, c=0, d=0, e=0):
    if Shape==1:
        area = a**2
        Perimeter = 4*a
        print(f"The Area and Perimeter of Square with value {a} is: {area} and {Perimeter}")
        return area, Perimeter
    elif Shape==2:
        area = a*b
        Perimeter = 2*(a+b)
        print(f"The Area and Perimeter of Rectangle with value {a},{b} is: {area} and {Perimeter}")
        return area, Perimeter
    elif Shape==3:
        area = (1/2)*a*b
        Perimeter = c+d+e
        print(f"The Area and Perimeter of Triangle with value {a,b} and {c,d,e} is: {area} and {Perimeter}")
        return area, Perimeter
    elif Shape==4:
        area = math.pi*(a**2)
        Circumference = 2*(math.pi)*a
        print(f"The Area and Circumference of Circle with value {a} is: {area} and {Circumference}")
        return area, Circumference
    else:
        print("Wrong Entered Shape.")  
        return None, None  

def Volume(Shape, a, b=0, c=0, d=0):
    if Shape==1:
        volume = a**3
        surface = 6*(a**2)
        print(f"The Volume and Surface Area of Cube with value {a} is: {volume} and {surface}")
        return volume, surface
    elif Shape==2:
        volume = a*b*c
        surface = (2*a*b)+(2*b*c)+(2*c*a)
        print(f"The Volume and Surface Area of Prism with value {a,b,c} is: {volume} and {surface}")
        return volume, surface
    elif Shape==3:
        volume = (4/3)*(math.pi)*(a**3)
        surface = 4*(math.pi)*(a**2)
        print(f"The Volume and Surface Area of Sphere with value {a} is: {volume} and {surface}")
        return volume, surface
    elif Shape==4:
        volume = (math.pi)*(a**2)*b
        surface = [(2*(math.pi)*(a**2))+(2*(math.pi)*a*b)]
        print(f"The Volume and Surface Area of Cylinder with value {a,b} is: {volume} and {surface}")
        return volume, surface
    elif Shape==5:
        volume = (1/3)*(math.pi)*(a**2)*b
        slant = math.sqrt(a**2 + b**2)
        surface = math.pi*a*(a+slant)
        print(f"The Volume and Surface Area of Cone with value {a,b} is: {volume} and {surface}")
        return volume, surface
    elif Shape==6:
        volume = ((1/3)*a)*b
        surface = a + (1/2)*c*d
        print(f"The Volume and Surface Area of Pyramid with value {a} is: {volume} and {surface}") 
        return volume, surface
    else:
        print("Wrong Entered Shape.")   
        return None, None
    
def Principal_Interest(choose, find, a, b, c):
    if choose==1: #Simple Interest
        if find==1: #Interest Rate
            Simple_Interest=(a*b*c)/100
            Final_Amount= a+Simple_Interest
            print(f"The Simple Interest will be: {Simple_Interest:.2f}")
            print(f"The Final Amount will be: {Final_Amount:.2f}")
            return "Simple", Final_Amount
        elif find==2:
            Principal_Amt=(a*100)/b*c
            print(f"The Principal Amount will be: {Principal_Amt:.2f}")
            return "Simple", b
        elif find==3:
            Rate=(a*100)/b*c
            print(f"The Rate will be: {Rate:.2f}%")
            return "Simple", b
        elif find==4:
            Time=(a*100)/b*c
            print(f"The Time(in years) wil be: {Time:.2f}")
            return "Simple", b
        else:
            print("Wrong Entries has been entered.")
            return None, None
    
    elif choose==2: #Compund Interest
        if find==1: #Interest Rate
            Final_Amount = a * (1+(b/100))**c
            Compound_Interest = Final_Amount - a
            print(f"The Compound Interest will be: {Compound_Interest:.2f}")
            print(f"The Final Amount will be: {Final_Amount:.2f}")
            return "Compound", Final_Amount
        elif find==2:
            Principal_Amt= a/((1+b/100)**c-1)
            print(f"The Principal Amount will be: {Principal_Amt:.2f}")
            return "Compound", Principal_Amt+a
        elif find==3:
            Rate=((a/b)+1)** (1/c)-1
            print(f"The Rate will be: {b*100:.2f}%")
            return "Compound", a+b
        elif find==4:
            Time=math.log((a/b)+1)/ math.log(1+c/100)
            print(f"The Time(in years) wil be: {Time:.2f} years")
            return "Compound", a+b
        else:
            print("Wrong Entries has been entered.")
            return None, None
    
    else:
        print("Wrong Entry.")
        return None, None
        
def Random_Op(choice, a=0, b=0, itt=0, seq=0):
    if choice==1:
        num1=random.randint(0, 10000)
        num2=random.randint(0, 10000)
        print(f"The Random Numbers are: {num1} and {num2}")
        return num1,num2
    elif choice==2:
        random_str= ''.join(random.choices(string.ascii_letters + string.digits, k=(random.randint(8,25))))
        print(f"Random Password is '{random_str}'.")
        return random_str
    elif choice==3:
        if sympy.isprime(a):
            print(f"{a} is a prime number.")
            return "Prime"
        else:
            print(f"{a} is not a prime number.")
            return "Not a Prime"
    elif choice==4:
        print("The Sequence is: ")
        if seq==1: #(a^n)
            for i in range(0, itt):
                s = (a**b)
                print(s, end=" ")
                b=b+1
        elif seq==2: #(a^n)-1    
            for i in range(0, itt):
                s = (a**b)-1
                print(s, end= " ")
                b=b+1
        elif seq==3: #((a^n)/a)
            for i in range(0, itt):
                s = ((a**b)/a)
                c = (a**b)
                d = a
                print(f"{c}/{d}", end=" ")
                b=b+1
        elif seq==4: #(a+n/a-n)
            for i in range(0, itt):
                s = [(a+b)/a-b]
                c = (a+b)
                d = (a-b)
                print(f"{c}/{d}", end=" ")
                b=b+1
        elif seq==5: #(a+n)/n
            for i in range(0, itt):
                s = (a+b)/b
                c=a+b
                d=b
                print(f"{c}/{d}", end=" ")
                b=b+1
        elif seq==6: #(a*a+n)/n
            for i in range(0, itt):
                s = (a*a+b)/b
                c=(a*a+b)
                d=b
                print(f"{c}/{d}", end=" ")
                b=b+1
        elif seq==7: #(a*a-n)/n
            for i in range(0, itt):
                s = (a*a-b)/b
                c = (a*a-b)
                d = b
                print(f"{c}/{d}", end=" ")
                b=b+1
        elif seq==8: #a/n
            for i in range(0, itt):
                s = a/b
                c = a
                d = b
                print(f"{c}/{d}", end=" ")
                b=b+1
        elif seq==9: #a*n
            for i in range(0, itt):
                s = a*b
                print(s, end=" ")
                b=b+1
        elif seq==10: #a+n
            for i in range(0, itt):
                s = a+b
                print(s, end=" ")
                b=b+1
        elif seq==11: #a-n
            for i in range(0, itt):
                s = a-b
                print(s, end=" ")
                b=b+1
        elif seq==12: #(a*a)/(n*n)
            for i in range(0, itt):
                s = [(a*a)/(b*b)]
                c = a*a
                d = b*b
                print(f"{c}/{d}", end=" ")
                b=b+1
        else:
            print("Sequence Not Available Yet.")
    else:
        print("Wrong Choice Entered.")