def f_a():
    a=1
    def f_b():
        print a
        return None
    f_b()
    return None

f_a()