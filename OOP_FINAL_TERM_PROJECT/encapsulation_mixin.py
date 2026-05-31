# ============================================================
# FILE: encapsulation_mixin.py
# PURPOSE: Adds the summary() method to SmartArray
#
# OOP CONCEPT: ENCAPSULATION
#   - The summary() method hides the internal complexity
#     of accessing multiple ndarray attributes
#   - Instead of the user writing:
#         print(a.shape)
#         print(a.dtype)
#         print(a.min())
#         print(a.max())
#         ... etc
#   - They just call:
#         a.summary()
#   - The messy details are ENCLOSED inside one method
#     That is Encapsulation — bundling data and methods
#     together and hiding the internal details
# ============================================================


class EncapsulationMixin:
    """
    Mixin class that adds the summary() method.

    OOP Concept: ENCAPSULATION
        A mixin is a class that provides methods to be
        inherited by another class without being a full
        parent class on its own.

        summary() demonstrates encapsulation by bundling
        multiple attribute accesses into one clean method.
        The user does not need to know what is happening
        inside — they just call summary() and get all info.

    Usage:
        This class is not used directly.
        It is inherited by SmartArray in smart_array_full.py
    """

    def summary(self):
        """
        Prints a complete summary of the array.

        Shows: shape, dimensions, size, data type,
               minimum value, maximum value, mean value.

        OOP Note: This is Encapsulation — multiple internal
        details are bundled behind one clean method call.

        Example:
            a = SmartArray([[10, 20, 30],
                            [40, 50, 60]])
            a.summary()

        Output:
            ========================================
                    SmartArray Summary
            ========================================
              Shape      : (2, 3)
              Dimensions : 2
              Size       : 6
              Data Type  : int64
              Min Value  : 10
              Max Value  : 60
              Mean Value : 35.00
            ========================================
        """
        print("=" * 40)
        print("        SmartArray Summary")
        print("=" * 40)
        print(f"  Shape      : {self.shape}")     # from ndarray (inherited)
        print(f"  Dimensions : {self.ndim}")      # from ndarray (inherited)
        print(f"  Size       : {self.size}")      # from ndarray (inherited)
        print(f"  Data Type  : {self.dtype}")     # from ndarray (inherited)
        print(f"  Min Value  : {self.min()}")     # from ndarray (inherited)
        print(f"  Max Value  : {self.max()}")     # from ndarray (inherited)
        print(f"  Mean Value : {self.mean():.2f}")# from ndarray (inherited)
        print("=" * 40)
