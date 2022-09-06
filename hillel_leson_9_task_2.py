"""2)Задачи на функцию any()
    Повторить примеры как в функции all()."""
"""function any() returns True if any item in an iterable are true,
otherwise it returns False"""
# any() True :
my_list: list = [0, 2, 0]
print("any() my_list: ")
print(any(my_list))

# any() False :
my_dict: dict = {0: "first", False: "second"}
print("any() my_dict: ")
print(any(my_dict))


# example with False replacement
print(any([bool([]), bool(''), bool(0)]))

# example with True replacement
print(any([bool([]), bool(''), bool(1)]))
