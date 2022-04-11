# Frame is built, need to edit in proper outputs, math, and add two buttons! Otherwise
# framework is in! Also need to add in possible methods for MATH, API, 

from matplotlib import pyplot as plt
import numpy as np

class ROI():
# Initializing variables used to run ROI
    def __init__(self):
        self.monthly_income = {"Rental Income":0,"Laundry":0,"Storage":0,"Misc.":0}
        self.monthly_expenses = {"Tax":0,"Insurance":0,"Electrical":0,"Water":0,"Gas":0,
        "Sewer":0,"HOA":0,"Gardening":0,"Vacancy":0,"Repairs":0,"Property Management":0,
        "Mortgage":0}
        self.investment = {"Down Payment":0,"Closing Costs":0,"Rehab Budget":0,"Misc. Other":0}
        self.monthly_cash_flow = 0
        self.roi = 0
        self.dict_name = {}
        self.display_dict_name = ''
        self.pie_chart_label = []
        self.pie_chart_value = []


    def run(self):
        print("""              
              Welcome to Cookie's ROI Calculator
(please use the letters in the parenthesis for what you would like to edit)                    
        """)
        running = True

# While loop for my Landing Menu
        while running:
            self.do_math()
            print(f"""\n
                Total Monthly Income(I) = ${sum(self.monthly_income.values()) : .2f}
                
                Total Monthly Expenses(E) = ${sum(self.monthly_expenses.values()) : .2f}
                    Total Monthly Cash Flow = ${self.monthly_cash_flow : .2f}
                
                Total Investment(T) = ${sum(self.investment.values()) : .2f}
                    Return on Investment = {self.roi : .2f}%
            
                Quit(Q)
            """)
            user_option = input("What would you like to edit? ")
            if user_option.lower() == "i":
                self.dict_name = self.monthly_income
                self.display_dict_name = "monthly income"
                self.edit_dict()
            elif user_option.lower() == "e":
                self.dict_name = self.monthly_expenses
                self.display_dict_name = "monthly expenses"
                self.edit_dict()
            elif user_option.lower() == "t":
                self.dict_name = self.investment
                self.display_dict_name = "investment"
                self.edit_dict()
            elif user_option.lower() == "q":
                print("Thank you for using Cookie's Calculator!")
                running = False
            else:
                print("This is not a valid choice.")

# Menu for adding and removing from dictionaries 
    def edit_dict(self):
        running = True
        while running:
            
            for x,y in self.dict_name.items():
                print(f"{x}  :  ${y : .2f}")
            print(f"Your total {self.display_dict_name} is ${sum(self.dict_name.values()) : .2f}")
            print(f"""
                {self.display_dict_name}
            
            (Add) to {self.display_dict_name}
            (Remove) from {self.display_dict_name}
            
            (Back) to calculate
            """)
            what_to_do = input("What would to do? ")

            if what_to_do.lower() == "add":
                self.dict_add()                    
            elif what_to_do.lower() == "remove":
                self.dict_remove()                 
            elif what_to_do.lower() == "back":
                running = False
            else:
                print("This is not a valid option.")

# Add Button
    def dict_add(self):
        add = input("What would you like to add/change? ")
        num = input(f"How much would you like to add to {add}? ")
        try:
            if "," or "$" in num:
                num = num.replace(',', '')
                num = num.replace('$', '')
            if add in self.dict_name:
                self.dict_name[add] += float(num)
            else:
                self.dict_name[add] = float(num)
        except:
            print("This is not a valid option")

# Remove Button
    def dict_remove(self):
        remove = input("What would you like to remove? ")
        
        if remove in self.dict_name:
            num = input(f"How much would you like to remove from {remove}? ")
            if "," or "$" in num:
                num = num.replace(',', '')
                num = num.replace('$', '')
            self.dict_name[remove] -= float(num)
            if self.dict_name[remove] <= 0:
                self.dict_name.pop(remove)
        else:
            print(f"{remove} is not on the list of {self.display_dict_name}")

    def do_math(self):
        
        self.monthly_cash_flow = sum(self.monthly_income.values()) -  sum(self.monthly_expenses.values())
        try:
            self.roi = (self.monthly_cash_flow * 12) / sum(self.investment.values()) * 100
        except:
            self.roi = 0



ROI().run()