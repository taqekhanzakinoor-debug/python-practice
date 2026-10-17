# Python to AI Bootcamp: Practice Repository

Hands-on practice for **Day 1 and Day 2** of the Python to AI Bootcamp, organized by Google Developer Groups (GDG) CUI Wah.

## Repository Structure

```
python-practice/
├── DAY-1/
│   ├── strings_practice.py
│   ├── basics_practice.py
│   ├── data_structures_practice.py
│   ├── functions_practice.py
│   ├── LIST.py
│   └── student_marks_analyzer.py
├── DAY-2/
│   ├── Data-analysis.ipynb
│   └── titanic.csv
└── README.md
```

## Day 1: Python Fundamentals

| File | Topics Covered |
|---|---|
| `basics_practice.py` | Variables, data types, type conversion with `input()`, operators (arithmetic, comparison, logical, membership, identity), `if / elif / else`, `for` and `while` loops, `break`, `continue` |
| `strings_practice.py` | Indexing, slicing, `upper()`, `lower()`, `title()`, `strip()`, `replace()`, `split()`, `join()`, f-strings |
| `LIST.py` | List indexing, slicing, `append`, `insert`, `extend`, `remove`, `pop`, `sort`, `sorted`, list comprehension |
| `data_structures_practice.py` | Lists, tuples, sets, and dictionaries |
| `functions_practice.py` | Functions with `def` and `return`, default parameters, keyword arguments |
| `student_marks_analyzer.py` | Mini-project: Student Marks Analyzer extended with `max()` and `min()` to show the highest and lowest marks |

### Student Marks Analyzer

The analyzer calculates the total and average of a list of marks, prints a result category, and shows the highest and lowest marks.

```python
student_marks = [40, 80, 90, 100, 50]
analyze(student_marks)
```

**Sample output:**

```
Normal
40
80
90
100
50
Total: 360
Average: 72.0
Highest: 100
Lowest: 40
```

Changes made to the original version:

- Added `max()` and `min()` to display the highest and lowest marks
- Fixed the loop (`range(0,4)` skipped the last mark) by looping over the list directly
- Added a check for an empty list, so the program doesn't crash

## Day 2: NumPy, Pandas and Titanic Dataset

`DAY-2/Data-analysis.ipynb` covers:

- **NumPy:** `np.array`, `sum`, `mean`, `max`, element-wise operations
- **Pandas:** `read_csv`, `head`, `tail`, `shape`, `columns`, `info`, `describe`, `isnull().sum()`, `value_counts`, `loc`, `iloc`
- **Custom Titanic questions** (below)

### Custom Questions and Findings

**Q1: How many male passengers over 40 in 2nd class survived?**

```python
q1 = df.loc[
    (df["Sex"] == "male") &
    (df["Age"] > 40) &
    (df["Pclass"] == 2) &
    (df["Survived"] == 1)
]
print(len(q1))
```

**Answer:** 2 survivors out of 21 male passengers over 40 in 2nd class. Older men in 2nd class had a low survival rate.

**Q2: What was the average fare paid by survivors who embarked from Southampton (S)?**

```python
q2 = df.loc[
    (df["Survived"] == 1) & (df["Embarked"] == "S"),
    "Fare"
]
print(round(q2.mean(), 2))
```

**Answer:** 39.55 average fare across 217 passengers, which is higher than the overall median fare of 14.45.

**Note:** 177 passengers have a missing `Age`, so they are left out of the age filter in Q1.

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/taqekhanzakinoor-debug/python-practice.git
cd python-practice
```

**2. Install the requirements**

```bash
pip install numpy pandas jupyter
```

**3. Run a Day 1 file**

```bash
python DAY-1/strings_practice.py
python DAY-1/student_marks_analyzer.py
```

**4. Open the Day 2 notebook**

Open `DAY-2/Data-analysis.ipynb` in VS Code or Jupyter, then click **Run All**. Keep `titanic.csv` in the same folder as the notebook.

## Tools Used

- Python 3
- NumPy
- Pandas
- Jupyter Notebook
- VS Code
- Git and GitHub

## Author

**Alauddin**
GitHub: [taqekhanzakinoor-debug](https://github.com/taqekhanzakinoor-debug)

Python to AI Bootcamp, Google Developer Groups (GDG) CUI Wah.
