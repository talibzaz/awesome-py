import sys

while True:
    try:
        x = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("Oops incorrect value!")

try:
    f = open('../file/text.txt')
    s = f.read()
    print(s)
    i = int(s.strip())
except OSError as err:
    print("OS Error: ", err)
except ValueError:
    print("could not convert data to integer")
except:
    print("Unexpected error: ", sys.exc_info()[0])
    raise

try:
    x = 10/0
except:
    print("error: ", sys.exc_info()[0])

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("divide by 0 not allowed.")
    else:
        print("Result: ", result)
    finally:
        print("Executing finally")

divide(2, 1)
divide(5, 0)