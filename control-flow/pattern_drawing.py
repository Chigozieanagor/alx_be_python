pattern = int(input("Enter the size of the pattern: "))
while pattern:
    for i in range(1, pattern + 1):
        print("*" * pattern, end="")
        print()
    break
