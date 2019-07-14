class LooseItem:
    def __init__(self, price_per_kilo, weight):
        self.price_per_kilo = price_per_kilo
        self.weight = weight
    def getPrice(self):
        return self.price_per_kilo * self.weight
class PackedItem:
    def __init__(self, pack_price, pack_weight):
        self.pack_price = pack_price
        self.pack_weight = pack_weight

mushrooms = LooseItem(12, 2)
potatoes = LooseItem(200, 3)
apples = LooseItem(4, 90)

# print(mushrooms.getPrice())
# print(potatoes.getPrice())
# print(apples.getPrice())

strawberries = PackedItem(12, 30)
blackberries = PackedItem(12, 21)

class PriceList:
    def printPrice():
        print(mushrooms.getPrice())
        print(potatoes.getPrice())
        print(apples.getPrice())

    printPrice()

class Mushrooms(LooseItem):
        def __init__(self, size):
            self.size = size
class Potato(LooseItem):
    def __init__(self, variety):
        self.variety = variety
class Strawberries(LooseItem):
    def __init__(self, imported):
        self.imported = imported

inmushrooms = Mushrooms("large")
inpotato = Potato("sometype")
instrawberries = Strawberries()
