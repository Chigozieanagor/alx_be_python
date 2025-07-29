from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    now_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {now_date}")

    return current_date
def calculate_future_date():
    current_date = display_current_datetime()

    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")

    future_date = current_date + timedelta(days = number_of_days)

    print("Future Date:", future_date.strftime("%Y-%m-%d") )

if __name__ == "__main__":
    calculate_future_date()
