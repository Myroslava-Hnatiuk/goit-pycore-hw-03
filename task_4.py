from datetime import datetime, timedelta

def get_congratulations_date(birthday: datetime) -> datetime:
    if birthday.weekday() == 5:  # Saturday
        return birthday + timedelta(days=2) # If the birthday falls on a Saturday, the congratulations date is set to the following Monday (2 days later).
    if birthday.weekday() == 6:  # Sunday
        return birthday + timedelta(days=1) # If the birthday falls on a Sunday, the congratulations date is set to the following Monday (1 day later).
    return birthday


def build_birthday_record(user: dict[str, str], birthday: datetime) -> dict[str, str]:
    congratulation_date = get_congratulations_date(birthday)
    return {
        "name": user["name"],
        "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
    }

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
       
        if birthday_this_year < today: # If the birthday has already passed this year
            if birthday_this_year.weekday() in (5, 6) and (today - birthday_this_year).days <= 2: # If the birthday was on a weekend and within the last 2 days
                upcoming_birthdays.append(build_birthday_record(user, birthday_this_year))
            continue

        date_diff = (birthday_this_year - today).days # Calculate the difference in days between the birthday and today
        if date_diff <= 7: # If the birthday is within the next 7 days
            upcoming_birthdays.append(build_birthday_record(user, birthday_this_year))

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.07.25"},
    {"name": "Jane Smith", "birthday": "1990.07.27"},
    {"name": "Bob Johnson", "birthday": "1990.05.07"},
    {"name": "Karl", "birthday": "1990.09.17"},
    {"name": "Alice Brown", "birthday": "1990.08.01"},
     {"name": "Alice 1", "birthday": "1990.07.29"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)