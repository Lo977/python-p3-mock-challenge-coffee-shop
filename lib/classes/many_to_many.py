class Coffee:
    all = []

    def __init__(self, name: str):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self) -> str:
        return self._name 

    @name.setter
    def name(self, name: str):
        if not hasattr(self, "_name"):  # Ensure name can only be set once
            self._name = name

    def orders(self) -> list:
        """Returns all orders that contain this coffee."""
        return [order for order in Order.all if order.coffee == self]

    def customers(self) -> list:
        """Returns a list of unique customers who ordered this coffee."""
        return list({order.customer for order in self.orders()})

    def num_orders(self) -> int:
        """Returns the total number of orders for this coffee."""
        return len(self.orders())

    def average_price(self) -> float:
        """Returns the average price of this coffee across all orders."""
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0

    
class Customer:
    all = []

    def __init__(self, name: str):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self) -> str:
        return self._name 

    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        # else:
        #     raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self) -> list:
        """Returns all orders made by this customer."""
        return [order for order in Order.all if order.customer == self]

    def coffees(self) -> list:
        """Returns a list of unique coffees ordered by this customer."""
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee: Coffee, price: float) -> 'Order':
        """Creates and returns a new order for this customer."""
        return Order(self, coffee, price)

    


class Order:
    all = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float):
        if isinstance(price, float) and not hasattr(self,"_price") and price >= 0:
            self._price = price
        # else:
        #     raise ValueError("Price must be a positive float.")

    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    def customer(self, customer: Customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError("Customer must be an instance of Customer.")

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    @coffee.setter
    def coffee(self, coffee: Coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError("Coffee must be an instance of Coffee.")

    