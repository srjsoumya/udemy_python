num = None
while num == None or num != 0:
    num = int(input("Enter a number: or 0 to exit\n"))
    if num == 0:
        continue
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
print("------Exited-----")