import numpy as np

def least_sq(xy):
    """
    Fits linear function to given vector of 2D points.

    Funkcja liczy parametry funkcji liniowej ax+b do danych za pomocą metody
    najmniejszych kwadratów.
    (1 pkt.)

    A = (N*Sum(xy)-Sum(x)*Sum(y))/Delta
    B = (Sum(x^2)*Sum(y)-Sum(x)*Sum(xy))/Delta
    Delta = N*Sum(x^2) - (Sum(x)^2)

    :param xy: vector of 2D points (shape (2, n))
    :type xy: np.ndarray
    :return: Tuple of fitted parameters
    """
    iks=xy[0,:]
    igrek=xy[1,:]

    x2 = iks*iks
    xdoty = iks*igrek
    sumx = np.sum(iks)
    sumy = np.sum(igrek)
    sumxy = np.sum(xdoty)
    sumx2 = np.sum(x2)
    N = iks.size

    Delta = N*sumx2 - sumx*sumx
    A = (N*sumxy-sumx*sumy)/Delta
    B = (sumx2*sumy - sumx*sumxy)/Delta

    return (A, B)
