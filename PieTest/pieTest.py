# ROI Project - Coding Temple - April 11, 2022 - Michael Cook
# Changes I would like to make:
# Put all my functions in one class to be accessed by all other classes
# Re size buttons to fit to screen
# Debug Math

import tkinter as tk
from tkinter import ttk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
LARGEFONT =("Verdana", 35)
  
class ROI_Calculator(tk.Tk):
     
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.monthly_income = {"rental income":0,"laundry":0,"storage":0,"misc.":0}
        self.monthly_expenses = {"tax":0,"insurance":0,"electrical":0,"water":0,"gas":0,
        "sewer":0,"home owner association":0,"gardening":0,"vacancy":0,"repairs":0,"property management":0,
        "mortgage":0}
        self.investment = {"down payment":0,"closing costs":0,"rehab budget":0,"misc.":0}
        self.monthly_cash_flow = 0
        self.roi = 0
        self.dict_name = {}
        self.display_dict_name = ''
        self.pie_chart_label = []
        self.pie_chart_value = []
        self.plzwork = 1
         
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {} 

        for F in (Calculate, Monthly_Expenses, Monthly_Income, Investment):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Calculate)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
class Calculate(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        # Displays 
        self.pie_chart()
        self.dict_display()
         

        # label.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan=4)
  
        # My Buttons!
        button_expenses = ttk.Button(self, text ="Expenses",command = lambda : controller.show_frame(Monthly_Expenses))
        button_expenses.grid(row = 2, column = 0, padx = 10, pady = 10)
        button_income = ttk.Button(self, text ="Income", command = lambda : controller.show_frame(Monthly_Income))
        button_income.grid(row = 2, column = 1, padx = 10, pady = 10)
        button_investment = ttk.Button(self, text ="Investment",command = lambda : controller.show_frame(Investment))
        button_investment.grid(row = 2, column = 2, padx = 10, pady = 10)
    
    def pie_chart(self):
        pie_display = Figure(figsize=(5,5), dpi=100,) 
        subplot2 = pie_display.add_subplot(111) 
        labels2 = ['Return on Investment', 'Total Investment'] 
        pieSizes = [self.controller.plzwork - (self.controller.monthly_cash_flow * 12), self.controller.monthly_cash_flow * 12]
        my_colors2 = ['lightblue','lightsteelblue','silver']
        subplot2.pie(pieSizes, colors=my_colors2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) 
        subplot2.axis('equal')  
        one_pie = FigureCanvasTkAgg(pie_display, self)
        one_pie.get_tk_widget().grid(row = 1, column = 0, padx = 10, pady = 5, columnspan=2)
    def dict_display(self):
        message = f"""\n
Total Monthly Income = ${sum(self.controller.monthly_income.values()) : .2f}
                
Total Monthly Expenses = ${sum(self.controller.monthly_expenses.values()) : .2f}
    Monthly Cash Flow = ${self.controller.monthly_cash_flow : .2f}
                
Total Investment = ${sum(self.controller.investment.values()) : .2f}
    Return on Investment = {self.controller.roi : .2f}%
                    """
        text_box = Text(self, height=29, width=50)
        text_box.grid(row = 1, column = 2, columnspan=2, padx = 5, pady = 5)
        text_box.insert('end', message)
        text_box.config(state='disabled')

    def do_math(self):
        
        self.controller.monthly_cash_flow = sum(self.controller.monthly_income.values()) -  sum(self.controller.monthly_expenses.values())
        self.controller.plzwork = int(sum(self.controller.investment.values()))
        print(self.controller.plzwork)
        
        try:
            self.controller.roi = (self.controller.monthly_cash_flow * 12) / sum(self.controller.investment.values()) * 100
        except:
            self.controller.roi = 0

class Monthly_Income(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller 
        tk.Frame.__init__(self, parent)
        self.str_changer = StringVar()
        self.num_changer = DoubleVar()

        # Calculator Display
        self.calc_display()
        
        # Page Title 
        label = ttk.Label(self, text ="Total Monthly Income", font = LARGEFONT)
        label.grid(row = 0, column = 0, columnspan= 3, padx = 5, pady = 5)
        
        # Entry boxes for calculator
        Entry(self, textvariable = self.str_changer,justify = LEFT).grid(row = 2, column = 1)
        Entry(self, textvariable = self.num_changer,justify = LEFT).grid(row = 2, column = 2)
        
        # Calculator Buttons
        button_add = ttk.Button(self, text ="Add", command = self.calc_add)
        button_add.grid(row = 3, column = 1, sticky=N+S+E+W)
        
        button_subtract = ttk.Button(self, text ="Subtract", command = self.calc_subtract)
        button_subtract.grid(row = 3, column = 2, sticky=N+S+E+W, ipady=20, ipadx=20)
        
        button_calculate = ttk.Button(self, text ="Calculate",command = lambda : controller.show_frame(Calculate))
        button_calculate.grid(row = 4, column = 1, sticky=N+S+E+W, ipady=20, ipadx=20)
        
        button_expenses = ttk.Button(self, text ="Expenses",command = lambda : controller.show_frame(Monthly_Expenses))
        button_expenses.grid(row = 5, column = 1, sticky=N+S+E+W, ipady=20, ipadx=20)

        button_investment = ttk.Button(self, text ="Investment",command = lambda : controller.show_frame(Investment))
        button_investment.grid(row = 5, column = 2, sticky=N+S+E+W, ipady=20, ipadx=20)


    def calc_display(self):
        message = ''
        for x,y in self.controller.monthly_income.items():
            message += f"\n{x.title()}  :  ${y : .2f}"

        text_box = Text(self, height=40, width=50)
        text_box.grid(row = 1, column = 0,rowspan = 5, padx = 5, pady = 5)
        text_box.insert('end', message)
        text_box.config(state='disabled')

    def calc_add(self):
        if self.str_changer.get().lower() in self.controller.monthly_income:
            try:
                self.controller.monthly_income[self.str_changer.get().lower()] += self.num_changer.get()
                self.calc_display()
                self.controller.frames[Calculate].do_math()
                self.controller.frames[Calculate].dict_display()
                self.controller.frames[Calculate].pie_chart()()
                print(self.controller.monthly_income[self.str_changer.get()])
            except:
                pass
        else:
            self.controller.monthly_income[self.str_changer.get()] = self.num_changer.get()

    def calc_subtract(self):        
        if self.str_changer.get() in self.controller.monthly_income:
            try:
                self.controller.monthly_income[self.str_changer.get()] -= self.num_changer.get()
                self.calc_display()
                self.controller.frames[Calculate].dict_display()
                print(self.controller.monthly_income[self.str_changer.get()])
            except:
                pass
        else:
            self.controller.monthly_income.pop(self.str_changer.get())
    
class Monthly_Expenses(tk.Frame):
     
    def __init__(self, parent, controller):
        self.controller=controller 
        tk.Frame.__init__(self, parent)
        self.calc_display()
        self.str_changer = StringVar()
        self.num_changer = DoubleVar()
        
        label = ttk.Label(self, text ="Total Monthly Expenses", font = LARGEFONT)
        label.grid(row = 0, column = 0, columnspan= 3, padx = 5, pady = 5)
        
        # Entry boxes for calculator
        Entry(self, textvariable = self.str_changer,justify = LEFT).grid(row = 2, column = 1)
        Entry(self, textvariable = self.num_changer,justify = LEFT).grid(row = 2, column = 2)
        
        # Calculator Buttons
        button_add = ttk.Button(self, text ="Add", command = self.calc_add)
        button_add.grid(row = 3, column = 1, sticky=N+S+E+W)
        
        button_subtract = ttk.Button(self, text ="Subtract", command = self.calc_subtract)
        button_subtract.grid(row = 3, column = 2, sticky=N+S+E+W, ipady=20, ipadx=20)
        
        button_calculate = ttk.Button(self, text ="Calculate",command = lambda : controller.show_frame(Calculate))
        button_calculate.grid(row = 4, column = 1, sticky=N+S+E+W, ipady=20, ipadx=20)
        
        button_expenses = ttk.Button(self, text ="Income",command = lambda : controller.show_frame(Monthly_Income))
        button_expenses.grid(row = 5, column = 1, sticky=N+S+E+W, ipady=20, ipadx=20)

        button_investment = ttk.Button(self, text ="Investment",command = lambda : controller.show_frame(Investment))
        button_investment.grid(row = 5, column = 2, sticky=N+S+E+W, ipady=20, ipadx=20)
        
    def calc_display(self):
        message = ''
        for x,y in self.controller.monthly_expenses.items():
            message += f"\n{x.title()}  :  ${y : .2f}"

        text_box = Text(self, height=40, width=50)
        text_box.grid(row = 1, column = 0,rowspan = 5, padx = 5, pady = 5)
        text_box.insert('end', message)
        text_box.config(state='disabled')

    def calc_add(self):
        if self.str_changer.get() in self.controller.monthly_expenses:
            try:
                self.controller.monthly_expenses[self.str_changer.get()] += self.num_changer.get()
                self.calc_display()
                self.controller.frames[Calculate].do_math()
                self.controller.frames[Calculate].dict_display()
                self.controller.frames[Calculate].pie_chart()()
                print(self.controller.monthly_expenses[self.str_changer.get()])
            except:
                pass
        else:
            self.controller.monthly_expenses[self.str_changer.get()] = self.num_changer.get()

    def calc_subtract(self):
        if self.str_changer.get() in self.controller.monthly_expenses:
            try:
                self.controller.monthly_expenses[self.str_changer.get()] -= self.num_changer.get()
                self.calc_display()
                self.controller.frames[Calculate].dict_display()
                print(self.controller.monthly_expenses[self.str_changer.get()])
            except:
                pass
        else:
            self.controller.monthly_expenses.pop(self.str_changer.get())

class Investment(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller 
        tk.Frame.__init__(self, parent)
        self.calc_display()
        self.str_changer = StringVar()
        self.num_changer = DoubleVar()
        
        # Page Title 
        label = ttk.Label(self, text ="Total Investment", font = LARGEFONT)
        label.grid(row = 0, column = 0, columnspan= 3, padx = 5, pady = 5)
        
        # Entry boxes for calculator
        Entry(self, textvariable = self.str_changer,justify = LEFT).grid(row = 2, column = 1)
        Entry(self, textvariable = self.num_changer,justify = LEFT).grid(row = 2, column = 2)
        
        # Calculator Buttons
        button_add = ttk.Button(self, text ="Add", command = self.calc_add)
        button_add.grid(row = 3, column = 1, sticky=N+S+E+W)
        
        button_subtract = ttk.Button(self, text ="Subtract", command = self.calc_subtract)
        button_subtract.grid(row = 3, column = 2, sticky=N+S+E+W, ipady=20, ipadx=20)
        
        button_calculate = ttk.Button(self, text ="Calculate",command = lambda : controller.show_frame(Calculate))
        button_calculate.grid(row = 4, column = 1, sticky=N+S+E+W, ipady=20, ipadx=20)
        
        button_expenses = ttk.Button(self, text ="Expenses",command = lambda : controller.show_frame(Monthly_Expenses))
        button_expenses.grid(row = 5, column = 1, sticky=N+S+E+W, ipady=20, ipadx=20)

        button_investment = ttk.Button(self, text ="Income",command = lambda : controller.show_frame(Monthly_Income))
        button_investment.grid(row = 5, column = 2, sticky=N+S+E+W, ipady=20, ipadx=20)

    def calc_display(self):
        message = ''
        for x,y in self.controller.investment.items():
            message += f"\n{x.title()}  :  ${y : .2f}"

        text_box = Text(self, height=40, width=50)
        text_box.grid(row = 1, column = 0,rowspan = 5, padx = 5, pady = 5)
        text_box.insert('end', message)
        text_box.config(state='disabled')

    def calc_add(self):
        if self.str_changer.get() in self.controller.investment:
            try:
                self.controller.investment[self.str_changer.get()] += self.num_changer.get()
                self.calc_display()
                self.controller.frames[Calculate].do_math()
                self.controller.frames[Calculate].dict_display()
                self.controller.frames[Calculate].pie_chart()()
                print(self.controller.investment[self.str_changer.get()])
            except:
                pass
        else:
            self.controller.investment[self.str_changer.get()] = self.num_changer.get()

    def calc_subtract(self):
        if self.str_changer.get() in self.controller.investment:
            try:
                self.controller.investment[self.str_changer.get()] -= self.num_changer.get()
                self.calc_display()
                self.controller.frames[Calculate].dict_display()
                print(self.controller.investment[self.str_changer.get()])
            except:
                pass
        else:
            self.controller.investment.pop(self.str_changer.get())


# Driver Code
def main(): 
    root = ROI_Calculator()
    root.geometry("800x600")
    root.title('Cookie\'s ROI Calculator')
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()