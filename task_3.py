import re

def normalize_phone(phone_number: str) -> str:
    if type(phone_number) is not str:
        print(f"Invalid phone number: {phone_number}. It is not a string.")
        return None

    phone_digits = re.sub(r"[^\d]", "", phone_number) # Remove all non-digit characters from the phone number

    if len(phone_digits) < 10:
        print(f"Invalid phone number: {phone_number}. It has less than 10 digits.")
        return None

    # If number starts with +380, it is already correct
    if phone_digits.startswith("+380"):
        return phone_digits

    # If number starts with 380, add only +
    elif phone_digits.startswith("380"):
        return "+" + phone_digits

    # If number starts with 80, add only +3
    elif phone_digits.startswith("80"):
        return "+3" + phone_digits

    # If number starts with 0, add +38
    elif phone_digits.startswith("0"):
        return "+38" + phone_digits


raw_numbers = [
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "8 050 123 4567",
    "+380+501234567",
    "++380501234567"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

