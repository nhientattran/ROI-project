import datetime
from IPython.display import clear_output as clear

current_time = datetime.datetime.now()

class Roi_calculator():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.investment = 0
        self.cash_on_cash = 0

    def income_cal(self):
        while True:
            if current_time.hour < 12:
                print("Good morning, welcome to our ROI calculator. With this application, we can help you to calculate your Return On Investment (ROI)! Let's do this!\n")
            elif current_time.hour <= 18:
                print("Good afternoon, welcome to our ROI calculator. With this application, we can help you to calculate your Return On Investment (ROI)! Let's do this!\n")
            else:
                print("Good evening, welcome to our ROI calculator. With this application, we can help you to calculate your Return On Investment (ROI)! Let's do this!\n")
            rental_income = input("First, enter your Rental income: ")
            if rental_income.isdigit() == False:
                print("Please enter numbers! Try again.")
            else:
                rental_income = int(rental_income)
                print("Thank you!")
                self.income += rental_income
                break
        while True:
            income_choice = input("Enter your side income(s)('Laundry', 'Storage' or 'Misc'). If you don't have, please enter 'No' to continue: ").lower()
            if income_choice == 'laundry':
                laundry_income = input("Please enter your Laundry Income: ")
                while True:
                    if laundry_income.isdigit() == False:
                        print("Please enter numbers! Try again.")
                    else:
                        laundry_income = int(laundry_income)
                        print("Thank you! We received your Income Information.")
                        self.income += laundry_income
                    break
            elif income_choice == 'storage':
                storage_income = input("Please enter your Storage Income: ")
                while True:
                    if storage_income.isdigit() == False:
                        print("Please enter numbers! Try again.")
                    else:
                        storage_income = int(storage_income)
                        print("Thank you! We received your Income Information.")
                        self.income += storage_income
                    break
            elif income_choice == 'misc':
                misc_income = input("Please enter your Misc Income: ")
                while True:
                    if misc_income.isdigit() == False:
                        print("Please enter numbers! Try again.")
                    else:
                        misc_income = int(misc_income)
                        print("Thank you! We received your Income Information.")
                        self.income += misc_income
                    break
            elif income_choice == 'no':
                clear()
                print("Great! Let's continue to the next step to calculate your Expenses.\n")
                break
            else:
                print("Please enter 'Laundry Income' or 'Storage Income' or 'Misc Income', or 'No' to continue: ")
        self.expenses_cal()
    
    def expenses_cal(self):
        expenses_list = ['taxes', 'insurance', 'water/sewer', 'garbage', 'electric', 'gas', 'hoa fees', 'lawn/snow', 'vacancy', 'maintainances', 'property management', 'mortgage']
        expenses_rental_list = ['taxes', 'insurance', 'hoa fees', 'vacancy', 'property management', 'mortgage']
        expenses_dic = {}
        while True:
            expenses_choice = input('For this step, we would like to know if you do Airbnb or rental house. Please enter Airbnb if you do Airbnb, or Rental if you do Rental house: ').lower()
            if expenses_choice == 'airbnb':
                print (f"For Airbnb, this is your expenses list: {expenses_list}")
                while True:
                    expenses_remove = input("Do you not have to pay any expenses in that list? Please enter it, enter 'No' if that list is correct: ")
                    if expenses_remove == 'no':
                        break
                        clear()
                    else:
                        if expenses_remove in expenses_list:
                            clear()
                            expenses_list.remove(expenses_remove)
                            print(f'Here is your updated expenses list: {expenses_list}')
                        else:
                            print('You enter the wrong expense, please try again.')
                while True:
                    for i in range(len(expenses_list)):
                        expenses_dic[expenses_list[i]] = input(f"Please enter your {expenses_list[i]}: ")
                        if expenses_dic[expenses_list[i]].isdigit() == True:
                            print(f"Thank you! Your information has been saved!")
                        else:
                            print('Please enter numbers. Try again!')
                    clear()
                    print ("Thank you! Let's move to the next step!")
                    for value in expenses_dic.values():
                        self.expenses += int(value)
                    break
                break
            if expenses_choice == "rental":
                print(f"For Rental House, we assume that you only need to pay these expenses: {expenses_rental_list}")
                while True:
                    expenses_rental_remove = input("Do you not have to pay any expenses in that list? Please enter it, enter 'No' if that list is correct: ")
                    if expenses_rental_remove == 'no':
                        break
                        clear()
                    else:
                        if expenses_rental_remove in expenses_rental_list:
                            clear()
                            expenses_rental_list.remove(expenses_rental_remove)
                            print(f'Here is your updated expenses list: {expenses_rental_list}')
                        else:
                            print ("You entered the wrong expense! Please try again.")
                while True:
                    for i in range(len(expenses_rental_list)):
                        expenses_dic[expenses_rental_list[i]] = input(f"Please enter your {expenses_rental_list[i]}: ")
                        if expenses_dic[expenses_rental_list[i]].isdigit() == True:
                            clear()
                            print(f"Thank you! Your {expenses_rental_list[i]} information has been saved!")
                        else:
                            print('Please enter numbers. Try again!')
                    clear()
                    print ("Thank you! Let's move to the next step!")
                    for value in expenses_dic.values():
                        self.expenses += int(value)
                    break
                break
            else:
                print("Please enter 'Airbnb' for AirBnB or 'Rental' for Rental House! Try again.")
                continue
        self.cash_cal()
    
    def cash_cal(self):
        cash = self.income - self.expenses
        self.cash_flow = cash * 12
        print (f"As we calculated, your Total Monthly Income is: ${self.income} and your Total Monthly Expenses is ${self.expenses}.\nAs a result, your Total Monthly Cashflow is: ${cash}.\nYour Annual Cash Flow is: ${self.cash_flow}.\n")
        # print (f"As a result, your Total Monthly Cashflow is: ${cash}\n")
        # print (f"Your Annual Cash Flow is: ${self.cash_flow}.\n")
        self.cash_return()
    
    def cash_return(self):
        print("""
        For this last step, we would like to know your:
        - Down Payment Amount
        - Closing Costs
        - Rehab Budget
        - Misc Other
        """)
        while True:
            down_payment = input("Please enter your Down Payment Amount: ")
            if down_payment.isdigit() == True:
                print('Thank you!')
                down_payment = int(down_payment)
                self.investment += down_payment
                break
            else:
                print("Please enter numbers or 'No' to continue! Try again.")
        while True:
            closing_cost = input("Please enter your Closing Cost: ")
            if closing_cost.isdigit() == True:
                print('Thank you!')
                closing_cost = int(closing_cost)
                self.investment += closing_cost
                break
            else:
                print("Please enter numbers or 'No' to continue! Try again.")
        while True:
            rehab_budget = input("Please enter your Rehab Budget, you can enter 'No' if you do not have it: ").lower()
            if rehab_budget == "no":
                print ("Thank you!")
                break
            elif rehab_budget.isdigit() == True:
                print('Thank you!')
                rehab_budget = int(rehab_budget)
                self.investment += rehab_budget
                break
            elif rehab_budget.isdigit() == False:
                print("Please enter numbers or 'No' to continue! Try again.")
        while True:
            other = input("Please enter other Investments that you have put down, you can enter 'No' if you dont have it: ").lower()
            if other == 'no':
                print("Thank you!")
                break
            elif other.isdigit() == True:
                print('Thank you!')
                other = int(other)
                self.investment += other
                break
            elif other.isdigit() == False:
                print("Please enter numbers! Try again.")
        print (f"As we calculated, your Total Investment is ${self.investment}")
        self.cash_on_cash = (self.cash_flow / self.investment) * 100
        print (f"Your Cash on Cash return is ${self.cash_on_cash}. Thank you for using our application!")


class Main():
    def run():
        user = Roi_calculator()
        user.income_cal()

Main.run()
 
