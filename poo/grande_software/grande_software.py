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
    ELECTRIC = "electric"

class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "cocobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

class GuitarSpec:
    def __init__(self, builder, model, typeG, backWood, topWood):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood

    def matches(self, otherSpec):
        if self.builder != otherSpec.builder and otherSpec.builder != Builder.ANY.value:
            return False
        if self.model != otherSpec.model and otherSpec.model:
            return False
        if self.typeG != otherSpec.typeG and otherSpec.typeG:
            return False
        if self.backWood != otherSpec.backWood and otherSpec.backWood:
            return False
        if self.topWood != otherSpec.topWood and otherSpec.topWood:
            return False
        return True

class Guitar:
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getSpec(self):
        return self.spec

class Inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, serialNumber, price, builder, model, typeG, backWood, topWood):
        spec = GuitarSpec(builder, model, typeG, backWood, topWood)
        guitar = Guitar(serialNumber, price, spec)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def searchGuitar(self, searchSpec):
        matchingGuitars = []
        for guitar in self.guitars:
            if guitar.getSpec().matches(searchSpec):
                matchingGuitars.append(guitar)
        return matchingGuitars

inventory = Inventory()

inventory.addGuitar("V95693", 1499.95, Builder.FENDER.value, "Stratocastor", TypeG.ELECTRIC.value, Wood.ALDER.value, Wood.ALDER.value)
inventory.addGuitar("11277", 3999.95, Builder.COLLINGS.value, "CJ", TypeG.ACOUSTIC.value, Wood.INDIAN_ROSEWOOD.value, Wood.INDIAN_ROSEWOOD.value)

whatErinLikes = GuitarSpec(Builder.FENDER.value, "Stratocastor", TypeG.ELECTRIC.value, Wood.ALDER.value, Wood.ALDER.value)

matchingGuitars = inventory.searchGuitar(whatErinLikes)
if matchingGuitars:
    for guitar in matchingGuitars:
        spec = guitar.getSpec()
        print(f"Erin, you might like this {spec.builder} {spec.model} {spec.typeG} guitar:\n{spec.backWood} back and sides,\n{spec.topWood} top.\nYou can have it for only ${guitar.getPrice()}!")
else:
    print("Sorry, Erin, we have nothing for you.")