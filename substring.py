# "Without own words"
# Please write a program that prints out "Hello Gregor". The challenge is that you are not allowed to create own chars & strings. You are only allowed to use elements of a given string provided in the solution.py file.
#
# Output
# "Hello Gregor"


given_string = """One morning, when Gregor Samsa woke from troubled dreams,
he found himself transformed in his bed into a horrible vermin.
 He lay on his armour-like back, and if he lifted his head a
little he could see his brown belly, slightly domed and divided by
arches into stiff sections. The bedding was hardly able to cover
it and seemed ready to slide off any moment. His many legs, pitifully
thin compared with the size of the rest of him, waved about helplessly
as he looked."""

# to find the locations I used:
# print(given_string.find("Gre"))

a = given_string[14:16]
b = given_string[183:189:4]
c = given_string[5]
d = given_string[17:24]
print((a + b + c + d).title())