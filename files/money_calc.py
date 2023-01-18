class Money:
    def round_and_format_amount(self, amount: float) -> str:
        """
        Rounded the amount to 2 decimal places and format it as a string.
        If the rounded amount is greater than or equal to 1, it returns "${:.2f}" format.
        Otherwise, it returns "{:.0f} cents" format.
        """
        rounded_amount = round(amount, 2)
        if rounded_amount >= 1:
            return "${:.2f}".format(rounded_amount)
        else:
            return "{:.0f} cents".format(rounded_amount * 100)

    def calculate_price_per_pound(self, price: float, pounds: float) -> str:
        """
        Calculate the price per pound of a product
        """
        return self.round_and_format_amount(price * pounds)

    def part_of_whole_percentage(self, whole: float, part: float) -> str:
        """
        Calculate the percentage of the part to the whole
        """
        return f"{(part / whole)*100}%"
    
    def percent_of_number(self, percent: float, number: float) -> str:
        """
        Calculate the value of a percent of a number
        """
        return self.round_and_format_amount((percent/100) * number)

money = Money()
print(money.calculate_price_per_pound(1.73, 2.6))
print(money.part_of_whole_percentage(520, 494))
print(money.percent_of_number(6, 95))
