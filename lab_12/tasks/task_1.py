def generate_fibonacci(n=100):
    zwrotka = []
    num=0
    if not isinstance(n, int) or n<1 or n>100:
        raise RuntimeError
    while num < n:
        if num <= 1:
            zwrotka.append(num)
            yield num
        else:
            zwrotka.append(zwrotka[num-1] + zwrotka[num-2])
            yield zwrotka[num]
        num += 1



if __name__ == '__main__':
    assert list(generate_fibonacci(1)) == [0]
    assert list(generate_fibonacci(2)) == [0, 1]
    assert sum(generate_fibonacci(10)) == 88
    ii = 0
    for ii in generate_fibonacci():
        pass
    assert ii == 218922995834555169026
    try:
        generate_fibonacci(0)
    except Exception as exc:
        assert isinstance(exc, RuntimeError)
