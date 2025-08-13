class Product:
    def __init__(self, name, quantity):
        self.name = str(name)
        self.quantity = int(quantity)

class Store:
    def __init__(self):
        self.__products = {}

    def add_products(self, name, quantity):
        obj = Product(name, quantity)
        if obj.name in self.__products:
            self.__products[obj.name].quantity += obj.quantity
        else:
            self.__products[obj.name] = obj

    def show_products(self):
        for name ,obj in self.__products.items():
            print(f"{obj.name}  :  {obj.quantity}")
            

my_store = Store()
my_store.add_products("Coco", 3)
my_store.add_products("Coffee", 2)
my_store.add_products("Coffee", 4)
my_store.show_products()