class Computer:
     def __init__(self):
          self.__max_price=1000
     def sell(self):
         print("The selling price is : ",self.__max_price) 
     def set_max_price(self,price):
          self.__max_price=price
obj1=Computer()
obj1.sell()
obj1.set_max_price(1500)  
obj1.sell()