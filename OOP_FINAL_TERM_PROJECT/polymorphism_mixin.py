# ============================================================
# FILE: polymorphism_mixin.py
# PURPOSE: Adds __str__() override and is_symmetric()
#          to SmartArray
#
# OOP CONCEPT: POLYMORPHISM
#   - __str__() is overridden from ndarray
#   - The same print() function behaves DIFFERENTLY
#     depending on whether you pass it a normal ndarray
#     or a SmartArray
#   - Same method name, different behavior = Polymorphism
# ============================================================

import numpy as np


class PolymorphismMixin:
    """
    Mixin class that adds __str__() override and is_symmetric().

    OOP Concept: POLYMORPHISM
        Polymorphism means the same method behaves
        differently depending on the object it belongs to.

        __str__() is defined in ndarray (parent class).
        We OVERRIDE it in SmartArray (child class) so that
        print() gives different output for SmartArray
        compared to a regular ndarray.

        Same print() call — different output = Polymorphism.

    Usage:
        This class is not used directly.
        It is inherited by SmartArray in smart_array_full.py
    """

    def __str__(self):
        """
        Overrides the default ndarray __str__ method.

        Adds a SmartArray label with shape and dtype info
        before showing the array values.

        OOP Note: This is METHOD OVERRIDING — a key form
        of Polymorphism. The parent ndarray has its own
        __str__. We replace it with our own version.

        Example:
            normal = np.array([1, 2, 3])
            smart  = SmartArray([1, 2, 3])

            print(normal)
            # [1 2 3]                        ← ndarray __str__

            print(smart)
            # SmartArray(shape=(3,), dtype=int64)
            # [1 2 3]                        ← our __str__
        """
        # np.array_str() converts the ndarray part to a clean string
        array_string = np.array_str(np.asarray(self))

        # Add our custom label on top
        return (f"SmartArray(shape={self.shape}, dtype={self.dtype})"
                f"\n{array_string}")

    def is_symmetric(self):
        """
        Checks whether this 2D array is symmetric.

        A matrix is symmetric when it equals its own
        transpose — meaning a[i][j] == a[j][i] for
        every position in the matrix.

        Returns:
            True  — if the array is symmetric
            False — if the array is not symmetric
            False — if the array is not 2D (with error message)

        Example:
            # Symmetric matrix (equals its transpose)
            sym = SmartArray([[1, 2, 3],
                              [2, 5, 6],
                              [3, 6, 9]])
            print(sym.is_symmetric())    # True

            # Not symmetric
            not_sym = SmartArray([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]])
            print(not_sym.is_symmetric()) # False

        OOP Note: This is a new method added through
        Inheritance — SmartArray extends ndarray with
        functionality that ndarray does not have.
        """
        # Guard: only works on 2D arrays (matrices)
        if self.ndim != 2:
            print("Error: is_symmetric() only works on 2D arrays!")
            return False

        # Compare array with its own transpose
        # self.T is the transpose — also inherited from ndarray!
        return np.array_equal(self, self.T)
