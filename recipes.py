# Recipe data stuff goes here
# This file loads recipes from recipes.json and from the Spoonacular API.
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()  # Load API key environment variable from .env file

API_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def load_recipes():
    """Load recipes from the recipes.json file."""

    with open("data/recipes.json", "r") as file:
        recipes = json.load(file)

    return recipes

def fetch_api_recipes(ingredients, max_results=10):
    """Fetch recipes from the Spoonacular API based on the provided ingredients.

    Retuns a list of recipes in the format seen in recipes.json
    ({"name": "Recipe Name", "ingredients": ["ingredient1", "ingredient2", ...]})
    Returns None if the API could not be used, so the caller can fall back on local recipes.
    """

    api_key = os.environ.get("SPOONACULAR_API_KEY")
    if not api_key:
        print("Spoonacular API key not found.")
        return None

    params = {
        "apiKey": api_key,
        "ingredients": ",".join(ingredients),
        "number": max_results,  # Kept small because credits are charged per result with Spoonacular.
        "ranking": 1,           # 1 = maximize used ingredients, 2 = minimize missing ingredients
        "ignorePantry": True,   # Ignores pantry items like water, salt, etc.
    } 

    try:
        response = requests.get(API_URL, params=params, timeout = 5) # Use set params, times out after 5s

        # The free plan with Spoonacular will return 402 if the daily limit is exceeded
        if response.status_code == 402:
            print("The daily limit for the Spoonacular API has been exceeded.")
            return None

        response.raise_for_status()  # Raise an error for other HTTP errors
        data = response.json()
    except (requests.exceptions.RequestException, ValueError):
        print("Could not get recipes from the Spoonacular API. Local data will be used.")
        return None

    # Convert Spoonacular data into the format we are using in recipes.json
    recipes = []
    for item in data:
        used = [ing["name"].lower() for ing in item.get("usedIngredients", [])]
        missed = [ing["name"].lower() for ing in item.get("missedIngredients", [])]

        recipes.append({
            "name": item["title"],
            "ingredients": used + missed,
            "missing": missed,
        })

    return recipes