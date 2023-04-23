import csv

class Cafe:
    __filename = "cafe_csv_data.csv"

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)

    @property
    def cafe_data(self):
        """ Return a list obj """
        with open(self.__filename, "r", encoding="utf8") as f:
            self.__data = []
            data = csv.DictReader(f)
            for row in data:
                obj = Cafe(**row)
                self.__data.append(obj)
        return self.__data
    
    @cafe_data.setter
    def cafe_data(self, data):
        """ Handles adding data from form into csv file """
        objs = self.cafe_data
        _objects = []
        for obj in objs:
            _objects.append(obj.__dict__)
        _objects.append(data)
        with open(self.__filename, "w", encoding="utf8", newline="") as file:
            fieldname = _objects[0]
            obj = csv.DictWriter(file, fieldnames=fieldname)
            obj.writeheader()
            obj.writerows(_objects)
        

if __name__ == "__main__":
    data = Cafe().cafe_data = {"CafeName":"Testing", "Location":"Life Camp", "Open":"6AM", "Close":"8PM"}
    # print(getattr(data[0], "CafeName"))
    # print(dir(data[0]))
    # print(data[0].Location)
    #print(data)
