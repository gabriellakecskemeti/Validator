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
        raise ValueError(
            f"Postal code {number} is not valid! Valid codes are: {','.join([str(value) for value in postalcodes])}")

    return number


def input_bounded_integer(prompt, description, minimum, maximum):
    while True:
        try:
            input_value = input(f"{prompt}{description}! (Enter \'q\' to quit): ")
            if input_value.upper() == "Q":
                return "Good bye!"
            else:
                return _check_bounded_integer(input_value, description, minimum, maximum)

        except ValueError as error:
            print(error)


def _check_bounded_integer(value, description, minimum, maximum):
    try:
        integer_value=int(value)
    except ValueError:
        raise ValueError(f" Your input {value} for {description} was not numerical!")

    if not minimum <= integer_value <= maximum:
        raise ValueError(f"Your input {value} for {description} is not between  {minimum} and {maximum}!")

    return value
