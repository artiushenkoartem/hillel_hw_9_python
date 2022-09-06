"""1)Задачи на функцию all()
    Создать пример со значениями True и False.
    Создать пример со значениями заменяющими True False.
    Любой объект в пайтон можно представить
    как бул объект. Пример bool( [ ] ) -> False"""
"""function all() returns True if all items in an iterable are true,
otherwise it returns False"""
# all() True :
my_list: list = [1, 2, 3]
print("all() my_list: ")
print(all(my_list))

# all() False :
my_dict: dict = {0: "first", 1: "second"}
print("all() my_dict: ")
print(all(my_dict))

# example with True replacement
print("all() : ")
print(all([bool([1, 2, 3]), bool('asdf'), bool(1)]))

# example with False replacement
print("all() : ")
print(all([bool([]), bool(''), bool(0)]))
