# uses Stack data structure to implement number conversion
from stack import Stack
import pyinputplus as pyip

number_to_convert = pyip.inputInt(prompt="Enter number to convert : ")
user_choice = pyip.inputMenu(
    ["Decimal to Binary", "Decimal to Hexadecimal"],
    numbered=True,
    prompt="Enter operation to perform : \n",
)


def decimal_to_binary(number_to_convert):
    myStack = Stack()
    while number_to_convert > 0:
        myStack.push(str(number_to_convert % 2))
        number_to_convert = number_to_convert // 2
    final_solution = myStack.viewItems()

    return "".join(final_solution)


def decimal_to_hexadecimal(number_to_convert):
    myStack = Stack()
    hexadecimal_values = "0123456789ABCDEF"
    while number_to_convert > 0:
        number_to_check = ((number_to_convert / 16) - (number_to_convert // 16)) * 16
        myStack.push(str(hexadecimal_values[int(number_to_check)]))
        number_to_convert = number_to_convert // 16
    final_solution = myStack.viewItems()

    return "".join(final_solution)


if user_choice == "Decimal to Binary":
    print(
        f"Number {number_to_convert} to binary form is  : =====>\n\t",
        decimal_to_binary(number_to_convert),
    )

if user_choice == "Decimal to Hexadecimal":
    print(
        f"Number {number_to_convert} in hexadecimal form is : \n\t ======>",
        decimal_to_hexadecimal(number_to_convert),
    )
