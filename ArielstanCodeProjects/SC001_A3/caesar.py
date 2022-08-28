"""
File: caesar.py
Name: Ariel
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program builds the Caesar Cipher system.
    """
    n = int(input('Secret number: '))
    s = input("What's the ciphered string?")
    new_s = upper(s)
    print('The deciphered string is: '+deciphered_string(n, new_s))


def upper(s):
    """
    This function turns ciphered string into uppercase letters.
    """
    ans = ''
    for i in range(len(s)):
        ch = s[i]
        if ch.islower():   # Change
            ans += ch.upper()
        else:   # Keep
            ans += ch
    return ans


def deciphered_string(n, new_s):
    """
    This function deciphers any given ciphered string.
    """
    new_alphabet = ''
    a = n
    for i in range(n):
        ch = ALPHABET[(len(ALPHABET) - a)]
        new_alphabet += ch
        a -= 1

    a = n
    for i in range(len(ALPHABET) - a):
        ch = ALPHABET[i]
        new_alphabet += ch
        a -= 1

    ans = ''
    for i in range(len(new_s)):
        ch = new_s[i]
        if ch.isalpha():
            for j in range(len(new_alphabet)):
                if ch == new_alphabet[j]:
                    ans += ALPHABET[j]
        else:
            ans += new_s[i]
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
