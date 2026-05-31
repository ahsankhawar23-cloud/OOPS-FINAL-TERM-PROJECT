# ============================================================
# FILE: main.py
# PURPOSE: Demo file — runs all SmartArray features
#
# HOW TO RUN:
#     python main.py
#
# FOLDER STRUCTURE:
#     code/
#       ├── smart_array_base.py      ← Inheritance (base class)
#       ├── encapsulation_mixin.py   ← Encapsulation (summary)
#       ├── abstraction_mixin.py     ← Abstraction (normalize)
#       ├── polymorphism_mixin.py    ← Polymorphism (__str__, is_symmetric)
#       ├── smart_array_full.py      ← Final combined SmartArray
#       └── main.py                  ← This file (demo runner)
# ============================================================

import numpy as np
from smart_array_full import SmartArray


def demo_inheritance():
    """
    DEMO 1 — Inheritance
    Shows that SmartArray automatically has all
    ndarray attributes and methods without rewriting them.
    """
    print("\n" + "=" * 55)
    print("  DEMO 1 — INHERITANCE")
    print("  SmartArray inherits everything from ndarray")
    print("=" * 55)

    a = SmartArray([1, 2, 3, 4, 5, 6])

    # All these come from ndarray — we never wrote them
    print(f"  .shape    : {a.shape}")
    print(f"  .dtype    : {a.dtype}")
    print(f"  .ndim     : {a.ndim}")
    print(f"  .size     : {a.size}")
    print(f"  .reshape  : {a.reshape(2, 3)}")
    print(f"  .flatten  : {a.flatten()}")
    print(f"  class     : {type(a)}")
    print(f"  is ndarray: {isinstance(a, np.ndarray)}")


def demo_encapsulation():
    """
    DEMO 2 — Encapsulation
    summary() bundles multiple attribute accesses
    into one clean method call.
    """
    print("\n" + "=" * 55)
    print("  DEMO 2 — ENCAPSULATION")
    print("  summary() hides multiple details behind one call")
    print("=" * 55)

    a = SmartArray([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])

    print("\n  Without encapsulation you would write:")
    print("      print(a.shape)")
    print("      print(a.dtype)")
    print("      print(a.min())")
    print("      print(a.max())  ... etc\n")
    print("  With encapsulation — just one call:")
    a.summary()


def demo_abstraction():
    """
    DEMO 3 — Abstraction
    normalize() hides the Min-Max formula completely.
    User just calls normalize() without knowing the formula.
    """
    print("\n" + "=" * 55)
    print("  DEMO 3 — ABSTRACTION")
    print("  normalize() hides the Min-Max formula")
    print("=" * 55)

    marks = SmartArray([45, 78, 32, 91, 55, 60])

    print(f"\n  Original marks : {np.asarray(marks)}")
    print(f"  Normalized     : {np.asarray(marks.normalize())}")
    print("\n  Formula hidden inside: (value - min) / (max - min)")
    print("  User never needs to know this!")


def demo_polymorphism():
    """
    DEMO 4 — Polymorphism
    Same print() call, different output for ndarray vs SmartArray.
    __str__ is overridden to show different behavior.
    """
    print("\n" + "=" * 55)
    print("  DEMO 4 — POLYMORPHISM")
    print("  Same print() — different behavior")
    print("=" * 55)

    normal = np.array([1, 2, 3])
    smart  = SmartArray([1, 2, 3])

    print("\n  Normal ndarray print:")
    print(f"  {normal}")

    print("\n  SmartArray print (overridden __str__):")
    print(smart)

    print("\n  --- is_symmetric() ---")
    sym = SmartArray([[1, 2, 3],
                      [2, 5, 6],
                      [3, 6, 9]])

    not_sym = SmartArray([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])

    print(f"\n  Symmetric matrix    → is_symmetric(): {sym.is_symmetric()}")
    print(f"  Non-symmetric matrix → is_symmetric(): {not_sym.is_symmetric()}")


def demo_all_together():
    """
    DEMO 5 — All features together
    A realistic Data Science use case.
    """
    print("\n" + "=" * 55)
    print("  DEMO 5 — REAL DATA SCIENCE USE CASE")
    print("  Student exam marks analysis")
    print("=" * 55)

    # Exam marks of 5 students in 3 subjects
    marks = SmartArray([[55, 72, 68],
                        [88, 91, 85],
                        [40, 45, 38],
                        [76, 80, 72],
                        [60, 55, 65]])

    print("\n  Raw marks:")
    print(marks)

    print("\n  Summary statistics:")
    marks.summary()

    print("\n  Normalized marks (for ML model input):")
    print(marks.normalize())


# ── Run all demos ──
if __name__ == "__main__":
    print("\n" + "*" * 55)
    print("  OOP Final Project — SmartArray Complete Demo")
    print("  BS Data Science — Semester 2")
    print("  Group: Muhammad Ahsan Khawar, Tooba Saeed, Talia Tahir")
    print("*" * 55)

    demo_inheritance()
    demo_encapsulation()
    demo_abstraction()
    demo_polymorphism()
    demo_all_together()

    print("\n" + "*" * 55)
    print("  All Demos Complete!")
    print("*" * 55)
