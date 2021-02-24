# Python program to implement Atbash Cipher Encryption

# This script uses dictionaries to lookup various alphabets
from threading import *
import time

lookup_table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}


def atbash(fileName, outputFileName, key=3, shift_type="right", decrypt=False):
    with open(fileName, "r") as f_in:
        with open(outputFileName, "w") as f_out:
            filename = input("Enter name of file:") + '.txt'
            lineNew = atbash(key, decrypt=decrypt, shift_type=shift_type)
            f_out.write(lineNew)
            filepath = 'I:\\' + filename
            handler = open(filepath)
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


# multithreding process for Atbash Encryption program

def atbash_speed(n):
    cipher = ''
    for x in n:
        cipher += lookup_table[n]
        time.sleep(1)
        print('for speed testing', x % n)


n = [1, 2, 3, 4, 5, 6, 7, 8]
start = time.time()
t1 = Thread(target=atbash_speed, args=(n,))
t1.start()
time.sleep(1)
t1.join()
end = time.time()
print(end - start)

# unittest  for Atbash encrption Program

import unittest
from encrdecrprog import encryption


class TestEncription(unittest.TestCase):
    def setup(self):
        pass

    def test_encryption(self):
        self.assertEquals(encryption('letter'), lookup_table['Hello World'])
        print(self.test_encryption)


if __name__ == '__main__':
    unittest.main()

# Executes the main function
if __name__ == '__main__':
    main()
