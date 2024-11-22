def decor(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        res += 1
        return res
    return inner


@decor
def plus(x):
    return x + 1

print(plus(1))

# print(decor(plus)(1))

def decor_with_arg(num):
    def decor2(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            res += num
            return res
        return inner
    return decor2

@decor_with_arg(3)
def plus2(x):
    return x+1

print(plus2(1))

print(decor_with_arg(3)(plus2)(1))