def Assign(num1, num2, op):
    num3=num1
    if op=='=':
        num1=num2
        print(f"{num3} is now equals to {num2}: a={num1} and b={num2}")
        return num1
    elif op=="+=":
        num1+=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=="-=":
        num1-=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=="*=":
        num1*=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=="/=":
        num1/=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=="%=":
        num1%=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=="//=":
        num1//=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=="**=":
        num1**=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=='&=':
        num1=int(num1)
        num2=int(num2)
        num1&=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=="|=":
        num1=int(num1)
        num2=int(num2)
        num1|=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=="^=":
        num1=int(num1)
        num2=int(num2)
        num1^=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op==">>=":
        num1=int(num1)
        num2=int(num2)
        num1>>=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op=="<<=":
        num1=int(num1)
        num2=int(num2)
        num1<<=num2
        print(f"The value of {num3} is now {num1}")
        return num1
    elif op==":=":
        num1=int(num1)
        num2=int(num2)
        print(f"The value of {num3} is now",num1:=num2)
        return num1
    else:
        print("Wrong Operator Entered.")
        return None