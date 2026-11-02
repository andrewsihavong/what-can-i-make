# Recipe matching goes here
# Compare what ingredients the user has with what each recipe needs
def find_matches(user_ingredients, recipes):
    """Find recipes that match the input of ingredients."""
    matches = []

    for recipe in recipes:
        recipe_ingredients = recipe["ingredients"]
        all_ingredients_found = True

        for ingredient in recipe_ingredients:
            if ingredient not in user_ingredients:
                all_ingredients_found = False

        if all_ingredients_found:
            matches.append(recipe)
    return matches
