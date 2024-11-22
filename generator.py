def normal():
    integers = []
    for i in range(1, 10):
        integers.append(i)
    return integers

print(normal())

def gen_normal():
    for i in range(1,10):
        yield i

print(gen_normal())
print(dir(gen_normal()))
print(next(gen_normal()))

for i in gen_normal():
    print(i)

print((i for i in range(1, 10)))



def m_yield():
    print("yield 1")
    yield 1
    print("yield 2")
    yield 2
    print("yield 3")
    yield 3

y = m_yield()
print(next(y))
print(next(y))

print(dir())

