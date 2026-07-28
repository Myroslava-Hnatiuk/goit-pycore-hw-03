from datetime import datetime # importing datetime module to work with dates

def get_days_from_today(dateStr: str) -> int:
    try:
        # converting string to date object, if this step gets errors, it will be caught in the except block
        date  = datetime.strptime(dateStr, "%Y-%m-%d")

        # getting today's date and converting it to date object
        today = datetime.strptime(datetime.today().strftime("%Y-%m-%d"), "%Y-%m-%d")

        # getting the difference between today and the given date as a timedelta object
        date_delta = today - date

        # getting the difference in days from the timedelta object
        difference_days = date_delta.days

        print(difference_days)

        return difference_days
    
    except TypeError:
        print("Invalid input type. Please provide a string in the format YYYY-MM-DD.")
        return None
    
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None