# ============================================================
# OOP Final Project — BS Data Science Semester 2
# Library: NumPy
# Custom Extension: SmartArray
# Description: A subclass of numpy.ndarray that adds
#              useful Data Science helper methods
# ============================================================

import numpy as np


class SmartArray(np.ndarray):
    """
    SmartArray is a custom subclass of numpy.ndarray.

    It inherits all features of ndarray and adds:
        - summary()      : prints key statistics in one go
        - normalize()    : scales values between 0 and 1
        - is_symmetric() : checks if a 2D array is symmetric
        - __str__()      : overrides print to show cleaner output

    OOP Concepts Demonstrated:
        - Inheritance   : SmartArray inherits from ndarray
        - Polymorphism  : __str__ behaves differently than ndarray
        - Encapsulation : internal numpy details are hidden
        - Abstraction   : complex math hidden behind simple methods
    """

    # ─────────────────────────────────────────────
    # __new__ is used instead of __init__ because
    # ndarray is a special C-level class in NumPy.
    # This is the correct NumPy-documented way to
    # subclass ndarray.
    # ─────────────────────────────────────────────
    def __new__(cls, input_data):
        """
        Creates a new SmartArray from any array-like input.
        (list, tuple, another ndarray, etc.)
        """
        # Convert input to ndarray first, then view as SmartArray
        obj = np.asarray(input_data).view(cls)
        return obj

    def __array_finalize__(self, obj):
        """
        Required by NumPy when subclassing ndarray.
        Called every time a new SmartArray is created.
        """
        pass

    # ─────────────────────────────────────────────
    # METHOD 1: summary()
    # Shows all important info about the array
    # OOP Concept: Inheritance (new method added)
    # ─────────────────────────────────────────────
    def summary(self):
        """
        Prints a complete summary of the array including:
        shape, dimensions, size, data type, min, max, and mean.

        Example:
            a = SmartArray([[1, 2, 3], [4, 5, 6]])
            a.summary()
        """
        print("=" * 40)
        print("        SmartArray Summary")
        print("=" * 40)
        print(f"  Shape      : {self.shape}")
        print(f"  Dimensions : {self.ndim}")
        print(f"  Size       : {self.size}")
        print(f"  Data Type  : {self.dtype}")
        print(f"  Min Value  : {self.min()}")
        print(f"  Max Value  : {self.max()}")
        print(f"  Mean Value : {self.mean():.2f}")
        print("=" * 40)

    # ─────────────────────────────────────────────
    # METHOD 2: normalize()
    # Scales all values between 0 and 1
    # OOP Concept: Abstraction (complex math hidden)
    # ─────────────────────────────────────────────
    def normalize(self):
        """
        Returns a new SmartArray with all values scaled
        between 0 and 1 using Min-Max normalization.

        Formula: (value - min) / (max - min)

        Useful in Data Science before feeding data
        into machine learning models.

        Example:
            a = SmartArray([10, 20, 30, 40, 50])
            print(a.normalize())
            # [0.   0.25  0.5  0.75  1.0]
        """
        min_val = self.min()
        max_val = self.max()

        # Avoid division by zero if all values are the same
        if max_val - min_val == 0:
            return SmartArray(np.zeros_like(self, dtype=float))

        # Apply min-max normalization formula
        normalized = (self - min_val) / (max_val - min_val)
        return SmartArray(normalized)

    # ─────────────────────────────────────────────
    # METHOD 3: is_symmetric()
    # Checks if a 2D array equals its transpose
    # OOP Concept: Inheritance (new method added)
    # ─────────────────────────────────────────────
    def is_symmetric(self):
        """
        Checks if the 2D array is symmetric.
        A matrix is symmetric if it equals its own transpose.
        (i.e. a[i][j] == a[j][i] for all positions)

        Returns:
            True if symmetric, False otherwise.
            Error message if array is not 2D.

        Example:
            a = SmartArray([[1, 2, 3],
                            [2, 5, 6],
                            [3, 6, 9]])
            print(a.is_symmetric())   # True
        """
        # Only works for 2D arrays
        if self.ndim != 2:
            print("Error: is_symmetric() only works on 2D arrays!")
            return False

        # A matrix is symmetric if it equals its transpose
        return np.array_equal(self, self.T)

    # ─────────────────────────────────────────────
    # METHOD 4: __str__() override
    # Changes how the array looks when printed
    # OOP Concept: Polymorphism (overriding parent method)
    # ─────────────────────────────────────────────
    def __str__(self):
        """
        Overrides the default ndarray print behavior.
        Adds a label showing it is a SmartArray and
        includes shape and dtype information.

        OOP Note: This is polymorphism — the same print()
        function behaves differently for SmartArray vs ndarray.
        """
        return (f"SmartArray(shape={self.shape}, dtype={self.dtype})"
                f"\n{np.array_str(np.asarray(self))}")


# ============================================================
#  DEMO — showing SmartArray in action
#  Run this file directly to see the demo
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 50)
    print("   OOP Final Project — SmartArray Demo")
    print("=" * 50)

    # ── Demo 1: Creating a SmartArray ──
    print("\n--- Demo 1: Creating a SmartArray ---")
    a = SmartArray([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])
    print(a)

    # ── Demo 2: summary() method ──
    print("\n--- Demo 2: summary() method ---")
    a.summary()

    # ── Demo 3: normalize() method ──
    print("\n--- Demo 3: normalize() method ---")
    marks = SmartArray([45, 78, 32, 91, 55, 60])
    print("Original marks :", marks)
    print("Normalized marks:", marks.normalize())

    # ── Demo 4: is_symmetric() method ──
    print("\n--- Demo 4: is_symmetric() method ---")

    symmetric = SmartArray([[1, 2, 3],
                            [2, 5, 6],
                            [3, 6, 9]])

    not_symmetric = SmartArray([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]])

    print("Symmetric matrix:")
    print(symmetric)
    print("Is symmetric?", symmetric.is_symmetric())

    print("\nNon-symmetric matrix:")
    print(not_symmetric)
    print("Is symmetric?", not_symmetric.is_symmetric())

    # ── Demo 5: Inherited ndarray methods still work ──
    print("\n--- Demo 5: Inherited ndarray methods still work ---")
    b = SmartArray([1, 2, 3, 4, 5, 6])
    print("Original      :", b)
    print("Reshaped (2,3):", b.reshape(2, 3))
    print("Flattened     :", b.flatten())
    print("dtype         :", b.dtype)
    print("shape         :", b.shape)
    print("size          :", b.size)

    # ── Demo 6: Polymorphism — __str__ override ──
    print("\n--- Demo 6: Polymorphism — print behavior ---")
    normal = np.array([1, 2, 3])
    smart  = SmartArray([1, 2, 3])
    print("Normal ndarray print:")
    print(normal)
    print("\nSmartArray print (overridden __str__):")
    print(smart)

    print("\n" + "=" * 50)
    print("   Demo Complete!")
    print("=" * 50)
