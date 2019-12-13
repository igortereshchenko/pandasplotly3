# This ability of lambdas to be invoked immediately allows you to use them inside functions like map() and reduce(). It is useful because you may not want to use these functions again.

sequences = [10,2,8,7,5,4,3,11,0, 1]

filtered_result = filter (lambda x: x > 4, sequences)
print(list(filtered_result))

# or

def f(x):
    return x > 4

filtered_result = filter(f, sequences)
print(list(filtered_result))


# or

def f(x):
    return x > 4

filtered_result = []
for elm in sequences:
    if f(elm):
        filtered_result.append(elm)

print(filtered_result)