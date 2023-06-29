
print_symbol = lambda symbol, count=100: print(symbol * count)
print_symbol('*')
print_symbol("123", 5)


max_number = lambda x, y: x if x > y else y
result = max_number(8, 5)
print(result)


return_10 = lambda: 10
result = return_10()
print(result)



def make_bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def make_italic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper

def make_underline(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"
    return wrapper

@make_bold
@make_italic
@make_underline
def hello_world():
    return "hello world"

result = hello_world()
print(result)



lst1 = [44, 54, 64, 74, 104]

lst2 = [x + 6 for x in lst1]

print(lst2)


lst3 = [2, 4, 6, 8, 10, 12, 14]

lst4 = [x**2 for x in lst3 ]

print(lst4)


car_dict = {
    "Sedan": 1500,
    "SUV": 2000,
    "Pickup": 2500,
    "Minivan": 1600,
    "Van": 2400,
    "Semi": 13600,
    "Bicycle": 7,
    "Motorcycle": 110
}
cars = [cars.upper() for cars, weight in car_dict.items() if weight <= 5000]

print(cars)





