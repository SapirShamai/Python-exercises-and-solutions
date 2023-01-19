#You need to find the word "Nemo" in a given string and return its position in that string, like this:
#I found Nemo at [index]!



text = input("Enter your text here : ").lower()
if "nemo" in text:
    print("I found Nemo at ", text.find("nemo"), "!")
else:
    print("I cant find Nemo :(")