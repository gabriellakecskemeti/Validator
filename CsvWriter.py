import csv
from os.path import isfile

import Person


class CsvWriter:

    def __init__(self, filename):
        self.filename = filename

    def write(self, person: Person):
        answer = ""
        a_w_parameter = "w"

        mydict = {"Name": person.name, "Address": person.address, "Postal": person.postal,
                  "Day": person.day, "Month": person.month,
                  "Year": person.year}

        while answer.upper() != "Q":
            try:
                a_w_parameter = "w"

                if isfile(self.filename):
                    a_w_parameter = "a"

                with open(self.filename, a_w_parameter, newline='') as csvfile:
                    # with open(self.filename, a_w_parameter, newline='', encoding="UTF-8") as csvfile:
                    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

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

    def read(self) -> Person:
        """
        It reads a csv file.
        The file must have the structure of Class Person.
        :return: Person type object
        """
        with open('people.csv', 'r', newline='') as csvfile:   #, encoding="UTF-8"
            reader = csv.reader(csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

            for row in reader:  # row contains the data a list, e.g. [“Georg”, “Mansky-Kummert”, 46.0, ... ]
                for index in range(len(row)):
                    if isinstance(row[index], float):  # if the value is a float, we convert it to an integer
                        row[index] = int(row[index])
                print(row)