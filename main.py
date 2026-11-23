# Main program stuff goes here
from recipes import fetch_api_recipes, load_recipes
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


        # Attempt API first
        matches = fetch_api_recipes(clean_ingredients)

        # If API not usable (returned None), fall back to local recipes
        if matches is None:
            print("Using local recipes instead.")
            recipes = load_recipes()
            matches = find_matches(clean_ingredients, recipes)

        if len(matches) == 0:
            print("No matching recipes found.")

        else:
            print("Here are all the recipes you can make!")
            for recipe in matches:
                print("- " + recipe["name"])

                # API recipes may be missing a few ingredients
                if recipe.get("missing"):
                    print("  Missing ingredients: " + ", ".join(recipe["missing"]))
            choice = input("Please select a recipe to make by entering the name: ")

            selected_recipe = None

            while selected_recipe is None:
                for recipe in matches:
                    if choice.strip().lower() == recipe["name"].lower():
                        selected_recipe = recipe
                        break

                if selected_recipe is None:
                    print("Invalid selection. Please choose a recipe from the list.")
                    choice = input("Enter the name of a recipe: ")

            print("You have selected: " + selected_recipe["name"])
            

if __name__ == "__main__":
    main()
