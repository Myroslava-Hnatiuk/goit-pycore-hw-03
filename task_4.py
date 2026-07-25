from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.today().date() # Get today's date as a date object
    upcoming_birthdays = [] # List to store users with upcoming birthdays

    for user in users: # Iterate through each user in the list
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # Convert the birthday string to a date object
        birthday_this_year = datetime(
            today.year,
            birthday.month,
            birthday.day
        ).date() # Create a date object for the user's birthday in the current year

        user_with_congratulations = {} # Create a dictionary to store the user's name and the date for congratulations

        if birthday_this_year < today: # If the birthday has already passed this year, then go to next user
            continue
        else: 
            date_diff = (birthday_this_year - today).days # Calculate the difference in days between the birthday in this year and today

            if date_diff <= 7: # If the birthday is within the next 7 days, then add the user to the upcoming_birthdays list
                user_with_congratulations['name'] = user['name'] # Add the user's name to the user_with_congratulations dictionary
                if birthday_this_year.weekday() == 5: # If the birthday falls on a Saturday, then set the congratulations date to Monday
                    congratulations_date = birthday_this_year + timedelta(days=2) # Add 2 days to the birthday date to get the next Monday
                    user_with_congratulations["congratulations_date"] = congratulations_date.strftime("%Y-%m-%d") # Save the congratulations date in the user dictionary in string format YYYY-MM-DD
                    upcoming_birthdays.append(user_with_congratulations)

                elif birthday_this_year.weekday() == 6: # If the birthday falls on a Sunday, then set the congratulations date to Monday
                    congratulations_date = birthday_this_year + timedelta(days=1) # Add 1 day to the birthday date to get the next Monday
                    user_with_congratulations["congratulations_date"] = congratulations_date.strftime("%Y-%m-%d") # Save the congratulations date in the user dictionary in string format YYYY-MM-DD
                    upcoming_birthdays.append(user_with_congratulations)

                else: # If the birthday falls on a weekday, then set the congratulations date to the birthday itself
                     user_with_congratulations["congratulations_date"] = birthday_this_year.strftime("%Y-%m-%d")
                     upcoming_birthdays.append(user_with_congratulations)
                continue

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.07.23"},
    {"name": "Jane Smith", "birthday": "1990.07.27"},
    {"name": "Bob Johnson", "birthday": "1990.05.07"},
    {"name": "Karl", "birthday": "1990.09.17"},
    {"name": "Alice Brown", "birthday": "1990.08.01"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)