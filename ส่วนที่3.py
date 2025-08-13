class Onlineshop:
    def __init__(self, name, url):
        self.name = name          
        self.url = url            
        self.products = {}     

    def addingItemsToCart(self, customer, product, quantity):
        if product.name in customer._cart:
            customer._cart[product.name]['quantity'] += quantity
        else:
            customer._cart[product.name] = {
                'product': product,
                'quantity': quantity
            }

    def checkout(self, customer):
        if not customer._cart:
            return "Empty"

        order_id = len(customer.past_orders) + 1
        total = sum(details['product'].price * details['quantity']
                    for details in customer._cart.values())
        item = {
            name: {
                "quantity": details['quantity'],
                "price": details['product'].price
            }
            for name, details in customer._cart.items()
        }
        order = {
            "order_id": order_id,
            "items": item,
            "total": total
        }

        customer.past_orders[order_id] = order
        customer._cart.clear()
        return f"Order #{order_id} placed success!"

    def orderTracking(self, customer, order_id):
        return customer.past_orders.get(order_id, "Order not found.")


class Product:
    def __init__(self, name, description, price, online_shop):
        self.name = name              
        self.description = description 
        self.price = float(price)      
        self.online_shop = online_shop  


class Customer:
    def __init__(self, name, email, address):
        self._name = name             
        self._email = email           
        self.__address = address        
        self._cart = {}                 
        self.past_orders = {}          

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, new_name):
        self._name = new_name

    # Getter for email
    def get_email(self):
        return self._email

    # Setter for email
    def set_email(self, new_email):
        self._email = new_email

    # Getter for address
    def get_address(self):
        return self.__address

    # Setter for address
    def set_address(self, new_address):
        self.__address = new_address

# Example usage
my_store = Onlineshop("Gadget World", "www.gadgetworld.com")
my_product1 = Product("Laptop", "noob", 49, my_store)
my_product2 = Product("Mouse", "noobs", 496, my_store)
my_product3 = Product("Mouse", "noobs", 496, my_store)

john = Customer("john", "jojo@ghjiotdh", "jostar230")

my_store.addingItemsToCart(john, my_product1, 3)
print(my_store.checkout(john))
print(my_store.orderTracking(john, 1))

# Accessing encapsulated attributes safely
print(john.get_name())      # john
print(john.get_email())     # jojo@ghjiotdh
print(john.get_address())   # jostar230