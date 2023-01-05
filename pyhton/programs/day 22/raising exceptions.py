

#exception handling
#raising exceptions (we can set the conditions)

try:
    age = int(input("Enter you age: "))
    if age>18:
        print("Liscence can be issued.")
    else:
        raise KeyError("The candidate is underage")
except Exception as e: #Exception is the main class, allother errors comes under this
    print(e)
