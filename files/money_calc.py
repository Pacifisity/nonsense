class Money:
    def __init__(self):
        self.payroll = Payroll()

    def round_and_format_amount(self, amount: float) -> str:
        # Rounded the amount to 2 decimal places and format it as a string.
        # If the rounded amount is greater than or equal to 1, it returns "${:.2f}" format.
        # Otherwise, it returns "{:.0f} cents" format.
        if amount >= 1:
            return f"${amount:,.2f}"
        else:
            return f"{amount * 100:.0f} cents"

    def calculate_price_per_pound(self, price: float, pounds: float) -> str:
        # Calculate the price per pound of a product
        return self.round_and_format_amount(price * pounds)

    def part_of_whole_percentage(self, whole: float, part: float) -> str:
        # Calculate the percentage of the part to the whole
        return f"{round((part / whole)*100)}%"
    
    def percent_of_number_percentage(self, percent: float, number: float) -> str:
        # Calculate the value of a percent of a number
        return self.round_and_format_amount((percent / 100) * number)
    
    def calculate_salary_plus_comission(self, salary: float, comission_percentage: float, sold_products: float):
        return f"${salary + round(sold_products * (comission_percentage/100), 2)}"

    def calculate_is_of(self, string):
        # Var init
        is_index = string.find("is")
        of_index = string.find("of")
        if is_index == -1 or of_index == -1:
            return None
        is_num = ""
        of_num = ""

        # Find the numbers near is and of
        for i in range(is_index + 3, len(string)): # start from index after "is "
            if string[i].isnumeric() or string[i] == ".":
                is_num += string[i]
            else:
                break

        for i in range(of_index + 3, len(string)): # start from index after "of "
            if string[i].isnumeric() or string[i] == ".":
                of_num += string[i]
            else:
                break
        
        # No instance of is or of
        if is_num == "" or of_num == "":
            return None

        is_num = float(is_num)
        of_num = float(of_num)

        # Divide by zero prevention
        if of_num == 0:
            return None

        # Check for percentage
        if '%' in string[is_index:]:
            return f"{(is_num * of_num)/100}"
        else:
            return f"{(is_num / of_num)*100:.2f}%"

class Payroll:
    def __init__(self):
        self.biweekly = 26
        self.semimonthly = 24
    
    # Calculates pay given the hour and rate then formats it as a string
    def calculate_pay(self, hours: float, rate: float):
        if hours > 40:
            total_pay = self.calculate_overtime(hours, rate)
        else:
            total_pay = hours * rate

        if total_pay == round(total_pay):
            return f"${round(total_pay)}"
        else:
            return f"${round(total_pay, 2)}"
    
    # Calculate's overtime pay given the hour and rate then returns it as a number
    def calculate_overtime(self, hours: float, rate: float):
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        total_pay = regular_pay + overtime_pay
        return total_pay

    # Calculates the hourly rate given the amount in hours and the gross pay
    def calculate_hourly_rate(self, hours: float, gross: float):
        return f"${round(gross / hours, 2)}/hr"

money = Money()

question1 = money.payroll.calculate_pay(3*3, 17.15)
question2 = money.payroll.calculate_hourly_rate(8+7+5+1+8, 617.09)
question3 = money.payroll.calculate_pay(43, 23.44)
question4 = money.part_of_whole_percentage(134, 14)
question5 = money.calculate_salary_plus_comission(1815, 4, 9283)

print(f"1: {question1}\n2: {question2}\n3: {question3}\n4: {question4}\n5: {question5}")
