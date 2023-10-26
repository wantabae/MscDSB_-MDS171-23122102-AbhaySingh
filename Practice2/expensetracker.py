# #create a class restaurant
# #item and qty as input
# #inside your class you are having the item
# #and its price as a dictionary
# #create a function calculate total cost
# #print everything
# # class restaurant:
# #     def __init__(self,itmnm,qty):
# #         self.itmnm=itmnm
# #         self.qty=qty
# #         self.menuitems={"Rice":30,"Chicken":100,"Dal":40,"Chapati":10}
    
# #     def totalcost(self):
# #         print("Total cost for the item is:")
# #         print("Item\t:",self.itmnm)
# #         print("Quantity\t:",self.qty)
# #         total=self.qty*self.menuitems[self.itmnm]
# #         print("Total\t:",total)

# # obj=restaurant("Rice",4)
# # obj.totalcost()

# class Restaurant:
#     def __init__(self, itmnm, qty):
#         self.itmnm = itmnm
#         self.qty = qty
#         self.menuitems = {"Rice": 30, "Chicken": 100, "Dal": 40, "Chapati": 10}

#     def totalcost(self):
#         print("Total cost for the item is:")
#         print("Item\t:", self.itmnm)
#         print("Quantity\t:", self.qty)
#         total = self.qty * self.menuitems[self.itmnm]
#         print("Total\t:", total)

# # Ask the user for input
# itmnm = input("Enter the item name: ")
# qty = int(input("Enter the quantity: "))
# obj = Restaurant(itmnm, qty)
# obj.totalcost()


#define a class expense tracker that stores the
#expenses and income in a dictionary
#implement the method to 
# - store the transaction;
# - view transactions;
#calculate the total expense/income

# class expenseTracker:
#     def __int__(self):
#         self.expenseDict = {
#             "income": [],
#             "expense": [],
#         }
#     def store_transactions(self,type,amt,category,date,details):
#         trans = {
#             "Amount": amt,
#             "Category" : category,
#             "Date" : date,
#             "Details" : details,
#         }

#         if type == "income":
#             self.expenseDict['income'].append(trans)
#         else:
#             self.expenseDict['ex[ense]'].append(trans)

#     def view_transaction(self):
#         print("Your income:")
#         for item in self.expenseDict['income']:
#             print(item)
#         print("your expenses:")
#         for item in self.expenseDict['expense']:
#             print(item)

#     def calculate_transactions(self):
#         total_income=0
#         for item in self.expenseDict['income']:
#             total_income+=item["Amount"]
#         print("Total income\t:\t",total_income)
        
#         total_expense=0
#         for item in self.expenseDict['expense']:
#             total_expense+=item["Amount"]
#         print("Total Expenses\t:\t",total_expense)
class ExpenseTracker:
    def __init__(self):
        self.expenseDict = {
            "income": [],
            "expense": [],
        }

    def store_transaction(self, type, amt, category, date, details):
        trans = {
            "Amount": amt,
            "Category": category,
            "Date": date,
            "Details": details,
        }

        if type == "income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expense'].append(trans)

    def view_transactions(self):
        print("Your income:")
        for item in self.expenseDict['income']:
            print(item)
        print("Your expenses:")
        for item in self.expenseDict['expense']:
            print(item)

    def calculate_transactions(self):
        total_income = sum(item["Amount"] for item in self.expenseDict['income'])
        total_expense = sum(item["Amount"] for item in self.expenseDict['expense'])

        print("Total Income\t:\t", total_income)
        print("Total Expenses\t:\t", total_expense)

tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Calculate Totals")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        type = input("Enter transaction type (income/expense): ")
        amt = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        date = input("Enter the date: ")
        details = input("Enter transaction details: ")
        tracker.store_transaction(type, amt, category, date, details)
        print("Transaction added successfully.")

    elif choice == '2':
        tracker.view_transactions()

    elif choice == '3':
        tracker.calculate_transactions()

    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid ch1oice. Please select a valid option.")
