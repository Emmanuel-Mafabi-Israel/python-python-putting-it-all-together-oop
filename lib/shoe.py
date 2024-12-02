# GLORY BE TO GOD,
# PYTHON PROGRAMMING - PYTHON - PROPERTY FUNCTION DECORATOR
# BY ISRAEL MAFABI EMMANUEL

class Shoe:
    def __init__(self, brand:str="", size:int = 0):
        self.brand = brand
        self.size  = size

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            print("Brand name should be a string ~ text.")
        else:
            self._brand = value

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("Shoe size should be a number(integer)!")
        else:
            self._size = value

    def cobble(self):
        try:
            self.condition = "New"
            print("Your shoe is as good as new!")
        except TypeError as e:
            print(f"Error: {e}")


adidas = Shoe("Adidas", 9)
adidas.cobble()
print(adidas.condition)