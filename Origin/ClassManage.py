classes = {
  "adidas": 0, "alfa-romeo": 1, "amazon": 2, "apple": 3, "at&t": 4, "audi": 5, "bmw": 6,
  "cisco": 7, "coca-cola": 8, "corona": 9, "dacia": 10, "disney": 11, "ducati": 12, "fedex": 13,
  "ferrari": 14, "fiat": 15, "ford": 16, "general-electric": 17, "google": 18, "heineken": 19,
  "hp": 20, "hyundai": 21, "ibm": 22, "ikea": 23, "intel": 24, "kia": 25, "lamborghini": 26, "lego": 27,
  "levis": 28, "lexus": 29, "marlboro": 30, "mazda": 31, "mcdonald": 32, "mercedes-benz": 33, "microsoft": 34,
  "mitsubishi": 35, "mustang": 36, "nike": 37, "nissan": 38, "opel": 39, "pepsi": 40, "peugeot": 41,
  "pinterest": 42, "red-bull": 43, "renault": 44, "samsung": 45, "seat": 46, "skoda": 47, "starbucks": 48,
  "suzuki": 49, "taipei": 50, "target": 51, "tesla": 52, "toyota": 53, "volkswagen": 54, "volvo": 55
}

class Classes:
    def __init__(self):
        self.classesDictionar = classes
        self.classes = self.getClasses(self.classesDictionar)

    def getClasses(self, classes):
        cl_all = sorted(list(classes))
        return cl_all

    def getClassName(self, number):
        for cls in self.classesDictionar:
            if self.classesDictionar[cls] == number:
                return cls
        return None  # None

    def getClass(self, nameLogo):
        for cls in self.classesDictionar:
            if cls == nameLogo:
                return self.classesDictionar[cls]
        return 27  # None