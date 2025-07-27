def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                print("chose a none zero number")
                
            elif num2 >= 1:
                return num1 / num2       
        case _:
            print()
