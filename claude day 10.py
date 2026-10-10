while True :
    try :
        num = int(input("Enter  a number : "))
    except ValueError :
            print("Please enter a valid number : ")
    else :
        print(f"You have entered {num}")
        break 


def read_file_safe(path):

    try :
        with open(path) as f :
            return f.read()
    except FileNotFoundError :
        return "File doesn't exisits."
    finally :
        print("Check complete!")

print(read_file_safe("sample.txt"))
print(read_file_safe("does_not_exists.txt"))

def safe_divide(a, b):
    try :
        return a / b 
    except ZeroDivisionError :
        return "Can't divide by zero"
    except TypeError :
        return "Can't divide by entered value"
    except Exception as e :
        return f"Unexpected error : {e}"

print(safe_divide(10,20))
print(safe_divide(10,0))
print(safe_divide(10 , "a"))
print(safe_divide(12,4.8))
print(safe_divide(10**400, 1))


def show_file(path):
    try :
        with open (path) as f :
            data = f.read()
    except FileNotFoundError :
        print(f"Error : {path} not found")
    else :
        print(data)
    finally :
        print("Operation Finished !")

print(show_file("sample.txt")) 
print(show_file("missing_file.txt"))
print(show_file("output.txt"))  

def set_age(age):
    if age < 0 :
        raise ValueError("Age can't be negetive")
    return f"Age set to {age}"

try :
    print(set_age(25))
    print(set_age(-3))
except ValueError as e :
    print(f"Error : {e}")


    