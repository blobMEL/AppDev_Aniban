
def ask_location():
    """
    Asks the user for their current location.
    Returns:
        str: The user's location.
    """
    location = input("Where are you currently living? ")
    return location

def print_location(location):
    """
    Prints the user's location.
    Args:
        location (str): The user's location.
    """
    print(f"You are currently living in {location}.")
