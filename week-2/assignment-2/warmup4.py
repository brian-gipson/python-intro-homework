# 1. What the error message said (paste it)
#    Traceback (most recent call last):
#      File "d:\Code the Dream\Code\python-intro-homework\week-2\assignment-2\warmup4.py", line 5, in <module>
#        age = this_year - year_born
#          ~~~~~~~~~~^~~~~~~~~~~
#    TypeError: unsupported operand type(s) for -: 'int' and 'str'
#
# 2. What caused it
#    input() returns a string, so year_born is a string. You cannot subtract a string from an integer.
#
# 3. How you fixed it
#    I converted year_born to an integer using int() before performing the subtraction.

from datetime import date

year_born = int(input("What year were you born? "))
this_year = date.today().year
age = this_year - year_born

print(f"You are about {age} years old.")

