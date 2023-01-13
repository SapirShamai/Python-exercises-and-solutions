# #The Secret of Love :
# Everyone wants to hide their secrets, especially if those are their love's secrets
# To help them we will write a cipher for their secrets.
#
# There will be inputs : the secret , love name, year of birth.
#
# Secret condition: The secret must be at least 8 characters.
#
# The cipher algorithm is :
# Concatenate the love secret with the love name
# Reverse the string
# Concatenate the revered string with the year of birth

a = 0
while a == 0:
    secret = input("Your secret: ")
    if len(secret) < 8:
        print("Please type in at least 8 characters")
    else:
        a += 1

name = input("Enter your love name: ")
year = input("year of birth: ")
x = secret + name
cipher = x[::-1] + year
y = cipher.replace(" ", "_")
print("your cipher:", y)