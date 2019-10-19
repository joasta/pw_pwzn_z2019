from lab_3.tasks.task_1 import parse_input
from collections import Counter

def check_frequency(input):
    """
    Perform counting based on input queries and return queries result.

    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje)
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Zbiór danych zrealizuj za pomocą struktury z collections.

    :param input: pairs of int: command, value
    :type input: string
    :return: list of integers with results of operation 3
    :rtype: list
    """
    cnt = Counter()
    input_list = parse_input(input)
    result = []
    for elem in input_list:
        if elem[0] == 1:
            cnt[elem[1]] += 1
        elif elem[0] == 2:
            cnt[elem[1]] -= 1
            cnt += Counter()
        elif elem[0] == 3:
            result.append(cnt[elem[1]])
    return result


_input = """
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2


"""
assert check_frequency(_input) == [0,0]