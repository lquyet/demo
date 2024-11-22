class CustomIterator:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num == 10:
            raise StopIteration

        num = self.num
        self.num += 1
        return num

t = CustomIterator()

while True:
    print(t)
    try:
        el = next(t)
        print(el)
    except StopIteration as e:
        print("End of sequence")
        break
    else:
        print("Still in sequence, trying to print the next ...")


print(dir([1,2,3]))
print(dir(iter([1,2,3])))
