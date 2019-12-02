import numpy as np

def estimate_pi(n):
    """
    Returns estimated value of pi.

    Funkcja szacuje wartość pi metodą probabilistyczną.
    Wygenerujmy n punktów z obszaru [-1,1]^2. Niech k określa liczbę punktów
    odległych od punku (0,0) o nie więcej niż 1. Proporcja 4k/n
    powinna szacować wartość pi.
    (1pkt).

    :param n: Number of points to made estimation.
    :type xy: int
    :return: Estimated Pi value
    :rtype: float
    """
    points = np.random.uniform(-1,1,(n,2))
    distance = (points[:,0]*points[:,0]+points[:,1]*points[:,1])
    distance = distance**(0.5)

    distance[distance==0] = 0.5
    distance[distance >1] = 0
    distance[distance >0] = 1
    pi_est = 4*np.sum(distance)/n

    return pi_est


if __name__ == '__main__':
    np.testing.assert_approx_equal(estimate_pi(int(1e2)), np.pi, 1)
    np.testing.assert_approx_equal(estimate_pi(int(1e3)), np.pi, 2)
