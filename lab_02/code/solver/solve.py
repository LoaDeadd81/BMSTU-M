import numpy as np
import scipy as sp


def get_kolmogorov_eq(mtr):
    st_num = mtr.shape[0]

    r = np.zeros([st_num] * 2)

    for state in range(st_num):
        r[state][state] = -sum(mtr[state, :])
        r[state] += mtr[:, state]

    return r


def get_norm_eq(st_num):
    return 1, np.zeros(st_num) + 1


def solve(mtr):
    matrix = np.array(mtr)

    l = np.zeros(len(mtr))
    r = get_kolmogorov_eq(matrix)

    l[-1], r[-1] = get_norm_eq(len(mtr))

    return sp.linalg.solve(r, l)
