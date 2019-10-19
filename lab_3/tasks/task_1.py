def parse_input(input):
    """
    Splits multiline string into list of lists with integers.

    Napisz funkcję przymującą wielolinijkowy ciąg znaków.
    a zwracającą listę list liczb całkowitych znajdujących się w podanym ciągu znaków.
    Nie używaj pętl for i while.
    String może zawierać puste linie na początku i końcu.

    :param input: string to parse
    :type input: str
    :return: list of parsed list of integers
    :rtype: list
    """
    lines_list = input.strip().splitlines()
    lines_list = list(map(lambda x: list(map(lambda y: int(y), x.split())), lines_list))
    return lines_list


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

assert parse_input(_input) == [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
