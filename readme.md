Morse Code Converter
====================

This is a simple command line tool for converting English characters to Morse code and vice versa. When converting from English to Morse code, the tool will add a dot (.) after each character in order to separate where each Morse code starts. When converting from Morse code to English, each Morse code must be ended by a dot (.).

How to use
----------

The text or Morse code to be converted is read from an input file set with the -i flag (defaults to input.txt).
The converted text will be written to the file set with flag -o (defaults to output.txt).

By default the tool will assume to convert from English to Morse code. In order to convert Morse code to English, set the -M flag.

### Examples
Converting from English to Morse code.
```python
python morse_converter.py -i "english_input.txt" -o "morse_output.txt"
```

Converting from Morse code to English.
```python
python morse_converter.py -M -i "morse_input.txt" -o "english_output.txt"
```