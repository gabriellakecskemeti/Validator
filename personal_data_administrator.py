import validators

person = {"Name": None, "Address": None, "Postal": None, "Day": None, "Month": None, "Year": None}

while True:
    selection = input(
        "Please choose which aspect to edit: (n)ame, (a)ddress, (p)ostal code, (d)ay of birth, (m)onth of birth, (y)ear of birth (or enter 'q' to quit):").upper()

    match selection:
        case "NAME" | "N":
            person["Name"] = validators.input_string("Please Enter Name, (Enter 'q' to quit): ")
        case "ADDRESS" | "A":
            person["Address"] =validators.input_string("Please Enter your Address, (Enter 'q' to quit): ")
        case "POSTAL CODE" | "POSTAL" | "P":
            person["Postal"] = validators.input_postal_code("Please enter your postal "
                                                                  "code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040,
                                                                  1050)
        case "DAY OF BIRTH" | "DAY" | "D":
            person["Day"] = validators.input_bounded_integer("Please Enter ", "Day of birth", 1, 31)
        case "MONTH OF BIRTH" | "MONTH" | "M":
            person["Month"] = validators.input_bounded_integer("Please Enter ", "Month of birth", 1, 12)
        case "YEAR OF BIRTH" | "YEAR" | "Y":
            person["Year"] = validators.input_bounded_integer("Please Enter ", "Year of birth", 1850, 2022)

        case "QUIT" | "Q":
            break
        case _:
            print("Not valid option! Please try it again!")

#validators.dict_to_csv(person, "c:people.csv")
validators.dict_to_csv(person, "people.csv")

print(person)
print("Thank you for using the Validator!")
