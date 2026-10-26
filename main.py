print("What Can I Make?")

ingredients = input("Enter your ingredients separated by commas: ")

if ingredients.strip() == "":
    print("You did not enter any ingredients.")
else:
    ingredient_list = ingredients.split(",")
    print("Your ingredients are:")
    
    for ingredient in ingredient_list:
        print(ingredient.strip())