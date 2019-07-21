import unittest
import morse_converter

ALPHABET = "abcdefghijklmnopqrstuvwxyz.,?/@1234567890"
MORSE_CODES = (           # Form a string of all morse codes separated by .
    "*-"      +  "."      # A
    "-***"    +  "."      # B
    "-*-*"    +  "."      # C
    "-**"     +  "."      # D
    "*"       +  "."      # E
    "**-*"    +  "."      # F
    "--*"     +  "."      # G
    "****"    +  "."      # H
    "**"      +  "."      # I
    "*---"    +  "."      # J
    "-*-"     +  "."      # K 
    "*-**"    +  "."      # L
    "--"      +  "."      # M
    "-*"      +  "."      # N
    "---"     +  "."      # O
    "*--*"    +  "."      # P
    "--*-"    +  "."      # Q
    "*-*"     +  "."      # R
    "***"     +  "."      # S
    "-"       +  "."      # T
    "**-"     +  "."      # U
    "***-"    +  "."      # V
    "*--"     +  "."      # W
    "-**-"    +  "."      # X 
    "-*--"    +  "."      # Y 
    "--**"    +  "."      # Z 
    "*-*-*-"  +  "."      # . 
    "--**--"  +  "."      # , 
    "**--**"  +  "."      # ?
    "-**-*"   +  "."      # /
    "*--*-*"  +  "."      # @
    "*----"   +  "."      # 1
    "**----"  +  "."      # 2
    "***--"   +  "."      # 3
    "****-"   +  "."      # 4
    "*****"   +  "."      # 5
    "-****"   +  "."      # 6
    "--***"   +  "."      # 7
    "---**"   +  "."      # 8
    "----*"   +  "."      # 9
    "-----"   +  ".")     # 0
  

class TestEnglishToMorseCode(unittest.TestCase):

    def test_upper(self):
        # Test that the string of all characters get converted correctly
        self.assertEqual(morse_converter.convert_english(ALPHABET), MORSE_CODES)

class TestMorseCodeToEnglish(unittest.TestCase):

    def test_upper(self):
        # Test that all morse codes get converted correctly
        self.assertEqual(morse_converter.convert_morse(MORSE_CODES), ALPHABET.upper())


if __name__ == '__main__':
    unittest.main()