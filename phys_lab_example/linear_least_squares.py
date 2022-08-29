import numpy as np


def lin_ls(x, y, through_null=False):
    """
    Eng:
        Returns coefficients b, k and their standard errors s_k, s_b
    from linear approximation (using least squares) y = k * x + b to
    given points (x, y).
        If the flag through_null is True, then approximation does not include
    coefficient b (as well as s_b), b is considered to be zero.
    Rus:
        Возвращает коэффициенты b, k и их погрешности s_b, s_k при
    линейной аппроксимации y = k * x + b методом МНК по введённым точкам (х, у).
        Если флаг through_null равен True, то аппроксимация проводится через
    точку (0,0) и b, s_b не включены в вывод функции.

    Parameters
    ----------
    x : numpy.ndarray
        Numpy array with x coordinates of points.

    y : numpy.ndarray
        Numpy array with y coordinates of points. Vectors x and y must be the same length.

    through_null: bool, optional
        Flag for making approximation through (0, 0) point.

    Returns
    -------
    out : tuple
        If through_null is True: (k, s_k),
        If through_null is False: (k, s_k, b, s_b)
    """
    if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        if len(x) != len(y):
            raise ValueError("Incompatible x and y vectors. They must have the same length.")
        if through_null:
            k = np.mean(x * y) / np.mean(x * x)
            s_k = np.sqrt(1 / len(x)) * np.sqrt(np.mean(y * y) / np.mean(x * x) - k ** 2)
            return k, s_k
        else:
            xy = np.mean(x * y)
            x1y = np.mean(x) * np.mean(y)
            x2 = np.mean(x * x)
            x12 = np.mean(x) ** 2
            y2 = np.mean(y * y)
            y12 = np.mean(y) ** 2
            k = (xy - x1y) / (x2 - x12)
            b = np.mean(y) - k * np.mean(x)
            s_k = np.sqrt(1 / len(x)) * np.sqrt((y2 - y12) / (x2 - x12) - k ** 2)
            s_b = s_k * np.sqrt(x2 - x12)
            return k, s_k, b, s_b
    else:
        raise ValueError("Invalid x or/and y type. Must be numpy.ndarray.")
