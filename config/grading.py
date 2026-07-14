"""
grading.py

Grading Configuration
"""

# ======================================================
# Maximum Marks of Each Assessment
# ======================================================

QUIZ_MAXIMUMS = {

    "Day1 Module1": 15,

    "Day2 Module1": 15,

    "Day3 Module1": 25,

    "Day4 Module1": 60,

    "Day5 Module5": 16,

    "Day6 Module2": 10,

    "Day7 Module3": 20

   
   

    


}

# Automatically calculate total maximum marks

TOTAL_MAX_MARKS = sum(QUIZ_MAXIMUMS.values())

# ======================================================
# Grade Boundaries
# ======================================================

GRADE_BOUNDARIES = {

    "A+": 90,

    "A": 80,

    "B": 70,

    "C": 60,

    "D": 50,

    "F": 0

}
# ==========================================================
# Grade Display Order
# ==========================================================

GRADE_ORDER = [

    "A+",
    "A",
    "B",
    "C",
    "D",
    "F"

]

# ==========================================================
# Grade Remarks
# ==========================================================

GRADE_REMARKS = {

    "A+": "Outstanding Performance",
    "A": "Excellent Performance",
    "B": "Very Good",
    "C": "Good",
    "D": "Needs Improvement",
    "F": "Failed"

}

# ==========================================================
# Grade Colors
# ==========================================================

GRADE_COLORS = {

    "A+": "green",
    "A": "darkgreen",
    "B": "blue",
    "C": "orange",
    "D": "red",
    "F": "red"

}

