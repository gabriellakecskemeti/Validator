import validators

# print(validators.input_postal_code("Please enter your postal "
#                                   "code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040, 1050))

while True:
        selection = input(
            "Please choose which aspect to edit: (d)ay of birth, (m)onth of birth, (y)ear of birth, (p)ostal code (or enter 'q' to quit):").upper()

        match selection:
            case "DAY OF BIRTH" | "DAY" | "D":
                print(validators.input_bounded_integer("Please Enter ", "Day of birth", 1, 31))
                break
            case "MONTH OF BIRTH" | "MONTH" | "M":
                print(validators.input_bounded_integer("Please Enter ", "Month of birth", 1, 12))
                break
            case "YEAR OF BIRTH" | "YEAR" | "Y":
                print(validators.input_bounded_integer("Please Enter ", "Year of birth", 1850, 2022))
                break
            case "POSTAL CODE" | "POSTAL" | "P":
                print(validators.input_postal_code("Please enter your postal "
                                          "code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040, 1050))
                break
            case "QUIT" | "Q":

                break
            case _:
                print("Not valid option! Please try it again!")



print("Thank you for using the Validator!")


