# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


# lambda arguments : expression

x = lambda a : a + 10 # x is a pointer on function
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))