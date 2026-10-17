def greet(name="Student"):
    return f"Hello, {name}!"
def add(a, b):
    return a + b
def square(n):
    return n * n
def is_even(n):
    return n % 2 == 0
def introduce(name, age):
    return f"My name is {name} and I am {age} years old"
print(greet("ALAUDDIN"))
print(greet())
print(add(5, 7))
print(square(6))
print(is_even(10), is_even(7))
print(introduce(age=21, name="ALAUDDIN"))
result = add(2, 3) * square(2)
print(result)