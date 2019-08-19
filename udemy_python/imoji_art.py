# print("\U0001f602")

num = int(input("Enter a number: \n"))
for i in range(num):
    for j in range(i+1):
        print("\U0001f602", end="")
    print()


for i in range(1, num+1):
    print("\U0001f602"*i)
