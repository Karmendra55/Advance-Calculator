def logic(num1, num2, x, condition, check):
    max_num=max(num1, num2)
    min_num=min(num1, num2)
    if check=="==":
        if condition=="and":
            if(max_num==x and min_num==x):
                print(f"The Entered Number {x} is equal to both {num1} and {num2}")
                return True, '==', '=='
            else:
                print(f"The Entered Number {x} is not equal to both or one of the numbers {num1}, {num2}")
                return False, '==', '=='
        elif condition=="or":
            if(max_num==x or min_num==x):
                print(f"The Entered Number {x} is equal to one of the numbers {num1}, {num2}")
                return True, '==', '=='
            else:
                print(f"The Entered Number {x} is not equal to both the numbers {num1}, {num2}")
                return False, '==', '=='
        elif condition=="not":
            if (not(max_num==x)):
                print(f"The Entered Number {x} is not equal to the number {max_num}")
                y1=True
            elif(not(max_num!=x)):
                print(f"The Entered Number {x} is equal to the number {max_num}")
                y1=False 
            elif (not(min_num==x)):
                print(f"The Entered Number {x} is not equal to the number {min_num}")
                y2=True
            elif (not(min_num!=x)):
                print(f"The Entered Number {x} is equal to the number {min_num}")
                y2=False
            return bool(y1 and y2), '==', '!='
        else:
            print("The Entered Condition is Wrong.")
            return None, None, None
    elif check=="><":
        if condition=="and":
            if(max_num>x and min_num<x):
                print(f"The Entered Number {x} is between {min_num} and {max_num}")
                return True, '>', '<'
            else:
                print(f"The Entered Number {x} is not between {min_num} and {max_num}")
                return False, '>', '<'
        elif condition=="or":
            if(max_num>x or min_num<x):
                print(f"The Entered Number {x} is satisfying one condition {min_num} or {max_num}")
                return True, '>', '<'
            else:
                print(f"The Entered Number {x} is not satisfying any condition {num1}, {num2}")
                return False, '>', '<'
        elif condition=="not":
            if (not(max_num>x and min_num<x)):
                print(f"The Entered Number {x} is not satisfying the condition.")
                return False, ">", "<"
            elif (not(max_num>x or min_num<x)):
                print(f"The Entered Number {x} is satisfying atleast one condition.")
                return "Maybe", ">", "<"
            else:
                print(f"The Entered Number {x} is satisfying the condition.")    
                return True, ">", "<"
        else:
            print("The Entered Condition is Wrong.")
            return None, None, None
    elif check==">=<":
        if condition=="and":
            if(max_num>=x and min_num<=x):
                print(f"The Entered Number {x} is between or at one Border of {min_num} and {max_num}")
                return True, '>=', '<='
            else:
                print(f"The Entered Number {x} is not between or at the Border of {min_num} and {max_num}")
                return False, '>=', '<='
        elif condition=="or":
            if(max_num>=x or min_num<=x):
                print(f"The Entered Number {x} is between atleast one condition or at one border {min_num} or {max_num}")
                return True, '>=', '<='
            else:
                print(f"The Entered Number {x} is not between atleast one condition nor at any border {min_num} or {max_num}")
                return False, '>=', '<='
        elif condition=="not":
            if (not(max_num>=x and min_num<=x)):
                print(f"The Entered Number {x} is not satisfying the condition nor at border.")
                return True, '>=', '<='
            elif (not(max_num>=x or min_num<=x)):
                print(f"The Entered Number {x} is satisfying atleast either one condition or maybe at one border.")
                return 'Maybe', '>=', '<='
            else:
                print(f"The Entered Number {x} is satisfying the condition or maybe at one border.")
                return False, '>=', '<='    
        else:
            print("The Entered Condition is Wrong.")
            return None, None, None
    else:
        print("The Operations are Wrongly Entered, Please Carefully Enter the Operator.")   
        return None, None, None             