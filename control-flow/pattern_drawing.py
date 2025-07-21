pattern = int(input("Enter the size of the pattern: "))
while range(1, pattern + 1):
    for i in range(1, pattern + 1):
        print(f"*" , end="")
        print(f"*" * (pattern - 1), end="")
        print()
    break
