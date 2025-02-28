# Python Cookbook, 3rd Ed.
#
# Chapter: Function Definitions
# Recipe: Writing testable scripts with the script-library switch

# Subsection: There's more...

from pathlib import Path
from ch03.recipe_11 import distances

if __name__ == "__main__":
    for trip in 'trip_1.csv', 'trip_2.csv':
        distances(Path('data') / trip)

