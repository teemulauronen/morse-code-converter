JAVA / PYTHON
=============
Write a simple program that converts English text to Morse code and vice versa. For example, English
text “SOS” should be converted to “•••−−−•••”. Converter is case insensiƟve, thus “sos” should
produce same output “•••−−−•••” as “SOS” does. When converted to English, everything should be
uppercased, thus “sos” converted to Morse and back to English should output “SOS”.

For this task, text (Either English or Morse) should be read from a file and output should be written to
another. Simple command line interface for usage is enough which asks for input and output files and
offers a way to do conversion from either English or Morse. Let's assume that every character is
separated from each other with a dot and there cannot be two dots in a row. When converting
backwards, the script should tell if there is a non valid morse code.

An imaginary customer will need a graphical user interface later, as well as other means for input, for
example via a graphical user interface or a REST API. Also, output needs to be saved to elsewhere later,
for example to a cloud database via REST API. A support for other languages will be implemented in the
future. There is no need to implement these features yet, but those future requirements should be kept
in mind in software design and structure.


Evaluation criteria:
* Design
* Structure
* Use of language features
* Clarity of implementation
* Error checking
* Comments
* Testability
* Documentation
* Usability
*