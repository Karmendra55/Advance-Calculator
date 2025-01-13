import math
import cmath

def NumberSystem(num, base, convert):
    num = str(num)
    if base==1:
        decimal = int(num, 2)
        if convert==2:
            print(f"The Binary Value is: {num}")
            return num
        elif convert==8:
            octal= oct(decimal)[2:]
            print(f"The Octal Value of {num} is: {octal}")
            return octal
        elif convert==10:
            print(f"The Decimal Value of {num} is: {decimal}")
            return decimal
        elif convert==16:
            hexa = hex(decimal)[2:].upper()
            print(f"The Hexa Value of {num} is: {hexa}")
            return hexa
        else:
            print("Incorrect Base has been Entered.")
            return None
    elif base==2:
        decimal = int(num, 8)
        if convert==2:
            binary = bin(decimal)
            print(f"The Binary Value of {num} is: {binary}")
            return binary
        elif convert==8:
            print(f"The Octal Value of {num} is: {num}")
            return num
        elif convert==10:
            print(f"The Decimal Value of {num} is: {decimal}")
            return decimal
        elif convert==16:
            hexa = hex(decimal)[2:].upper()
            print(f"The Hexa value of {num} is: {hexa}")
            return hexa
        else:
            print("Incorrect Base has been Entered.")
            return None
    elif base==3:
        decimal = int(num)
        if convert==2:
            binary=bin(decimal)
            print(f"The Binary Value of {num} is: {binary}")
            return binary
        elif convert==8:
            octal = oct(decimal)[2:]
            print(f"The Octal Value of {num} is: {octal}")
            return octal
        elif convert==10:
            print(f"The Decimal Value of {num} is: {num}")
            return num
        elif convert==16:
            hexa = hex(decimal)[2:].upper()
            print(f"The Hexa value of {num} is: {hexa}")
            return hexa
        else:
            print("Incorrect Base has been Entered.")
            return None
    elif base==4:
        decimal= int(num, 16)
        if convert==2:
            binary=bin(decimal)
            print(f"The Binary Value of {num} is: {binary}")
            return binary
        elif convert==8:
            octal = oct(decimal)[2:]
            print(f"The Octal Value of {num} is: {octal}")
            return octal
        elif convert==10:
            print(f"The Decimal Value of {num} is: {decimal}")
            return decimal
        elif convert==16:
            print(f"The Hexa value of {num} is: {num}")
            return num
        else:
            print("Incorrect Base has been Entered.")
            return None
    else:
        print(f"The Entered Base Is Wrong.")
        return None

def Trigonometry(angle, op):
    angle_rad = math.radians(angle)
    sine = math.sin(angle_rad)
    cosine = math.cos(angle_rad)
    tangent = math.tan(angle_rad)
    if op==1:
        print(f"Sine Value of {angle_rad} is: {sine}")
        return 'Sin', sine
    elif op==2:
        print(f"Cosine Value of {angle_rad} is: {cosine}")
        return 'Cos', cosine
    elif op==3:
        print(f"Tangent of {angle_rad} is: {tangent}")
        return 'Tan', tangent
    elif op==4:
        sine_Inverse = math.degrees(math.asin(sine))
        print(f"Inverse of Sine: {sine_Inverse}")
        return 'Sin Inverse', sine_Inverse
    elif op==5:
        cosine_Inverse = math.degrees(math.acos(cosine))
        print(f"Inverse of Cosine: {cosine_Inverse}")
        return 'Cos Inverse', cosine_Inverse
    elif op==6:
        Tangent_Inverse = math.degrees(math.atan(tangent))
        print(f"Inverse of Tangent: {Tangent_Inverse}")
        return 'Tan Inverse', Tangent_Inverse
    else:
        print("Value Entered is Wrong.")
        return None, None

def Hyperbolic(angle, op):
    angle_rad = math.radians(angle)
    if op==1:
        sine = math.sinh(angle)
        sineh = math.sinh(angle_rad)
        print(f"Hyperbolic Value of Sin is: {sine}")
        print(f"Hyperbolic Value of Sin in radian is: {sineh}")
        return 'Sinh', sine
    elif op==2:
        cosine = math.cosh(angle)
        cosineh = math.cosh(angle_rad)
        print(f"Hyperbolic Value of Cos is: {cosine}")
        print(f"Hyperbolic Value of Cos in radian is: {cosineh}")
        return 'Cosh', cosine
    elif op==3:
        tangent = math.tanh(angle)
        tangenth = math.tanh(angle_rad)
        print(f"Hyperbolic Value of Tan is: {tangent}")
        print(f"Hyperbolic Value of Tan in radian is: {tangenth}")
        return 'Tanh', tangent
    else:
        print("The Entered Value is Wrong.")
        return None, None