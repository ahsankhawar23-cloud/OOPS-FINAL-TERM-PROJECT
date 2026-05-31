# ============================================================
# FILE: abstraction_mixin.py
# PURPOSE: Adds the normalize() method to SmartArray
#
# OOP CONCEPT: ABSTRACTION
#   - normalize() hides the Min-Max normalization formula
#     from the user completely
#   - The user does not need to know:
#         normalized = (value - min) / (max - min)
#   - They just call:
#         a.normalize()
#   - The HOW is hidden. Only the WHAT is exposed.
#     That is Abstraction.
# ============================================================

import numpy as np


class AbstractionMixin:
    """
    Mixin class that adds the normalize() method.

    OOP Concept: ABSTRACTION
        Abstraction means hiding HOW something works
        internally and only showing WHAT it does.

        normalize() hides the entire Min-Max normalization
        formula, the division-by-zero check, and the
        creation of a new SmartArray — all behind one
        simple method call.

    Usage:
        This class is not used directly.
        It is inherited by SmartArray in smart_array_full.py
    """

    def normalize(self):
        """
        Returns a new SmartArray with all values scaled
        between 0 and 1 using Min-Max normalization.

        Formula used internally (hidden from user):
            normalized_value = (value - min) / (max - min)

        This is very commonly used in Data Science before
        feeding data into Machine Learning models, because
        models perform better when all values are on the
        same scale (0 to 1).

        Returns:
            SmartArray with all values between 0.0 and 1.0

        Example:
            marks = SmartArray([40, 60, 80, 100])
            print(marks.normalize())
            # [0.   0.333  0.667  1.0]

        OOP Note: The user does not know or care about the
        formula inside. They just call normalize() and get
        the scaled result. That is Abstraction.
        """

        # Step 1: Find minimum and maximum values
        min_val = self.min()
        max_val = self.max()

        # Step 2: Guard against division by zero
        # (happens when all values in the array are the same)
        if max_val - min_val == 0:
            # Return array of all zeros — nothing to scale
            return self.__class__(np.zeros_like(self, dtype=float))

        # Step 3: Apply Min-Max normalization formula
        # This entire formula is HIDDEN from the user
        normalized = (self - min_val) / (max_val - min_val)

        # Step 4: Return as a new SmartArray (not plain ndarray)
        return self.__class__(normalized)
