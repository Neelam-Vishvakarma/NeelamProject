# Python program to implement Atbash Cipher Encryption

# This script uses dictionaries to lookup various alphabets
import os, re

lookup_table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}


def atbash(filename):
    regx = re.compile('[ ;\r\n]+')
    filename = input("Enter name of file:") + '.txt'
    filepath = 'I:\\' + filename
    handler = open(filepath)
    outfile = open("myfile.txt", "w")
    outfile.write('\n'.join(x for x in regx.split(handler.read()) if x))
    cipher = ''
    for letter in filename:
        # this checks for space
        if (letter != ' '):
            # adds the corresponding letter from the lookup_table
            cipher += lookup_table[letter]
        else:
            # this  adds space
            cipher += ' '

    return filename


# Driver function to run the program
def main():
    # encrypt the given message
    message = 'HELLO WORLD'
    print(atbash(message.upper()))


# Executes the main function
if __name__ == '__main__':
    main()
