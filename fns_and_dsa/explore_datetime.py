import datetime

def calculate_future_date():

    def display_current_datetime():
        current_date = datetime.datetime.now()
        print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
        return current_date
    
    current_date = display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    future_date = current_date + datetime.timedelta(days=number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

calculate_future_date()
