class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
    
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self,name):
        if not hasattr(self,"_name"):
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders() if order.coffee == self})
    
    def num_orders(self):
        return sum(1 for order in self.orders() if order.coffee == self)
    
    def average_price(self):
        prices = [order.price for order in self.orders()if order.coffee == self]
        return sum(prices)/len(prices) if len(prices) else 0

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 1<= len(name) <= 15:
            self._name = name
    
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders() if order.customer == self})
    
    def create_order(self, coffee, price):
        return Order(self,coffee,price)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        if isinstance(price,float) and not hasattr(self,"_price"):
            self._price = price
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self,customer):
        if isinstance(customer,Customer):
            self._customer = customer
    
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self,coffee):
        if isinstance(coffee,Coffee):
            self._coffee = coffee

    