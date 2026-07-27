import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    # Check if all parameters are integers then return an empty list if not
    if not all(type(x) is int for x in (min, max, quantity)): 
        return []

    # Check if min is less than 1 then return an empty list
    if min < 1:
        return []

    # Check if max is less than 1 then return an empty list
    if max < 1:
        return []

    # Check if max is greater than 1000 then return an empty list
    if max > 1000:
        return []

    if min > max:
        return []

    if quantity < 1:
        return []
    # Check if the range between min and max is less than the quantity of numbers requested, then return an empty list
    if max - min + 1 < quantity:
        return []
    
    random_numbers = range(min, max + 1) # Generate a list of random numbers between min and max + 1 to include max
    selected_amount_of_numbers = random.sample(random_numbers, quantity) # make a random selection of unique numbers from the list of random numbers
    sorted_numbers = sorted(selected_amount_of_numbers) # sort the selected numbers in ascending order
    print(sorted_numbers)
    return sorted_numbers


get_numbers_ticket(1, 49, 6) # [1, 4, 5, 12, 19, 36]
get_numbers_ticket(1, 36, 5) # [6, 8, 14, 16, 17]
get_numbers_ticket(0, 35, 5) # []
get_numbers_ticket(1, 1001, 5) # []
get_numbers_ticket(1, 10, 15) # []
get_numbers_ticket(1, 10, "five") # []
get_numbers_ticket(1, 10, 5.5) # []