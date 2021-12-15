from cofi.cofi_objective import Model


class BaseSolver:
    """Base class for all inverse solvers in CoFI.
    All inverse solvers must be sub-classes of this class and implements the 'solve()' method.
    
    Could potentially be split into categories based on what they need:
    - value of the objective function
    - value of the objective function and gradient
    - residual vector
    - residual vector and jacobian
    
    """

    def __init__(self):
        pass

    def solve(self) -> Model:
        raise NotImplementedError("inversion 'solve' method not implemented")
