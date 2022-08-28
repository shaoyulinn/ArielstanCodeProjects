"""
File: complement.py
Name: Ariel
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program finds the complement of any given DNA strand.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    print('The complement of '+str(dna)+' is '+build_complement(dna))


def build_complement(dna):
    """
    This function builds the complement of a given DNA strand.
    """
    new_dna = ''
    # This string represents DNA strand in uppercase letters
    ans = ''
    for i in range(len(dna)):
        ch = dna[i]
        if ch.islower():   # Change
            new_dna += ch.upper()
        else:   # Keep
            new_dna += ch

    for i in range(len(new_dna)):
        ch = new_dna[i]
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'G':
            ans += 'C'
        else:
            ans += 'G'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
