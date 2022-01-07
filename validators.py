def input_postal_code(prompt, *postalcodes):
    number = 0
    while True:
        number_char = input(prompt)
        if number_char.upper() == "Q":
            return "Good bye!"
        try:
            return _check_postalcode(number_char, postalcodes)
        except ValueError as error:
            print(error)


def _check_postalcode(value, postalcodes):

    try:
        number = int(value)
    except ValueError:
        raise ValueError(f"{value} is not numerical! Only numbers, please!")

    if number not in postalcodes:
        raise ValueError(f"Postal code {number} is not valid! Valid codes are: {','.join([str(value) for value in postalcodes])}")

    return number
