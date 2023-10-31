# 1. Create a simple calculus program as a script and as module.

# # import calc as calculator
# from calc import add

# a = 2 
# b = 2

# # result = calculator.add(a, b)
# result = add(a, b)

# print(result)

# 2.Create a program with 3 different modules:
# first, to do basic tasks with strings
# second, basic tasks with lists.
# third, basic tasks with numbers
# Import them as modules to the main.py module and show calculations.

# from strings import string_reverse
# import lists
# from numberz import square, root

# my_list: list = [1, 2, 3, 4, 5]

# print(string_reverse("Laba diena"))
# print(lists.list_length(my_list))
# print(lists.list_append(my_list, 7))
# print(square(5))
# print(root(49))


# 3. Create a module and import any PIP package of your choice. Then create a function that would use it. Import that function to the main.py module and use it.
# pasirasyti pythono funkcija kuri ijungs webcam

import open_webcam

open_webcam.show_webcam()

