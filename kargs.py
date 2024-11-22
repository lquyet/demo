def test(i, *args, **kwargs):
    print(i)
    print(args)
    print(kwargs)


test(1, "adsas", 2, (123, 123), name="linh", age=19)