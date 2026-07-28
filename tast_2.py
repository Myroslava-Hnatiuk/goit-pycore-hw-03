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
