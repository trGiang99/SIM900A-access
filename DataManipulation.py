import csv

class DataManipulation:
    def __init__(self):
        self.data = []

    def read_file(self, target_file):
        try:
            data_file = open(target_file, 'r')
        except:
            print (f"{target_file} may not exist.")

        self.data = csv.reader(data_file, delimiter=",")

    def print_data(self):
        for row in self.data:
            print (", ".join(row))
