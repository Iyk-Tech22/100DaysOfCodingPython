import csv

class Cafe:
    __filename = "cafe-data.csv"

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)

    @property
    def cafe_data(self):
        """ Return a list obj """
        with open(self.__filename, "r") as f:
            self.__data = []
            data = csv.DictReader(f)
            for row in data:
                obj = Cafe(**row)
                self.__data.append(obj)
        return self.__data

if __name__ == "__main__":
    data = Cafe().cafe_data
    print(getattr(data[0], "Cafe Name"))
    print(dir(data[0]))
    print(data[0].Location)

