# distutils: sources = lib/_c_solver_lib.c
# distutils: include_dirs = lib/

cimport _c_solver
from cofi.cofi_solvers import BaseSolver
from cofi.cofi_objective import LeastSquareObjective, Model

from libc.stdlib cimport malloc, free
import numpy as np
from warnings import warn

cdef hello_wrapper():
    hello()

def c_solve(g, y):
    cdef int n = g.shape[0]
    cdef int m = g.shape[1]
    cdef double **g_pt = <double **>malloc(n * sizeof(double *))
    cdef double *y_pt = <double *>malloc(n * sizeof(double))
    cdef double *res_pt = <double *>malloc(m * sizeof(double))
    if not g_pt or not y_pt or not res_pt:
        raise MemoryError
    
    cdef int i
    cdef int j
    for i in range(n):
        g_pt[i] = <double *>malloc(m * sizeof(double))
        for j in range(m):
            g_pt[i][j] = g[i,j]
        y_pt[j] = y[j]

    solve(m, n, g_pt, y_pt, res_pt)

    res = np.zeros(m)
    for i in range(m):
        res[i] = res_pt[i]
    return res


class LRNormalEquationC(BaseSolver):
    def __init__(self, objective: LeastSquareObjective):
        self.objective = objective

    def solve(self) -> Model:
        warn(
            "You are using linear regression formula solver, please note that this is"
            " only for small scale of data"
        )

        G = self.objective.design_matrix()
        Y = self.objective.data_y()

        res = c_solve(G, Y)
        # res = np.linalg.inv(G.T @ G) @ (G.T @ Y)

        model = Model(
            **dict([("p" + str(index[0]), val) for (index, val) in np.ndenumerate(res)])
        )
        return model
