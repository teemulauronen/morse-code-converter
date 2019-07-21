
import sys
import os
import json
import argparse
import logging

logger = logging.getLogger(__name__)

# Read Morse table into a global variable.
with open("morse_table.json", 'r') as f:
    MORSE_TABLE = json.load(f)
# Invert the Morse table for converting Morse code to English.
INVERTED_MORSE_TABLE = {v: k for k, v in MORSE_TABLE.items()}


def convert_english(line):
    """Convert a line of english characters to Morse code.
    
    Each character will be separated with a dot. White space characters are retained. 
    Invalid characters will trigger a warning and are removed from the result.
    """
    result = ""
    for ch in line:
        if ch.isspace():
            result += ch
        else:
            morse_code = MORSE_TABLE.get(ch.upper())
            if morse_code:
                result += morse_code + '.'
            else:
                logger.warning("Character %s can not be converted to Morse code!", ch)
    return result


def morse_code_to_char(morse_code):
    """Convert Morse code to character to corresponding English character.

    If matching character is not found, will return an empty string.
    """
    character = INVERTED_MORSE_TABLE.get(morse_code)
    if character:
        return character
    else:
        # Invalid Morse code is converted to _
        logger.warning("%s is not a valid morse code!", morse_code)
        return "_"


def convert_morse(line):
    """Convert a string of Morse code to English.

    Morse code must be encoded with * as the short and - as the long. 
    Each Morse code character should be separated with a dot. White space characters are retained.
    Invalid Morse codes will trigger a warning and are converted to _.
    Invalid characters will trigger a warning and the current morse code being decoded will be invalidated
    and is converted to _.
    """
    # Read line a character at a time. Characters are read into morse_buffer until a dot (.) is detected.
    # When a . is detected, convert the morse_buffer to a character and append it to the result.
    # Then reset morse_buffer to "".
    result = ""
    morse_buffer = ""
    for ch in line:
        if ch == '.':
            if morse_buffer:
                result += morse_code_to_char(morse_buffer)
                morse_buffer = ""
        elif ch.isspace():
            # If space is detected in the middle of a code, replace code with _ and reset morse_buffer
            if morse_buffer:
                logger.warning("Space in the middle of Morse code!")
                logger.warning("current morse code in the buffer %s is invalidated.", morse_buffer)
                result += "_"
                morse_buffer = ""
            result += ch
        elif ch in ['*', '-']:
            morse_buffer += ch
        else:
            # If invalid character is detected, replace possible morse code with _ and reset the morse_buffer
            logger.warning("%s is not a valid character in a Morse code!", ch)
            if morse_buffer:
                logger.warning("current morse code in the buffer %s is invalidated.", morse_buffer)
                result += "_"
            morse_buffer = ""
    return result


def main(args):
    logger.debug("main function started with arguments")
    logger.debug(args)
    
    # Select which function to use for converting lines.
    if args.M:
        logger.info("Converting Morse code to English")
        line_convert_function = convert_morse
    else:
        logger.info("Converting English to Morse code")
        line_convert_function = convert_english
    logger.info("from input file %s to output file %s", args.input, args.output)

    # Convert the contents of input file to the output file a line at a time.
    with open(os.path.abspath(args.input), 'r') as input:
        with open(os.path.abspath(args.output), 'w') as output:
            for line in input:
                output.write(line_convert_function(line))
    logger.info("Conversion finished")


def parse_args(args):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', type=str, default='input.txt', help='input file path')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='output file path')
    parser.add_argument('-M', action='store_true', 
        help='If set will convert Morse code to English. Normally converts from English to Morse code')
    
    args = parser.parse_args()
    if not os.path.exists(args.input):
        parser.error("Input file {} does not exist!".format(args.input))
    if os.path.exists(args.output):
        user_input = input(
            "Output file {} already exists. Do you want to overwrite it? (press y to overwrite)".format(args.output))
        if user_input != "y":
            sys.exit("File not converted!")
    return args


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
    main(parse_args(sys.argv[1:]))
