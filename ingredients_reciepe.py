# the task was to create a short program to my choice.
# the user needs to input the ingredient and the program recommends a recipe .


name = input("Hello ! please enter your name : ")
print("hey", name, " \ntype in which ingredients you have and I can recommend a nice recipe,")
ingredients_list = ["Beef", "Fish", "Chicken", "Vegetable", "Bread", "Cheese", "Eggs"]
x = 0
while x == 0:
    ingredient = input("Because I'm a new program you will have to choose from our selection here : \n" + str(ingredients_list) + ":\n")
    if ingredient == "Beef":
        print("Spaghetti Meatballs")
    elif ingredient == "Fish":
        print("Fish and chips")
    elif ingredient == "Chicken":
        print("Chicken soup")
    elif ingredient == "Vegetables":
        print("Chinese stir fry vegetables")
    elif ingredient == "Bread":
        print("French toast")
    elif ingredient == "Cheese":
        print("Cheese cake")
    elif ingredient == "Eggs":
        print("Omelette")
    else:
        print("Sorry, I do not have a recipe for", ingredient, "you might have to do some shopping.")
        break

    answer = input("Sounds good ? Y/N:\n")
    if answer == "Y":
        x += 1
        print("I'm glad I could help\n", "Bon appetit !")
    else:
        print("So let's choose something else...")