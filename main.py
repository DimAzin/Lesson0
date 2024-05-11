
def test_param(value, *types, text="Book", **values):
     print("Value: ", value)
     print("*types: ", *types)
     print("types: ", types)
     print("Text: ", text)
     print("Values: ")
     for key, value in values.items():
        print(key, value)

test_param("Пример использования параметров всех типов", 2, 3, 4, text1="Article", text="Newspaper", theme="About Python")

def factorial(n):
     if n == 1:
          return 1
     else:
          return n * factorial(n - 1)

print(factorial(7))
