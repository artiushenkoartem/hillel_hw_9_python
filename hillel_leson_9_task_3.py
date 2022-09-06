"""3)Задачи на функцию isinstance()
    Создать примеры со всеми известными вами объектами в пайтон."""
"""The isinstance() function returns True if the specified object
is of the specified type, otherwise False. If the type parameter is a tuple
the function will return True if the object is one of the types in the tuple"""
my_list = [1, 2, 3]
my_dict = {0: 'first', 1: 'second'}
my_tuple = (1, 2, 3)

print("Examples: ")
example_int = isinstance(5, int)
print(example_int)
example_float = isinstance(5.1, float)
print(example_float)
example_str = isinstance('str', str)
print(example_str)
example_dict = isinstance(my_dict, dict)
print(example_dict)
example_list = isinstance(my_list, list)
print(example_list)
example_tuple = isinstance(my_tuple, tuple)
print(example_tuple)


example_var = isinstance("Hello", (float, int, str, list, dict, tuple))
print(example_var)


class myObj:
    name = "John"
y = myObj()
print(isinstance(y, myObj))
