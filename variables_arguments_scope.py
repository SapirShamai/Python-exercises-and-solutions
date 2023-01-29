# Task1:
#Define a global variable named settings as a dictionary with a key title that contains a string of your choice,
# then create a function named change_site_title that takes one argument of type String
# and assigns it to the key title in the global variable settings.

settings = {"my_title": "Hello my title!", "pages": []}
#print(settings)

def change_site_title(title):
    # this function changes the title (in setting) which is a global variable in a different value
    settings["my_title"] = title

change_site_title("new title!!!!!!")   # now settings has changed
print(settings)

# Task2:
# Keep the previous code and define now a global variable named default_settings as a dictionary with a key title,
# then create a function named get_title that takes one argument
# as a dictionary that defaults to default_settings and returns the content of the key title in the given dictionary.

default_setting = {"my_title": "My original title", "pages": []}

def get_title(arg= default_setting): # this function has a default value and it's returning the value of the dictionary
    return arg

print(get_title())
print(get_title(settings))
change_site_title("New fancy title")   # im calling the function from before to put this new value inside settings
print(get_title(settings))
print(get_title())

# Task3.
# Add a key pages to your previous settings and default_settings dictionaries.
# Now, define two functions named get_pages and add_page. They will both have a parameter settings that will default to default_settings.
# The function get_pages will simply return the list stored in the key pages of the given settings dictionary.
# The function add_page will have an additional positional argument that will be the page as a dictionary.
# The function will append this argument to the pages key of the given settings dictionary.



def get_pages(settings2 = default_setting):

    return settings["pages"]

def add_page(pos_arg, settings2 = default_setting):

    return settings2["pages"].append(pos_arg)


home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))

# Task4:
# Create a new function named print_user_profile that will take 4 parameters:
# gender: a String indicating the gender of the user.The values available should be male and female. The default value should be female.
# first: a String with the first name of the user.
# The default value should be John if the gender is male but it should be Jane if the gender is female.
# last: a String with the last name of the user. The default value should be Doe.
# pictures: a List of strings with the name of the picture files. The default value should be an empty list.
# This function will add a common header picture to all profiles
# and then it will print on screen the name of the person and its list of pictures (including the common header). Example:


def print_user_profile(gender="female", first="Jane", last="Doe", pictures=[]):
    if gender == "male":
        first = "John"
    pictures = "\n".join(["common_header.png"] + pictures)
    return f"The user {first} {last} has the following pictures: \n{pictures}"

# TEST CASES:
test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print(print_user_profile(**test_data1))
#print(print_user_profile(**test_data2))
#print(print_user_profile(**test_data3))
#print(print_user_profile(**test_data2))