import Modules.Arithmatic as Arithmatic 
import Modules.Assignment as Assignment
import Modules.Comparsion as Comparsion
import Modules.Logical as Logical
import util.display as display
import Modules.Scientific as Scientific
import Modules.NumSys_Trignometry as NumSys_Trignometry
import Modules.Random_Operations as Random_Operations
import util.history as History

try:
    a,b = map(float, input("Please Enter the two initial Values: ").split())
    History.add_to_history(a, b, "changed")
except ValueError:
    print("The Entered Value(s) are incorrect, please Enter Two Numbers Only.")
    exit()
while True:
    display.display1()
    Action=int(input(""))
    try:
        if Action==9: 
            print("Thank You for Using this program to sort out the problems.")
            exit()
        elif Action not in range(0,6):
            raise ValueError
    except ValueError:
        print("Invalid Choice, Please Select Either (0-5 or 9).")
    if Action==0:
        display.more_display()
        Action=int(input(""))
        try: 
            if Action==11:
                try:
                    a,b= map(float, input("Enter The Two New Numbers: ").split())
                    History.add_to_history(a, b, "changed")
                except ValueError:
                    print("Value Error, Please Enter Only Two Numbers.")
                    break
            elif Action==6:
                display.display6()
                pick=int(input(""))
                if pick==1:
                    Choose=input("Would you like to enter the number or not? (yes, no): ")
                    if Choose=="no":
                        num=a
                    elif Choose=="yes":
                        num=float(input("Please Enter a New Number: "))
                    print("Enter The Number to pick the operation","--------------------------------------","1. Square, 2. Square Root, 3. Cube","4. Cube Root, 5. 1/x, 6. e^x","7. 10^x, 8. x!, 9. Sign Change","--------------------------------------",sep="\n")
                    opr=int(input(""))
                    c = Scientific.one(num, opr)
                    History.add_to_history_for_one_input(num, opr, c)
                elif pick==2:
                    print("Enter The Number to pick the operation","--------------------------------------","1. Mod, 2. Log, 3. ln","4. % , 5. Ceiling, 6. floor","--------------------------------------",sep="\n")
                    opr=int(input(""))
                    c = Scientific.two(a, b, opr)
                    History.add_to_history(a, b, opr, c)
                elif pick==3:
                    try:
                        a1, a2 = map(float, input("Enter The First Imaginary Part with the 'i' and with space: ").split())
                        b1, b2 = map(float, input("Enter The Second Imaginary Part same as you entered the First: ").split())
                    except ValueError:
                        print("The Entered Value(s) are incorrect, please Enter Complex Numbers Only. with the 'i'")
                        break
                    a=complex(a1,a2)
                    b=complex(b1,b2)
                    print("Enter The Number to pick the operation","--------------------------------------","1. '+', 2. '-', 3. '*'","4. '/' , 5. Conjugate, 6. Modulus","7. Phase, 8. Exponential","--------------------------------------",sep="\n")
                    opr=int(input(""))
                    c = Scientific.three(a, b, opr)
                    History.add_to_history(a, b, opr, c)
                else:
                    print("Wrong Choice Picked.")
                    break
                    
            elif Action==7:
                display.display7()
                pick=int(input(""))
                if pick==1:
                    print("Pick a Base To Enter the Number at","-------------------------","1. Binary, 2. Octal","3. Decimal, 4. HexaDecimal","-------------------------",sep="\n")
                    Base=int(input(""))
                    Num=(input("Enter a Number: "))
                    convert=int(input("Enter the Conversion Base(2, 8, 10, 16): "))
                    c = NumSys_Trignometry.NumberSystem(Num, Base, convert)
                    History.add_to_history_for_one_input(Num, convert, c)
                elif pick==2:
                    print("Pick a Trignometric Function","----------------------------","1. Sine, 2. Cosine","3. Tangent, 4. Inverse Sine","5. Inverse Cosine, 6. Inverse Tangent","----------------------------",sep="\n")
                    option=int(input(""))
                    angle=float(input("Enter the Angle: "))
                    pick, c = NumSys_Trignometry.Trigonometry(angle, option)
                    History.add_to_history_for_one_input(angle, pick, c)
                elif pick==3:
                    print("Pick a Hyperbolic Function","----------------------------","1. Sine, 2. Cosine, 3. Tangent","----------------------------",sep="\n")
                    option=int(input(""))
                    angle=float(input("Enter the Angle: "))
                    pick, c = NumSys_Trignometry.Hyperbolic(angle, option)
                    History.add_to_history_for_one_input(angle, pick, c)
                else:
                    print("Wrong Choice Picked.")
                    break
                
            elif Action==8:
                display.display8()
                pick=int(input(""))
                if pick==1:
                    Choose = input("Would you like to enter the data? ['yes' or 'no']")
                    if Choose=='yes':    
                        i=0
                        data=[]
                        num1 = int(input("Enter the amount of Numbers you want to enter: "))
                        print("Enter The Data.")
                        while i<num1:
                            enter_num=int(input(""))
                            data.append(enter_num)
                            i=i+1
                    else:
                        data=[1,2,3,4,5]
                if pick==1:
                    print("Pick A Statistics Operation","----------------------------","1. Mean, 2. Median, 3. Mode","4. Range, 5. Variance, 6. S.D","----------------------------")
                    opr=int(input(""))
                    op,c = Random_Operations.Statistics(data, opr)
                    History.add_to_history_statistic(data, op, c)
                elif pick==2:
                    print("Pick one:(Type it Fully)","1. 2D Shape, 2. 3D Shape",sep="")
                    shape_pick=input("")
                    if shape_pick=="2D Shape":
                        print("Pick a Shape:","1. Square, 2. Rectange", "3. Triangle, 4. Circle", sep="\n")
                        shape=int(input(""))
                        if shape==1:
                            A=int(input("Enter the side length: "))
                            area, perimeter = Random_Operations.Area(shape, A)
                            History.add_to_history_Square(A, area, perimeter)
                        elif shape==2:
                            L,W=map(int, input("Enter the length and Width of the rectangle: ").split())
                            area, perimeter = Random_Operations.Area(shape, L, W)
                            History.add_to_history_Rectangle(L, W, area, perimeter)
                        elif shape==3:
                            B,H=map(int, input("Enter the Base and Height of the Traingle: ").split())
                            p,q,r=map(int, input("Enter the Three Sides of the Triangle: ").split())
                            area, perimeter = Random_Operations.Area(shape, B, H, p, q, r)
                            History.add_to_history_Triangle(B, H, area, perimeter)
                        elif shape==4:
                            r=int(input("Enter the radius of the circle: "))
                            area, Circum = Random_Operations.Area(shape, r)
                            History.add_to_history_Circle(r, area, Circum)
                        else:
                            print("You Entered the Wrong Number.")
                            break
                    elif shape_pick=="3D Shape":
                        print("Pick a Shape:","1. Cube, 2. Prism, 3. Sphere","4. Cylinder, 5. Cone, 6. Pyramid",sep="\n")
                        shape=int(input(""))
                        if shape==1:
                            A=int(input("Enter the side length: "))
                            v,s = Random_Operations.Volume(shape, A)
                            History.add_to_history_Cube(A, v, s)
                        elif shape==2:
                            l,w,h=map(float, input("Enter the length, width and height: "))
                            v,s = Random_Operations.Volume(shape, l, w, h)
                            History.add_to_history_Prism(l, w, h, v, s)
                        elif shape==3:
                            r=float(input("Enter the radius of Sphere: "))
                            v,s = Random_Operations.Volume(shape, r)
                            History.add_to_history_Sphere(r, v, s)
                        elif shape==4:
                            r,h=map(float, input("Enter the Radius and Height of the Cylinder: ").split())
                            v,s = Random_Operations.Volume(shape, r, h)
                            History.add_to_history_Cylinder(r, h, v, s)
                        elif shape==5:
                            r,h=map(float, input("Enter the Radius and Height of the Cone: ").split())
                            v,s = Random_Operations.Volume(shape, r, h)
                            History.add_to_history_Cone(r, h, v, s)
                        elif shape==6:
                            B,h=map(float, input("Enter the Base area and Height of the Pyramid: ").split())
                            P,l=map(float, input("Enter the Perimeter and Slant Height of the Pyramid: ").split())
                            v,s = Random_Operations.Volume(shape, B, h, P, l)
                            History.add_to_history_Pyramid(B, h, v, s)
                        else:
                            print("You Have Entered the Wrong Number.")
                            break
                    else:
                        print("Wrong Entered Value.")
                        break
                elif pick==3:
                    print("Pick one:", "1. Simple Interest", "2. Compound Interest", sep="\n")
                    choose=int(input(""))
                    print("What would you like to find out?", "1. Final Amount, 2. Principal Amount", "3. Rate, 4. Time(In Years): ", sep="\n")
                    find_out=int(input(""))
                    a,b,c=map(float, input("Enter the remaining 3 Values in the sequence: ").split())
                    Type, number = Random_Operations.Principal_Interest(choose, find_out, a, b, c)
                    History.add_to_History_Interest(Type, number)
                elif pick==4:
                    print("Pick one: ","1. Random Number, 2. Random Password","3. Prime Check, 4. Simple Sequence Generator",sep="\n")
                    choose=int(input(""))
                    if choose==1:
                        a,b=Random_Operations.Random_Op(choose)
                        History.add_to_History_Random(a, b)
                    elif choose==2:
                        st = Random_Operations.Random_Op(choose)
                        History.add_to_History_Password(st)
                    elif choose==3:
                        num=int(input("Enter a Number to check if it's prime or not?: "))
                        val = Random_Operations.Random_Op(choose, num)
                        History.add_to_History_Prime(num, val)
                    elif choose==4:
                        print("Pick a Sequence:","1. (a^n), 2. (a^n)-1, 3. ((a^n)/a)","4. (a+n/a-n), 5.(a+n)/n, 6.(a*a+n)/n","7. (a*a-n)/n, 8. a/n, 9. a*n", "10. a+n, 11. a-n, 12. (a*a)/(n*n)")
                        Seq = int(input(""))
                        a,b= map(int, input("Enter the Integer Value of a and n(will increase by +1): ").split())
                        itt = int(input("Enter the amount of iterations to be performed: "))
                        Random_Operations.Random_Op(choose, a, b, itt, Seq)
                        print("\n")
                    else:
                        print("Wrong Entry.")
                        break
                else:
                    print("You have Selected the Wrong Value.")
                    break                    
            
            elif Action==9:
                print("Thank You for Using this program to sort out the problems.")
                exit()
            elif Action==10:
                display.display1()
            elif Action==12:
                History.display_history()
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input!, Please Enter Between (6-12) only.")
    
    elif Action>=1 and Action<=11:
        if Action==1:
            op=input("Enter an Operator [+, -, *, /, %, **, //]: ")
            c = Arithmatic.Operator(a, b, op)
            History.add_to_history(a, b, op, c)
        elif Action==2:
            op=input("Enter an Operator [=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=]: ")
            print("We will replace the first number with the inputted Values: ")
            c = Assignment.Assign(a, b, op)
            History.add_to_history(a, b, op, c)
        elif Action==3:
            op=input("Enter an Operator [==, !=, >, <, >=, <=]: ")
            c = Comparsion.compare(a, b, op)
            History.add_to_history(a, b, op, c)
        elif Action==4:
            num=int(input("Enter the Number to Check: "))
            condition=input("Enter the Condition to the check for the number [and, or, not]: ")
            check = input("To check for which condition? [==, ><(In Between), >=<(In Between with Open Values at End)]: ")
            c, op1, op2 = Logical.logic(a, b, num, condition, check)
            History.add_to_history_to_check(a, b, num, condition, op1, op2, c)
        elif Action==5:
            try:
                a,b= map(float, input("Enter The Two New Numbers: ").split())
                History.add_to_history(a, b, "changed")
            except ValueError:
                print("Value Error, Please Enter Only Two Numbers.")
                break    
    else:
        print("Please Enter the Correct Choice Between (1-6).")