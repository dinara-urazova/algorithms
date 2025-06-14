"""
Counting mechanisms are frequently used in computer algorithms
Generally a count must be made of the number of items in a set which possess some particular property / satisfy some
particular conditions.

Problem

Given a set of "n" students' examination marks (in the range 0 to 100) make a count of the number of students that passed the examination. A pass is awarded for all marks of 50 and above.
e.g.
we are given the following set of marks (55, 42, 77, 63, 29, 57, 89)
we can start at the left, examine each mark and see if it is  >= 50 and in this case increment the students_count 

Algorithm
1) read next mark
2) increment the count if the mark passes the requirement of 50 points
"""

students_passed = 0
marks = [55, 42, 77, 63, 29, 57, 89]
for mark in marks:
    if mark >= 50:
        students_passed = students_passed + 1 # students_passed (new value) = students_passed (old value) + 1 as RHS calculted first (right-hand side)
print(f"Number of students who passed the exam is {students_passed}")
