import csv
import json

with open('SampleCSVFile_11kb.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        print(line)


data = {
   "firstName": "Joe",
   "lastName": "Jackson",
   "gender": "male",
   "age": 28,
   "address": {
       "streetAddress": "101",
       "city": "San Diego",
       "state": "CA"
   },
   "phoneNumbers": [
       { "type": "home", "number": "7349282382" }
   ]
}

json_string = json.dumps(data)
print(json_string)


try:
    a = 10
    b = 0
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Division by zero is impossible .")
except Exception as e:
    print(f"Error: {e}")



try:
    my_list = [1, 2, 3, 4, 5]
    index = 10
    value = my_list[index]
    print(f"Element with index {index}: {value}")
except IndexError:
    print(f"Element with index {index} does not exist .")
except Exception as e:
    print(f"Error : {e} ")

