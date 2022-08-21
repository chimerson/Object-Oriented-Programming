#Write a class called Product. The class should have fields called name, amount, and price, holding the product’s name, the number of items of that product in stock, and the regular price of the product. There should be a method get_price that receives the number of items to be bought and returns a the cost of buying that many items, where the regular price is charged for orders of less than 10 items, a 10% discount is applied for orders of between 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should also be a method called make_purchase that receives the number of items to be bought and decreases amount by that much

class Product:
    def __init__(self, name, amount, price):
        self._name = name
        self._amount = amount
        self._price = price

    def get_price(self, amount2):
        if amount2 < 10:
            return amount2*self._price
        elif amount2 <=99:
            return (self._price - (10*self._price)/100) * amount2
        else:
            return (self._price - (20*self._price)/100) * amount2
            
    def make_purchase(self, amount3): 
        self._amount -= amount3


    def __str__(self) -> str:
        return 'The price of what you want to buy is ${}'.format(self._price)        

if __name__ == '__main__':
    marketing = Product('Piano', 7, 100)
    print(marketing.get_price(100))
    
  
