# ============================================================
# FILE: smart_array_full.py
# PURPOSE: Combines all mixin classes into one final
#          SmartArray class
#
# OOP CONCEPT: MULTIPLE INHERITANCE
#   SmartArray inherits from:
#       1. numpy.ndarray      — the core array class
#       2. EncapsulationMixin — adds summary()
#       3. AbstractionMixin   — adds normalize()
#       4. PolymorphismMixin  — adds __str__() and is_symmetric()
#
# This file is the main class file.
# Import SmartArray from here in your code.
# ============================================================

from smart_array_base    import SmartArray as _Base
from encapsulation_mixin import EncapsulationMixin
from abstraction_mixin   import AbstractionMixin
from polymorphism_mixin  import PolymorphismMixin


class SmartArray(_Base, EncapsulationMixin, AbstractionMixin, PolymorphismMixin):
    """
    SmartArray — final combined class.

    Inherits from:
        numpy.ndarray      → all array attributes and methods
        EncapsulationMixin → summary()
        AbstractionMixin   → normalize()
        PolymorphismMixin  → __str__(), is_symmetric()

    OOP Concepts demonstrated:
        ┌─────────────────┬───────────────────────────────────┐
        │ OOP Concept     │ Where                             │
        ├─────────────────┼───────────────────────────────────┤
        │ Inheritance     │ Inherits from ndarray + 3 mixins  │
        │ Encapsulation   │ summary() bundles details inside  │
        │ Abstraction     │ normalize() hides the formula     │
        │ Polymorphism    │ __str__() overrides ndarray print │
        └─────────────────┴───────────────────────────────────┘

    Example:
        from smart_array_full import SmartArray

        a = SmartArray([[1, 2, 3], [4, 5, 6]])
        a.summary()
        print(a.normalize())
        print(a.is_symmetric())
    """
    pass    # All methods come from the parent classes above
