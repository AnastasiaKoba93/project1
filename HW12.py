
with open("file.txt", "w") as file:
    file.write("Hello, world!")


with open("file.txt", "r") as file:
    content = file.read()
    print(content)


with open("file.txt", "a") as file:
    file.write("\nThis is an additional line.")


with open("file.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())


with open("file.txt", "a") as file:
    while True:
        user_input = input()
        if user_input == "exit":
            break
        file.write(user_input + "\n")
