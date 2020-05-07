import abc




class Pizza(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def get_status(self):
        pass



class Margherita(Pizza):
    def __init__(self):
        self.__pizza_price = 15.0


    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return  "Margherita: Tomato, Oregano, Cheese Mozzarella\n"




class Pepperoni(Pizza):
    def __init__(self):
        self.__pizza_price = 12.0



    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return  "Pepperoni: Pepperoni, Cheese Mozzarella\n"



class Chicken_BBQ(Pizza):
    def __init__(self):
        self.__pizza_price = 13.0



    def get_price(self):
        return self.__pizza_price

    def get_status(self):
        return  "Chicken_BBQ: Grilled Chicken, BBQ,Cheese Mozzarella\n"




class PizzaDecorator(Pizza):
    def __init__(self,pizza):
        self.pizza = pizza

    def get_price(self):
        return self.pizza.get_price()


    def get_status(self):
        return self.pizza.get_status()



class Tomato(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__tomato_price = 1.5


    @property
    def price(self):
        return self.__tomato_price

    def get_price(self):
        return super().get_price() + self.price

    def get_status(self):
        return super().get_status() + " + Tomato"


class Cheese(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__cheese_price = 2.0


    @property
    def price(self):
        return self.__cheese_price

    def get_price(self):
        return super().get_price() + self.price

    def get_status(self):
        return super().get_status() + " + Cheese"

class BBQ(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__bbq_price = 2.5


    @property
    def price(self):
        return self.__bbq_price

    def get_price(self):
        return super().get_price() + self.price

    def get_status(self):
        return super().get_status() + " + BBQ"

#-------------------------------------------Business Layer--------------------------------------------


class PizzaBuilder:

    def __init__(self, ptype):
        self.ptype = ptype
        self.pizza=eval(ptype)()
        self.extentions_list=[]
    
    def add_extension(self, extention):
        if extention=="Tomato":
            self.pizza=Tomato(self.pizza)
        elif extention=="Cheese":
            self.pizza=Cheese(self.pizza)

        elif extention=="BBQ":
            self.pizza=BBQ(self.pizza)
        
        self.extentions_list.append(extention)
   
    def remove_extension(self, extention):
        if extention in self.extentions_list:
            self.extentions_list.remove(extention)

        temp_pizza=eval(self.ptype)()
        for i in self.extentions_list:
            temp_pizza=eval(i)(temp_pizza)

        self.pizza=temp_pizza

    def get_price(self):
        return self.pizza.get_price()

    def get_status(self):
        return self.pizza.get_status()





