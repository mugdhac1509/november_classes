class IOString:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.strl = input("Enter String: ")

    def print_String(self):
        print("Result is :", self.strl.upper())

str1 = IOString()

str1.get_String()
str1.print_String()