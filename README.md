# OOP Analysis of NumPy
### Object-Oriented Programming — Final Term Project
**BS Data Science — Semester 2 | Spring 2026**

---

## Group Members

- Muhammad Ahsan Khawar — 02091
- Tooba Saeed — 02054
- Talia Tahir — 02079

  ---

 ## Video Presentation Link

 https://youtu.be/FFwPG-38JrM
 
---

## Library Chosen

**NumPy (Numerical Python)**

We chose NumPy for this project. It is the most widely used library for numerical computing in Python and almost every Data Science library like Pandas and Scikit-learn depends on it. More importantly, it is built using very clean OOP design so it was a good choice for this course.

---

## What We Did

We studied how NumPy uses OOP principles in its actual source code and then built our own custom class called **SmartArray** that extends `numpy.ndarray`.

Things we covered in the analysis:
- How `ndarray` uses **Encapsulation** by hiding raw memory details behind clean attributes
- How `matrix`, `memmap`, and `MaskedArray` use **Inheritance** by extending `ndarray`
- How operator overloading and `.dot()` show **Polymorphism**
- How methods like `.reshape()` and `.flatten()` show **Abstraction**

---

## Files in This Project

```
OOP-NumPy-Project/
│
├── report/
│   └── OOP_Final_Project_Report.pdf
│
├── code/
│   ├── smart_array_base.py        -- base class, sets up inheritance from ndarray
│   ├── encapsulation_mixin.py     -- adds summary() method
│   ├── abstraction_mixin.py       -- adds normalize() method
│   ├── polymorphism_mixin.py      -- adds __str__() and is_symmetric()
│   ├── smart_array_full.py        -- final combined SmartArray class
│   └── main.py                    -- run this to see all the demos
│
└── diagrams/
    └── class_hierarchy_diagram.jpg
```

---

## How to Run

First make sure NumPy is installed:

```bash
pip install numpy
```

Then go into the code folder and run main.py:

```bash
cd code
python main.py
```

You should see output for all five demos one after another. The whole thing runs in under two seconds.

---

## SmartArray — Our Custom Class

`SmartArray` is a subclass of `numpy.ndarray`. We added a few methods on top of what ndarray already provides:

- `summary()` — prints shape, dtype, size, min, max, and mean in one go *(Encapsulation)*
- `normalize()` — scales all values to be between 0 and 1 using Min-Max formula *(Abstraction)*
- `is_symmetric()` — checks if a 2D array is equal to its own transpose *(Inheritance)*
- `__str__()` — overrides the default print output to show a SmartArray label *(Polymorphism)*

Quick example:

```python
from smart_array_full import SmartArray

marks = SmartArray([45, 78, 32, 91, 55, 60])

marks.summary()           # encapsulation
print(marks.normalize())  # abstraction

matrix = SmartArray([[1, 2, 3],
                     [2, 5, 6],
                     [3, 6, 9]])
print(matrix.is_symmetric())  # True
```

---

## NumPy Class Hierarchy

```
numpy.ndarray
    ├── matrix        -- overrides * for matrix multiplication
    ├── memmap        -- for large files that don't fit in RAM
    ├── MaskedArray   -- handles missing/invalid values
    └── SmartArray    -- our custom class (this project)

Related:
    ├── dtype         -- describes element data type
    ├── ufunc         -- vectorised math functions
    └── nditer        -- iterator for multi-dimensional arrays
```

---

## References

- https://numpy.org/doc/stable/
- https://numpy.org/doc/stable/user/basics.subclassing.html
- https://github.com/numpy/numpy
- https://realpython.com/python3-object-oriented-programming/

---

**Course:** Object-Oriented Programming
**Submission Date:** 30 May 2026
**Total Marks:** 100
