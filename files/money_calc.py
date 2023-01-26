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

    # Calculates taxes given gross and returns net after fica and medicare taxes
    def calculate_taxes(self, gross: float):
        social_security = 1 - 0.062
        medicare = 1 - 0.0145

        # social security tax calculations
        social_security_taxes = gross - (gross * social_security)
        print(f"Social Security Taxes: {round(social_security_taxes, 2)}")

        # medicare tax calculations
        medicare_taxes = gross - (gross * medicare)
        print(f"Medicare Taxes: {round(medicare_taxes, 2)}")

        # Evaluates net after adding up all fica taxes
        fica_taxes = social_security_taxes + medicare_taxes
        net = gross - fica_taxes

        if net == round(net):
            return f"${round(net)}"
        else:
            return f"${round(net, 2)}"


money = Money()
payroll = money.payroll
# result = money.payroll.calculate_pay(40, 14)
result = money.payroll.calculate_taxes(944)
print(result)
