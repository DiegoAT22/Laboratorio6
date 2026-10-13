
from Exceptions import ExceptionsDemo

demo = ExceptionsDemo()

print("=== DIVISION ===")
demo.divide(10, 0)
demo.divide("10", 2)
demo.divide(10, 2)

print("\n=== LISTAS ===")
demo.access_list([1, 2, 3], 5)
demo.access_list(1, 0)
demo.access_list([1, 2, 3], 1)

print("\n=== DICCIONARIOS ===")
demo.access_dict({"a": 1}, "b")
demo.access_dict(123, "a")
demo.access_dict({"a": 1}, "a")

print("\n=== ARCHIVOS ===")
demo.read_file("text_2.txt")
demo.read_file("text.txt")

print("\n=== ATRIBUTOS ===")
demo.access_attribute(object())

print("\n=== NUMEROS POSITIVOS ===")
demo.check_positive(-5)
demo.check_positive(10)

print("\nPROGRAMA FINALIZADO CORRECTAMENTE")
