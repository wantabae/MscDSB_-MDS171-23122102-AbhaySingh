#restaurant
#menu items
#collecting orders
#billing
#print bill
#update order 
#search for an order
import random
class restaurant:
    def __init__(self):
        self.menu={
            "rice":30,
            "idli":10
        }
        #orderid:{set of order details}
        self.orders={}
    
    def printmenu(self):
        print("*"*30)
        print("The current options in the menu are")
        print("*"*30)
        print(self.menu)
        print("*"*30)

    def generateorderid(self):
        orderid=""
        for i in range (1,6,1):
            orderid+=str(random.randint(i,10))
        return orderid
    
    def collect_order(self):
        #print menu
        #ask user to enter the value
        #collect the value and update the order
        #print the order
        self.printmenu()#print menu
        phone=input("enter the customer phone number")
        order={}
        while True:
            item=input("enter the item name you want to order:")
            qty=int(input("enter the quantity of the item:"))
            order[item]=qty
            choice=input("Do you want to complete the order:'Y'")
            if choice=='Y':
                break
        orderid=self.generateorderid()
        self.orders[orderid]={
            "Phone":phone,
            "Order":order
        }

    def calculate_total(self, order):
        total = 0
        for item, qty in order.items():
            total += self.menu[item] * qty
        return total

    def generate_bill(self):
        

