# ============================================================
# FILE: smart_array_base.py
# PURPOSE: Defines the base SmartArray class
#          that inherits from numpy.ndarray
#
# OOP CONCEPT: INHERITANCE
#   - SmartArray inherits from numpy.ndarray
#   - All ndarray attributes (.shape, .dtype, .size etc.)
#     and methods (.reshape, .flatten etc.) are available
#     automatically without writing a single line for them
#
# This file is imported by all other files in this project
# ============================================================

import numpy as np


class SmartArray(np.ndarray):
    """
    SmartArray — base class that inherits from numpy.ndarray.

    OOP Concept: INHERITANCE
        SmartArray is a child class of numpy.ndarray.
        It gets everything ndarray has for free, and then
        adds its own extra methods on top.

    Inheritance chain:
        object
          └── numpy.ndarray        (parent)
                └── SmartArray     (our custom child class)
    """

    # ─────────────────────────────────────────────────────
    # WHY __new__ instead of __init__?
    #
    # numpy.ndarray is a special C-level class.
    # It allocates memory at the C level during __new__,
    # not during __init__. So we MUST override __new__
    # to properly create our subclass.
    #
    # This is the official NumPy-documented way to
    # subclass ndarray:
    # https://numpy.org/doc/stable/user/basics.subclassing.html
    # ─────────────────────────────────────────────────────

    def __new__(cls, input_data):
        """
        Creates a new SmartArray instance.

        Parameters:
            input_data : list, tuple, ndarray, or any array-like
                         The data to store in the SmartArray

        Returns:
            A new SmartArray object

        Example:
            a = SmartArray([1, 2, 3])
            b = SmartArray([[1, 2], [3, 4]])
        """
        # Step 1: Convert input to a regular ndarray
        # Step 2: View it as our SmartArray class
        obj = np.asarray(input_data).view(cls)
        return obj

    def __array_finalize__(self, obj):
        """
        Required method by NumPy when subclassing ndarray.

        NumPy calls this automatically every time a new
        SmartArray is created — whether directly, through
        slicing, or through other array operations.

        We leave it empty (pass) because we do not need
        any extra setup. But it MUST be defined.
        """
        pass
