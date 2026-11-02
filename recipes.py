# Recipe data stuff goes here
# This file loads recipes from recipes.json.
import json


def load_recipes():
    """Load recipes from the recipes.json file."""

    with open("data/recipes.json", "r") as file:
        recipes = json.load(file)

    return recipes
