class Money:
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
        return f"{(part / whole)*100:.2f}%"
    
    def calculate_percentage_of_number(self, percent: float, number: float) -> str:
        # Calculate the value of a percent of a number
        return self.round_and_format_amount((percent / 100) * number)

    def calculate_is_of(self, string):
        is_index = string.find("is")
        of_index = string.find("of")
        if is_index == -1 or of_index == -1:
            return None
        is_num = ""
        of_num = ""

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

        if is_num == "" or of_num == "":
            return None

        is_num = float(is_num)
        of_num = float(of_num)

        if of_num == 0:
            return None

        if '%' in string[is_index:]:
            return f"{(is_num * of_num)/100}"
        else:
            return f"{(is_num / of_num)*100:.2f}%"

money = Money()
# print(money.calculate_price_per_pound(1.73, 0.3))
# print(money.part_of_whole_percentage(120, 42))
# print(money.calculate_percentage_of_number(65, 1150))
question = input("Question:\n")
calculation = money.calculate_is_of(question)
print(calculation)
