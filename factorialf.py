def factorial(n:int):
    fact = 1
    i = 1 
    while i <= n:
        fact *= i
        i = i + 1
    return fact

print(factorial(int(input("Введите число\n"))))