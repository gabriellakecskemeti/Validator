import csv
from os.path import isfile


def input_postal_code(prompt, *postalcodes):
    """Postal code entry

    :param prompt:this a text to instruct the user what is possible to enter and how to quit.
    :param postalcodes:a list of postal codes to accept
    :return: the selected postal code
    """
    while True:
        number_char = input(prompt)
        if number_char.upper() == "Q":
            return
        try:
            return _check_postalcode(number_char, postalcodes)
        except ValueError as error:
            print(error)


def _check_postalcode(value, postalcodes):
    """
    method to check the entered postal code if it is part of the accepted codes
    list and if the entered postal code is numeric.
    :param value: entered postal code
    :param postalcodes: list of accepted codes
    :return: checked postal code in string format or error message
    if the code is not numeric or if the code is not in the list of postalcodes.
    """
    try:
        number = int(value)
    except ValueError:
        raise ValueError(f"{value} is not numerical! Only numbers, please!")

    if number not in postalcodes:
        raise ValueError(
            f"Postal code {number} is not valid! Valid codes are: {','.join([str(value) for value in postalcodes])}")

    return str(number)


def input_bounded_integer(prompt, description, minimum, maximum):
    """
    method to enter a bounded integer.
    :param prompt: text instruction for the user what it is possible to enter.
    :param description: the name of the integer. For example month or year etc.
    :param minimum: smallest accepted value of the integer
    :param maximum: highest accepted value of the integer
    :return: checked integer value or None if the user wants to quit.
    """
    while True:
        try:
            input_value = input(f"{prompt}{description}! (Enter \'q\' to quit): ")
            if input_value.upper() == "Q":
                return
            else:
                return _check_bounded_integer(input_value, description, minimum, maximum)

        except ValueError as error:
            print(error)


def _check_bounded_integer(value, description, minimum, maximum):
    """
    method to check a bounded integer
    :param value: the value what we want to check
    :param description: the name of this value. For example day, month or year, etc.
    :param minimum: smallest accepted value of the integer
    :param maximum: highest accepted value of the integer
    :return: checked integer value or an error if the value is not integer
    or not between the defined bounds.
    """
    try:
        integer_value = int(value)
    except ValueError:
        raise ValueError(f" Your input {value} for {description} was not numerical!")

    if not minimum <= integer_value <= maximum:
        raise ValueError(f"Your input {value} for {description} is not between  {minimum} and {maximum}!")

    return value


def input_string(prompt):
    """
    method to input any string value
    :param prompt: text for the user, to explain what should be entered and how to quit.
    :return: the entered value or None if the user wants to quit.
    """
    input_value = input(prompt)
    if input_value.upper() == "Q":
        return
    return input_value


def dict_to_csv(mydict, myfile):
    """
    method to write a dictionary to a csv file
    :param mydict: the dictionary
    :param myfile: the path and file name
    :return:
    """
    answer = ""
    a_w_parameter = "w"

    while answer.upper() != "Q":
        try:
            a_w_parameter = "w"

            if isfile(myfile):
                a_w_parameter = "a"

            with open(myfile, a_w_parameter, newline='') as csvfile:
            #with open(myfile, a_w_parameter, newline='', encoding="UTF-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                # the writer method works only right for special characters if i take off the utf-8 parameter.

                # writer = csv.DictWriter(csvfile, fieldnames=mydict.keys())
                if a_w_parameter == "w":
                    writer.writerow(mydict.keys())

                new_row = list()
                for i in mydict.keys():
                    new_row.append(mydict[i])
                writer.writerow(new_row)
            answer = "Q"
        except PermissionError:
            if a_w_parameter == "a":
                print("\ncsv file open! Please close the file or contact the system administrator!")
                answer = input("\nPlease press Enter if you closed the file or (Q) to quit! : ")
            else:
                print("\nPlease check the path, you do not have permission to write there."
                      " \nPlease contact the system administrator!")
                answer = "Q"
    return
