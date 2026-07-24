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

get_days_from_today("2025-07-01") # positive value, as the date is in the past
get_days_from_today("2027-07-01") # negative value, as the date is in the future
get_days_from_today("2023-13-01") # Invalid date format. Please use YYYY-MM-DD.
get_days_from_today("2023-02-29") # Invalid date format. Please use YYYY-MM-DD.
get_days_from_today("some_text") # Invalid date format. Please use YYYY-MM-DD.
get_days_from_today(2023)  # Invalid input type. Please provide a string in the format YYYY-MM-DD.