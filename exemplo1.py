def divide(a, b):
      return a/b  
# Executando o código
try:
    result = divide(10, 0)
    print("Resultado:", result)
except ZeroDivisionError as e:
        print("Failure: Divisão por zero!")
