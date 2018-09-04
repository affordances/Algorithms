#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    counts = {}
    for key, value in recipe.items():
        if not key in ingredients:
            return 0
        elif key in counts:
            counts[key] += ingredients[key] // recipe[key]
        else:
            counts[key] = ingredients[key] // recipe[key]
    return min(counts.values())


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
