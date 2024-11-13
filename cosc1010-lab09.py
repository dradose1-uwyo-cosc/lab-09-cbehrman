#Caleb Behrman
#UWYO COSC 1010
#11/13/24
#Lab 9
#Lab Section:15

class Pizza:
    def __init__(self, size, sauce='red'):
        self.setSize(size)
        #Set the sauce defaulting to red
        self.sauce=sauce
        #toppings is default
        self.toppings=['cheese']
#we did this whole first part together in class, I changed a couple of things though
    def setSize(self, size):
        if size>10:
            self.size=size
        else:
            self.size=10
    
    def getSize(self):
        return self.size

    def addToppings(self, *new_toppings):
        #adds new toppings
        self.toppings.extend(new_toppings)
    
    def getToppings(self):
        return self.toppings
    
    def getAmountOfToppings(self):
        return len(self.toppings)


class Pizzeria:
    price_per_topping=0.30
    price_per_inch=0.60

    def __init__(self):
        self.orders=0
        self.pizzas=[]

    def placeOrder(self):
        self.orders+=1
        
        #gets pizza size
        size=int(input("Please enter the size of pizza, as a whole number. The smallest size is 10\n"))
        
        #pizza sauze
        sauce=input("What kind of sauce would you like?\nLeave blank for red sauce\n")
        if not sauce:
            sauce='red'
        
        #toppings
        toppings=[]
        while True:
            topping=input("Please enter the toppings you would like, leave blank when done\n")
            if topping=='':
                break
            toppings.append(topping)

        #putting it all together
        pizza=Pizza(size, sauce)
        pizza.addToppings(*toppings)
        self.pizzas.append(pizza)

        #prints the recept
        self.getReceipt(pizza)

    def getPrice(self, pizza):
        #price calculations
        price_for_size=pizza.getSize()*self.price_per_inch
        price_for_toppings=pizza.getAmountOfToppings()*self.price_per_topping
        return price_for_size+price_for_toppings

    def getReceipt(self, pizza):
        #prints details and prices
        print(f"\nYou ordered a {pizza.getSize()}\" pizza with {pizza.sauce} sauce and the following toppings:")
        for topping in pizza.getToppings():
            print(f"                                                                  {topping}")
        
        price_for_size=pizza.getSize()*self.price_per_inch
        price_for_toppings=pizza.getAmountOfToppings()*self.price_per_topping
        total_price=self.getPrice(pizza)

        print(f"You ordered a {pizza.getSize()}\" pizza for {price_for_size}")
        print(f"You had {pizza.getAmountOfToppings()} topping(s) for ${price_for_toppings}")
        print(f"Your total price is ${total_price:.2f}\n")

    def getNumberOfOrders(self):
        return self.orders


#this is the main loop
def main():
    pizzeria=Pizzeria()
    
    while True:
        user_input=input("Would you like to place an order? type exit to exit\n")
        
        if user_input.lower()=='exit':
            break
        
        pizzeria.placeOrder()
    
    print(f"\nTotal number of orders placed: {pizzeria.getNumberOfOrders()}")

#this runs the whole things
if __name__=="__main__":
    main()