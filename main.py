
import sys
import os
import argparse
import logging

logger = logging.getLogger(__name__)

MORSE_TABLE = {
    "A" : "*-"     ,
    "B" : "-***"   ,
    "C" : "-*-*"   ,
    "D" : "-**"    ,
    "E" : "*"      ,
    "F" : "**-*"   ,
    "G" : "--*"    ,
    "H" : "****"   ,
    "I" : "**"     ,
    "J" : "*---"   ,
    "K" : "-*-*"   ,
    "L" : "*-**"   ,
    "M" : "--"     ,
    "N" : "-*"     ,
    "O" : "---"    ,
    "P" : "*--*"   ,
    "Q" : "--*-"   ,
    "R" : "*-*"    ,
    "S" : "***"    ,
    "T" : "-"      ,
    "U" : "**-"    ,
    "V" : "***-"   ,
    "W" : "*--"    ,
    "X" : "-**-"   ,
    "Y" : "-*--"   ,
    "Z" : "--**"   ,
    "." : "*-*-*-" ,
    "," : "--**--" ,
    "?" : "**--**" ,
    "/" : "-**-*"  ,
    "@" : "*--*-*" ,
    "1" : "*----"  ,
    "2" : "**----" ,
    "3" : "***--"  ,
    "4" : "****-"  ,
    "5" : "*****"  ,
    "6" : "-****"  ,
    "7" : "--***"  ,
    "8" : "---**"  ,
    "9" : "----*"  ,
    "0" : "-----"
}

INVERTED_MORSE_TABLE = {v: k for k, v in MORSE_TABLE.items()}


def convert_morse_code_to_char(morse_code):
    pass

def main(args):
    logger.info("main function started with arguments")
    logger.info(args)
    # Eli Morse-koodissa merkit tulee erottaa pisteellä (.)
    # Tämä molempiin suuntiin
    # Välilyönnille ei näkynyt koodia, mutta säilytetään rivinvaihdot ja välilyönnit ennallaan
    # Sitten pitää vielä miettiä tehään merkeillä joita ei voi kääntää sekä virheellisellä morse-koodilla
    # Read input file
    if args.M:
        logger.info("Converting morse code to english")
        with open(os.path.abspath(args.input), 'r') as input:
            with open(os.path.abspath(args.output), 'w') as output:
                for line in input:
                    logger.info(line)
                    morse_buffer = ""
                    for ch in line:
                        if ch == '.':
                            logger.info(". detected. morse_buffer: %s", morse_buffer)
                            character = INVERTED_MORSE_TABLE.get(morse_buffer)
                            logger.info(character)
                            if character:
                                output.write(character)
                            else:
                                print("{} is not a valid morse code".format(morse_buffer))
                            morse_buffer = ""
                        elif ch.isspace():
                            output.write(ch)
                        else:
                            morse_buffer += ch
                        
    else:
        with open(os.path.abspath(args.input), 'r') as input:
            with open(os.path.abspath(args.output), 'w') as output:
                for line in input:
                    for ch in line:
                        if ch.isspace():
                            output.write(ch)
                        else:
                            morse_code = MORSE_TABLE.get(ch.upper())
                            if morse_code:
                                output.write(morse_code + '.')
            
    # If Morse flag set convert Morse to English
    
    # Else convert English to Morse
    # Write output to file


def parse_args(args):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', type=str, default='input.txt', help='input file path')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='output file path')
    parser.add_argument('-M', action='store_true', help='If set will convert Morse to English')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    main(parse_args(sys.argv[1:]))
