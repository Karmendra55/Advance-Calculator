import datetime

def save_history(data):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("util/history.txt","a") as file:
        file.write(f"{current_time}: {data}\n")

history = []

def add_to_history(number1=None ,number2=None ,operation=None , result=None):
    entry = f">>> {number1} {operation} {number2} : {result}"
    history.append(entry)
    save_history(entry)

def display_history():
    if history:
        print("\nCalculation History:")
        for record in history:
            print(record)
    else:
        print("\nNo calculations performed yet.")

# Function to add a specific type of history entry (example for checking conditions)
def add_to_history_to_check(number1=None, number2=None, check=None, condition=None, operation1=None, operation2=None, result=None):
    entry = f">>> Is {check} {operation1} {number1} {condition} {check} {operation2} {number2} : {result}"
    history.append(entry)
    save_history(entry)

# Function for other specific history entries (e.g., for square, rectangle, etc.)
def add_to_history_for_one_input(number1=None, operation=None, Result=None):
    entry = f">>> {number1} {operation} : {Result}"
    history.append(entry)
    save_history(entry)

def add_to_history_statistic(data=[], operation=None, Result=None):
    entry = f">>> {data} with {operation} will get: {Result}"
    history.append(entry)
    save_history(entry)

def add_to_history_Square(number1=None, area=None, Perimeter=None):
    entry = f">>> square with sides of {number1} has {area} Area and {Perimeter} Perimeter."
    history.append(entry)
    save_history(entry)

def add_to_history_Rectangle(number1=None, number2=None, area=None, Perimeter=None):
    entry = f">>> Rectangle with sides of {number1} and {number2} has {area} Area and {Perimeter} Perimeter."
    history.append(entry)
    save_history(entry)

def add_to_history_Triangle(number1=None, number2=None, area=None, Perimeter=None):
    entry = f">>> Triangle with base and height of {number1} and {number2} has {area} Area and {Perimeter} Perimeter."
    history.append(entry)
    save_history(entry)

def add_to_history_Circle(number1=None, area=None, Circumference=None):
    entry = f">>> Circle with radius of {number1} has {area} Area and {Circumference} Circumference."
    history.append(entry)
    save_history(entry)

def add_to_history_Cube(number1=None, volume=None, Surface=None):
    entry = f">>> Cube with side of {number1} has {volume} Volume and {Surface} Surface."
    history.append(entry)
    save_history(entry)

def add_to_history_Prism(number1=None, number2=None, number3=None, volume=None, Surface=None):
    entry = f">>> Prism with sides of {number1}, {number2} and {number3} has {volume} Volume and {Surface} Surface."
    history.append(entry)
    save_history(entry)

def add_to_history_Sphere(number1=None, Volume=None, Surface=None):
    entry = f">>> Sphere with radius of {number1} has {Volume} Volume and {Surface} Surface."
    history.append(entry)
    save_history(entry)

def add_to_history_Cylinder(number1=None, number2=None, Volume=None, Surface=None):
    entry = f">>> Cylinder with radius and height of {number1} and {number2} has {Volume} Volume and {Surface} Surface."
    history.append(entry)
    save_history(entry)

def add_to_history_Cone(number1=None, number2=None, Volume=None, Surface=None):
    entry = f">>> Cone with radius and height of {number1} and {number2} has {Volume} Volume and {Surface} Surface."
    history.append(entry)
    save_history(entry)

def add_to_history_Pyramid(number1=None, number2=None, Volume=None, Surface=None):
    entry = f">>> Pyramid with Base area and Height of {number1} and {number2} has {Volume} Volume and {Surface} Surface."
    history.append(entry)
    save_history(entry)

def add_to_History_Interest(Type=None, number=None):
    entry = f">>> {Type} Interest when calculated gives total of : {number}."
    history.append(entry)
    save_history(entry)

def add_to_History_Random(Number1=None, Number2=None):
    entry = f">>> The Random Number Generated are: {Number1} and {Number2}"
    history.append(entry)
    save_history(entry)

def add_to_History_Password(Pass1=None):
    entry = f">>> The Password Generated is: {Pass1}"
    history.append(entry)
    save_history(entry)

def add_to_History_Prime(Number=None, Value=None):
    entry = f">>> The {Number} is {Value}."
    history.append(entry)
    save_history(entry)