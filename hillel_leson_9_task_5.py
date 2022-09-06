"""5)Написать функцию бутерброд внутри себя определяет другую функцию колбаса и возвращает
    ее объект(Пожалуйста не результат выполнения функции, а именно объект функции).
    Функции – это объекты: атрибуты и аннотации
    Косвенный вызов функций """
# defined function sandwich
def sandwich():
    # inside defined function sausage
    def sausage():
        pass
    # return object of sausage
    return sausage
print(sandwich())
