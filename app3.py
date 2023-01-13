# The application in this file will read the command line options using argparse.
# This application should support positional arguments and be called like this: ./app3.py [FIRST_NAME] [LAST_NAME] [AGE]
# If age is not specified, it should be assumed that it is 100. If the last name is not specified, it should be assumed that it is "Hanson". If the first name is not specified, should be assumed that it is "Larry".
# This application should also support the option --fast. It should print "fast mode enabled" if this is one of the options.
# The app should then output the text "Hello [FIRST_NAME] [LAST_NAME]! I see that you have had [AGE + 1] birthdays.".


import argparse
parser = argparse.ArgumentParser()

parser.add_argument(

    "-f",
    "--first_name",
    metavar= "FIRST NAME",
    type=str,
    nargs="?",
    help="Enter your first name",
    default="Larry"

)

parser.add_argument(

    "-l",
    "--last_name",
    metavar="LAST NAME",
    type=str,
    nargs="?",
    help="Enter your last name",
    default="Hanson"
)

parser.add_argument(

    "-a",
    "--age",
    metavar="AGE",
    type=int,
    nargs="?",
    help="Enter your age",
    default="100"
)
parser.add_argument(
    "--fast",
    help="select fast mode",
    action="store_true"
)

run = parser.parse_args()
print("Hello", run.first_name, run.last_name, "! I see that you have had", (run.age + 1), "birthdays")
if run.fast:
    print("fast mode enabled")
else:
    print("slow mode enabled")