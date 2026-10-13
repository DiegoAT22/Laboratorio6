
class MyException(Exception):
    pass


class ExceptionsDemo:

    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except TypeError:
            print("Error: Invalid data type for division.")

    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except IndexError:
            print("Error: Index out of range.")
        except TypeError:
            print("Error: Invalid list or index type.")

    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
        except KeyError:
            print("Error: Key not found.")
        except TypeError:
            print("Error: Invalid dictionary or key type.")

    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("Error: File not found.")
        except OSError:
            print("Error: File reading or writing error.")

    def access_attribute(self, obj):
        try:
            print(obj.tnonexistent_attribue)
        except AttributeError:
            print("Error: Attribute does not exist.")

    def check_positive(self, number):
        try:
            if number < 0:
                raise MyException("The number must be positive.")
            else:
                print("Valid number:", number)
        except MyException as e:
            print("Custom error:", e)
        except TypeError:
            print("Error: Invalid number type.")
