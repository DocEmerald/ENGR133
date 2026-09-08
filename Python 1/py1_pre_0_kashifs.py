"""
Course Number: ENGR 13300
Semester: e.g. Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py1 Pre-Task 9
    Team ID:        LC2, Individual
    Author:         Shayaan Kashif, kashifs@purdue.edu
    Date:           9/3/2026

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import math
a = 101
b = 7
c = 12.34

def eq1():
    return (c**2 - math.sin(b)**2)
def eq2():
    return (math.factorial(b)*(math.cos((math.pi)/c)-a))
def eq3():
    return ((c**((math.pi)*(math.e)))*(math.asin(math.sqrt(3)/2))/((a**(math.e))*b))
def main():
    print(f"equation 1: {eq1():.3f}")
    print(f"equation 2: {eq2():.3f}")
    print(f"equation 3: {eq3():.3f}")


if __name__ == "__main__":
    main()
