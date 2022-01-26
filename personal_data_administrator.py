from Person import Person
from CsvWriter import CsvWriter
#import CsvWriter
import validators

p1 = Person(None, None, None, None, None, None)

while True:
    selection = input(
        "Please choose which aspect to edit: \n(n)ame, \n(a)ddress, \n(p)ostal code, \n(d)ay of birth, \n(m)onth of birth, \n(y)ear of birth \n(or enter 'q' to quit):").upper()

    match selection:
        case "NAME" | "N":
            p1.name = validators.input_string("Please Enter Name, (Enter 'q' to quit): ")
        case "ADDRESS" | "A":
            p1.address = validators.input_string("Please Enter your Address, (Enter 'q' to quit): ")
        case "POSTAL CODE" | "POSTAL" | "P":
            p1.postal = validators.input_postal_code("Please enter your postal "
                                                     "code (Enter 'q' to quit): ", 1010, 1020, 1030, 1040,
                                                     1050)
        case "DAY OF BIRTH" | "DAY" | "D":
            p1.day = validators.input_bounded_integer("Please Enter ", "Day of birth", 1, 31)
        case "MONTH OF BIRTH" | "MONTH" | "M":
            p1.month = validators.input_bounded_integer("Please Enter ", "Month of birth", 1, 12)
        case "YEAR OF BIRTH" | "YEAR" | "Y":
            p1.year = validators.input_bounded_integer("Please Enter ", "Year of birth", 1850, 2022)
        case "QUIT" | "Q":
            break
        case _:
            print("Not valid option! Please try it again!")


csv1 = CsvWriter("people.csv")

csv1.write(p1)
print(p1)


print("Reading.....!")
personlist=csv1.read()

print("List of Person objects:")  #only for presentation oof the result
for x in personlist:
    print(x)

print("Thank you for using the Validator!")