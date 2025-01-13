def Operator(num1, num2, op):
    if op=='+':
        print(f"Sum of {num1} & {num2} is: {num1+num2}")
        return num1+num2
    elif op=='-':
        print(f"Difference between {num1} & {num2} is: {num1-num2}")
        return num1-num2
    elif op=='*':
        print(f"Multipling {num1} & {num2} is: {num1*num2}")
        return num1*num2
    elif op=='/':
        if num2!=0:
            print(f"Division of {num1} & {num2} is: {num1/num2}")
            return num1/num2
        else:
            print(f"Denomonator Must Not Be Zero.")
            return 0
    elif op=='%':
        print(f"Modulo of {num1} & {num2} is: {num1%num2}")
        return num1%num2
    elif op=="**":
        print(f"Power of {num1} and {num2} is: {num1**num2}")
        return num1**num2
    elif op=='//':
        print(f"Floor Division of {num1} & {num2} is: {num1//num2}")
        return num1//num2
    else:
        print("Wrong Operator Entered.")
        return None