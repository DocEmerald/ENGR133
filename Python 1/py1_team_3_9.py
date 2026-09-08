"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Determines relationship between characters in two words or phrases.

Assignment Information:
    Assignment:     Python 1 Team Task 3
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




def main():
    firstinput = input("Enter the first string: ")
    secondinput = input("Enter the second string: ")
    first = (firstinput.lower()).replace(" ", "")
    second = (secondinput.lower()).replace(" ", "")
    print("Characters in first string:")
    print(sorted(list(set(list(first)))))
    print("Characters in second string:")
    print(sorted(list(set(list(second)))))
    print("Characters in both strings:")
    print(sorted(list(set(list(first)) & set(list(second)))))
    print("Characters in the first string but not the second:")
    print(sorted(list(set(list(first)) - set(list(second)))))
    print("Characters in the second string but not the first:")
    print(sorted(list(set(list(second)) - set(list(first)))))


if __name__ == "__main__":
    main()
