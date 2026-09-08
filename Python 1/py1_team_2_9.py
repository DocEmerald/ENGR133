"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Illustrates equivalence of decimal and fraction mathematical operations.

Assignment Information:
    Assignment:     Python 1 Team Task 2
    Team ID:        LC2 - 09
    Author:         Shay Kashif, kashifs@purdue.edu
    Date:           09/08/2026

Contributors:
    Shay Kashif, kashifs@purdue.edu
    Addy Vasquez, vasqu168@purdue.edu
    Shreraj Singh Sanjay Sainani, ssainani@purdue.edu
    Emir Selim Bingol, ebingol@purdue.edu

    My contributor(s) helped me:
    [.] understand the assignment expectations without
        telling me how they will approach it.
    [.] understand different ways to think about a solution
        without helping me plan my solution.
    [.] think through the meaning of a specific error or
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
import random
import fractions

def main():
    random.seed(int(input("Enter the seed: ")))
    rand1 = round(random.uniform(0, 100), 3)
    rand2 = round(random.uniform(10, 50), 3)
    rand3 = round(random.uniform(20, 40), 3)
    rand4 = round(random.uniform(100, 200), 3)
    print("First random number: " + str(rand1))
    print("Second random number: " + str(rand2))
    print("Third random number: " + str(rand3))
    print("Fourth random number: " + str(rand4))
    print("Sum from decimals: " + str(rand1) + " + "  + str(rand2) + " + " + str(rand3) + " + " + str(rand4) + " = " + str(sum([rand1, rand2, rand3, rand4])))
    frac1 = fractions.Fraction(str(rand1))
    frac2 = fractions.Fraction(str(rand2))
    frac3 = fractions.Fraction(str(rand3))
    frac4 = fractions.Fraction(str(rand4))
    print("Sum from fractions: " + str(frac1) + " + "  + str(frac2) + " + " + str(frac3) + " + " + str(frac4) + " = " + str(sum([frac1, frac2, frac3, frac4])))

if __name__ == "__main__":
    main()
