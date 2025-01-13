def compare(num1, num2, op):
    if op=='==':
        if num1==num2:
            print(f"{num1} and {num2} are Equal.")
            return "True"
        else:
            print(f"{num1} and {num2} are Unequal.")
            return "False"
    elif op=='!=':
        if num1!=num2:
            print(f"{num1} and {num2} are Not Equal.")
            return "True"
        else:
            print(f"{num1} and {num2} are Similar.")
            return "False"
    elif op==">":
        if num1>num2:
            print(f"{num1} is greater then {num2}.")
            return "True"
        else:
            print(f"{num1} is not greater then {num2}.")
            return "False"
    elif op=="<":
        if num1<num2:
            print(f"{num1} is less then {num2}.")
            return "True"
        else:
            print(f"{num1} is not less then {num2}.")
            return "False"
    elif op==">=":
        if num1>=num2:
            print(f"{num1} is greater then or equal to {num2}.")
            return "True"
        else:
            print(f"{num1} is not greater then nor equal to {num2}.")
            return "False"
    elif op=="<=":
        if num1<num2:
            print(f"{num1} is less then or equal to {num2}.")
            return "True"
        else:
            print(f"{num1} is not less then nor equal to {num2}.")
            return "False" 
    else:
        print("Wrong Operator Entered.")
        return None