"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = ['A', 'B', 'C', 'D']
    current_number = 0
    while current_number < number:
        index = current_number - 4*(current_number//4)
        yield letters[index]
        current_number += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    letters = generate_seat_letters(number)
    current_number = 0 

    while current_number < number:
        row = 1 + (current_number // 4)
        row += row // 13
        yield f'{row}{letters.__next__()}'
        current_number += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = generate_seats(len(passengers))
    return {passenger: seats.__next__() for passenger in passengers}

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    while seat_numbers:
        seat = seat_numbers.pop(0)
        num_zeros = 12 - (len(seat) + len(flight_id))
        zeros = '0' * num_zeros
        yield f'{seat}{flight_id}{zeros}'
