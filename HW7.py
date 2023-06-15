
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print([fibonacci(n) for n in range(10)])



def sum_range(start, end):
    if start > end:
        start, end = end, start

    total = 0
    for num in range(start, end + 1):
        total += num

    return total

start = 5
end = 10
result = sum_range(start, end)
print(result)


def season(month):
    if month in [1, 2, 12]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return "error"
print(season(3))


def get_filtered(a):
    for element in a:
        if element < 5:
            print(element)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
get_filtered(a)



