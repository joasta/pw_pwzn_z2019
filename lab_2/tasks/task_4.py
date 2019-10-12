def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    mess=sorted(set(msg))
    krotka=(0,0)
    for elem in mess:
        a=0
        for letter in msg:
            if letter == elem:
                a+=1
        if a > krotka[1]:
            krotka=(elem,a)
    return krotka


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)