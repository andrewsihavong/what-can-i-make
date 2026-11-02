# Tests for the recipe matching stuff
# Basically make sure matcher.py is giving the right results
from matcher import find_matches

def test_find_match():
    """Test that a matching recipe is found."""
    user_ingredients = ["bread", "cheese", "butter"]
    recipes = [
        {
            "name": "Grilled Cheese",
            "ingredients": ["bread", "cheese", "butter"]
        }
    ]
    matches = find_matches(user_ingredients, recipes)

    assert len(matches) == 1
    assert matches[0]["name"] == "Grilled Cheese"

def test_no_match():
    """Test that no recipe is found when ingredients are missing."""
    user_ingredients = ["bread", "cheese"]
    recipes = [
        {
            "name": "Grilled Cheese",
            "ingredients": ["bread", "cheese", "butter"]
        }
    ]
    matches = find_matches(user_ingredients, recipes)
    assert len(matches) == 0

def test_multiple_matches():
    """Test that more than one matching recipe can be found."""
    user_ingredients = ["bread", "ham", "cheese", "mayo"]
    recipes = [
        {
            "name": "Ham and Cheese Sandwich",
            "ingredients": ["bread","ham", "cheese","mayo"]
        },
        {
            "name": "Ham Sandwich",
            "ingredients": ["bread", "ham", "mayo"]
        }
    ]
    matches = find_matches(user_ingredients, recipes)
    assert len(matches) == 2