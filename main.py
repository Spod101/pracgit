import os as s 
again = True

def divide(num = 0, deno = 0):
    print("=======================================")
    if deno == 0:
        return None
    else:
        return int(num) / int(deno)
    
def exponent(base = 0, exp = 0):
    print("=======================================")
    exp = base ** exp
    return exp

def remainder(num = 0, deno = 0):
    rem = 0
    print("=======================================")
    if deno == 0:
        return None
    else:
        return int(num) % int(deno)

def summation(lr = 0 , up = 0):
    sum = 0
    print("=======================================")
    if lr > up:
        return None
    else:
        for x in range(lr, up+1):
            sum += x
        return sum

def operation(choice):
    print("=======================================")
    if choice == "d":
        x = int(input("Enter the First number: \t"))
        y = int(input("Enter the Second number: \t"))
        print("Quotient: \t\t\t{}".format(divide(x, y)))
        s.system("pause")
        s.system("cls")
    elif choice == "e":
        x = int(input("Enter the First number: \t"))
        y = int(input("Enter the Second number: \t"))
        print("Result: \t\t\t{}".format(exponent(x, y)))
        s.system("pause")
        s.system("cls")
    elif choice == "r":
        x = int(input("Enter the First number: \t"))
        y = int(input("Enter the Second number: \t"))
        print("Remainder: \t\t\t{}".format(remainder(x, y)))
        s.system("pause")
        s.system("cls")
    elif choice == "f":
        x = int(input("Enter the First number: \t"))
        y = int(input("Enter the Second number: \t"))
        print("Summation: \t\t\t{}".format(summation(x, y)))
        s.system("pause")
        s.system("cls")
    else:
        s.system("cls")
        print("Invalid choice")
        s.system("pause")
        s.system("cls")

while again == True:
    print("========================================")
    print("[D.] - Divide")
    print("[E.] - Exponentation")
    print("[R.] - Remainder")
    print("[F.] - Summation")
    print("========================================")
    choice = input("Enter your choice: ").lower()
    s.system("pause")
    s.system("cls")
    operation(choice)
