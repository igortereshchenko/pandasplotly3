# The map function is used to apply a particular operation to every element in a sequence. Like filter(), it also takes 2 parameters:

sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences)

print(type(filtered_result))
print(list(filtered_result))

# or

def f(x):
    return x*x

filtered_result = map(f, sequences)
print(list(filtered_result))


# or

def f(x):
    return x*x

filtered_result = []
for elm in sequences:
    filtered_result.append(f(elm))

print(filtered_result)