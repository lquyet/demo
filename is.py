x = 4
y = x

print(y is x) # true

x += 1

print(y is x) # false

x = [1,2,3]
y = x
print(y is x) # true
x[1] = 5
print(y is x) # true
print(y) # same as x