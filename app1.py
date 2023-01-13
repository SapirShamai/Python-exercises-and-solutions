# The application in this file will read the command line options using sys.argv.
# If one of the options is --help, it should output a small help text.
# If one of the options is --fast is should print the text "fast mode enabled" to the command line.
# If --fast is not one of the options it should print the text "slow mode enabled" to the command line.

import sys

#sys.argv = list in command line

file_name = sys.argv[0]
rest_of_the_command_line = sys.argv[1:]



if "-h" in rest_of_the_command_line or "--help" in rest_of_the_command_line:
    print("Do you need some help?\n" + "I recommend that you ask somebody else\n" + "I hope it helps")
if "--fast" in rest_of_the_command_line:
    print("fast mode enabled")
else:
    print("slow mode enabled")