
from itertools import repeat, starmap
from typing import List
from collections.abc import Callable


def repeat_function(function: Callable[[], str], times: int | None = None, *args: List[str]) -> List[str]:
    """

        repeatedly calls a function that returns a string a specified number of times and returns the result in a list
        based on example provided in itertools documentation: https://docs.python.org/3/library/itertools.html#itertools-recipes

        Parameters
        ----------
        function: Callable[[], str]
            the function to call
        times: int
            the number of times to call the function
        *args: List[str]
            the parameters to be passed to the function

        Returns
        -------
        List[str]
            the collected results of calling the function multiple times

    """
    return list(starmap(function, repeat(args, times)) if times else starmap(function, repeat(args)))
