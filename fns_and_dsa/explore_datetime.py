from datetime import datetime,timedelta

def display_current_datetime():
    current_date = datetime.now()
    formated_date = current_date.strftime(f"%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formated_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime(f"%Y-%m-%d")
    print(f"Future Date: {formatted_future_date}")

display_current_datetime()
calculate_future_date()