
try:
    f = open("abc.txt")
    b = 1/0
#except Exception as e:
    print(e)
#except ZeroDivisionError:
    print("divided by zero")
#except FileNotFoundError:
    print("file not find")
except (FileNotFoundError, ZeroDivisionError):
    print("sdsdsddsdsdsd")

#i = 0/0

#we added it here just for fun
