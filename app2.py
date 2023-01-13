#The application in this file will read the command line options using getopt().
# This application should accept the flags -h or --help to print a help text.
# This application should let the user set a name with the option -n [NAME] or --name=[NAME].
# If a name is given, the application should output Good Morning [NAME]!. If no name is specified, it should just output Good Morning folks!


import sys
import getopt

file_name = sys.argv[0]
rest_of_the_command_line = sys.argv[1:]

x, y = getopt.getopt(rest_of_the_command_line, "hn:", ["help", "name="])
name = None



for i in x:
    print(i)
    if i[0] == "-h" or i[0] == "--help":
        print("How can I help you?")
    elif i[0] == "-n" or i[0] == "--name":
        name = i[1]

if name:
    print("Hello", name)
else:
    print("Good morning folks!")