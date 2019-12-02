import numpy as np

def calculate_neighbours(board):
    """
    Returns number of neighbours of board cells.

    Funkcja zwraca tablicę która w polu [R, C] zwraca liczbę sąsiadów którą
    ma komórka board[R, C].
    Obowiązuje sąsiedztwo Moore'a tzn. za sąsiada uznajemy żywą komórkę
    stykającą się bokiem bokach lub na ukos od danej komórki,
    więc maksymalna ilość sąsiadów danej komórki wynosi 8.
    Funkcja ta powinna być zwektoryzowana, tzn. liczba operacji w bytecodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.
    (1 pkt.)

    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczby prawych sąsiadów
    itp.
    Podpowiedź II: Proszę uważać na komówki na bokach i rogach planszy.

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :param periodic
    """
    tmp_board=board*1

    up=np.copy(np.roll(tmp_board, 1,0))
    up[0,:]=0

    down=np.copy(np.roll(tmp_board,-1,0))
    down[board.shape[0]-1,:]=0

    left=np.copy(np.roll(tmp_board,1,1))
    left[:,0]=0

    right=np.copy(np.roll(tmp_board,-1,1))
    right[:,board.shape[1]-1]=0

    upleft=np.copy(np.roll(left,1,0))
    upleft[0,:]=0

    upright=np.copy(np.roll(right,1,0))
    upright[0,:]=0

    downleft=np.copy(np.roll(left,-1,0))
    downleft[board.shape[0]-1,:]=0

    downright=np.copy(np.roll(right,-1,0))
    downright[board.shape[0]-1,:]=0

    neighbours = up+down+left+right
    neighbours += upleft+upright+downleft+downright

    return neighbours

def iterate(board):
    """
    Returns next iteration step of given board.

    Funkcja pobiera planszę game of life i zwraca jej następną iterację.
    Zasady Game of life są takie:
    1. Komórka może być albo żywa (True) albo martwa (False).
    2. Jeśli komórka jest martwa i ma trzech sąsiadów to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadów również umiera.
       W przeciwnym wypadku (dwóch lub trzech sąsiadów) to żyje dalej.
    (1 pkt.)

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :return: next board state
    :rtype: np.ndarray
    """
    neighbours = calculate_neighbours(board)
    tmp_board = board*1

    revive = np.copy(neighbours)
    revive[revive < 3] = 0
    revive[revive > 3] = 0

    kill = np.copy(neighbours)
    kill[kill < 2] = 0
    kill[kill > 3] = 0
    
    tmp_board[board == True] *= kill[board==True]
    tmp_board[board == False] += revive[board==False]

    result = np.array(tmp_board, dtype=bool)
    return result


if __name__ == '__main__':
    _board = np.array([
        [False, False, False,  True, False,  True],
        [ True, False,  True, False, False,  True],
        [ True,  True, False,  True,  True,  True],
        [False,  True,  True, False, False,  True],
        [False, False, False,  True, False, False],
        [False,  True,  True,  True, False,  True]
    ])

    assert (calculate_neighbours(_board) == np.array([
        [1, 2, 2, 1, 3, 1,],
        [2, 4, 3, 4, 6, 3,],
        [3, 5, 5, 3, 4, 3,],
        [3, 3, 4, 4, 5, 2,],
        [2, 4, 6, 3, 4, 2,],
        [1, 1, 3, 2, 3, 0,],
    ])).all()
    assert (iterate(_board) == np.array([
        [False, False, False, False,  True, False],
        [ True, False,  True, False, False,  True],
        [ True, False, False,  True, False,  True],
        [ True,  True, False, False, False,  True],
        [False, False, False,  True, False, False],
        [False, False,  True,  True,  True, False],
    ])).all()
