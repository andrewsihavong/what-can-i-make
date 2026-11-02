# Main program stuff goes here
from recipes import load_recipes
from matcher import find_matches

# This is where we get user input and connect everything together


def main():
    """Run the main recipe program."""

    print("What Can I Make?")

    ingredients = input("Enter your ingredients separated by commas: ")

    if ingredients.strip() == "":
        print("You did not enter any ingredients.")
    else:
        ingredient_list = ingredients.split(",")
        clean_ingredients = []

        for ingredient in ingredient_list:
            clean_ingredients.append(ingredient.strip().lower())
        recipes = load_recipes()
        matches = find_matches(clean_ingredients, recipes)

        if len(matches) == 0:
            print("No matching recipes found.")
        else:
            print("Here are all the recipes you can make!")
            for recipe in matches:
                print("- " + recipe["name"])


if __name__ == "__main__":
    main()
