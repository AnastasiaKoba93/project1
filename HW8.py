class PlaceHolder:
    pass


class MyClass:
    def __init__(self, parameter):
        self.parameter = parameter

    def print_parameter(self):
        print(self.parameter)

    @staticmethod
    def static_method():
        print("This is a static method")


class MyDerivedClass(MyClass):
    def __init__(self, parameter1, parameter2):
        super().__init__(parameter1)
        self.parameter2 = parameter2

    def print_parameter2(self):
        print(self.parameter2)


placeholder = PlaceHolder()
my_obj = MyClass("Hello")
my_obj.print_parameter()
my_obj.static_method()

derived_obj = MyDerivedClass("World", "OpenAI")
derived_obj.print_parameter()
derived_obj.print_parameter2()
derived_obj.static_method()