from Person import Person
from CsvWriter import CsvWriter
#import CsvWriter
import validators

p1 = Person(None, None, None, None, None, None)
# person = {"Name": P1.name, "Address": P1.address, "Postal": P1.postal, "Day": P1.day, "Month": P1.month,
#          "Year": P1.year}

while True:
    selection = input(
        "Please choose which aspect to edit: (n)ame, (a)ddress, (p)ostal code, (d)ay of birth, (m)onth of birth, (y)ear of birth (or enter 'q' to quit):").upper()

    match selection:
        case "NAME" | "N":
            # person["Name"] = validators.input_string("Please Enter Name, (Enter 'q' to quit): ")
            p1.name = validators.input_string("Please Enter Name, (Enter 'q' to quit): ")
        case "ADDRESS" | "A":
            # person["Address"] = validators.input_string("Please Enter your Address, (Enter 'q' to quit): ")
            p1.address = validators.input_string("Please Enter your Address, (Enter 'q' to quit): ")
        case "POSTAL CODE" | "POSTAL" | "P":
            # person["Postal"] = validators.input_postal_code("Please enter your postal "
            #                                                "code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040,
            #                                                1050)
            p1.postal = validators.input_postal_code("Please enter your postal "
                                                     "code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040,
                                                     1050)
        case "DAY OF BIRTH" | "DAY" | "D":
            # person["Day"] = validators.input_bounded_integer("Please Enter ", "Day of birth", 1, 31)
            p1.day = validators.input_bounded_integer("Please Enter ", "Day of birth", 1, 31)
        case "MONTH OF BIRTH" | "MONTH" | "M":
            # person["Month"] = validators.input_bounded_integer("Please Enter ", "Month of birth", 1, 12)
            p1.month = validators.input_bounded_integer("Please Enter ", "Month of birth", 1, 12)
        case "YEAR OF BIRTH" | "YEAR" | "Y":
            # person["Year"] = validators.input_bounded_integer("Please Enter ", "Year of birth", 1850, 2022)
            p1.year = validators.input_bounded_integer("Please Enter ", "Year of birth", 1850, 2022)
        case "QUIT" | "Q":
            break
        case _:
            print("Not valid option! Please try it again!")

#methode using dictionary have been deleted
#person = {"Name": p1.name, "Address": p1.address, "Postal": p1.postal, "Day": p1.day, "Month": p1.month,
#          "Year": p1.year}
#validators.dict_to_csv(person, "people.csv")
#print(person)


csv1 = CsvWriter("people.csv")

csv1.write(p1)
print(p1)
print("Thank you for using the Validator!")

print("Reading.....!")
csv1.read()
