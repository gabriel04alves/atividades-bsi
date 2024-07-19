from enum import Enum

class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"

class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "ococobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

class Guitar:
    def __init__(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_builder(self):
        return self.builder

    def get_typeg(self):
        return self.typeg

    def get_model(self):
        return self.model

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood

class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, typeg, back_wood, top_wood)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search_guitar(self, search_guitar):
        for guitar in self.guitars:
            if search_guitar.get_builder() != guitar.get_builder():
                continue

            model = search_guitar.get_model().lower()
            if model and model != "" and model != guitar.get_model().lower():
                continue

            if search_guitar.get_typeg() != guitar.get_typeg():
                continue
            if search_guitar.get_back_wood() != guitar.get_back_wood():
                continue
            if search_guitar.get_top_wood() != guitar.get_top_wood():
                continue
            return guitar
        return None

inventory = Inventory()

inventory.add_guitar("V95693", 1499.95, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)

whatErinLikes = Guitar(" ", 0, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
guitar = inventory.search_guitar(whatErinLikes)
if guitar is not None:
  print(f"Erin, talvez você goste desta: {guitar.get_builder()} {guitar.get_model()} {guitar.get_typeg()} guitar:\n {guitar.get_back_wood()} na traseira e laterais, \n{guitar.get_top_wood()} no tampo.\n Ela pode ser sua por apenas US${guitar.get_price()}!")
else:
  print("Desculpe Erin, não temos nada para você")
