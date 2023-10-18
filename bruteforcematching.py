import itertools

# Preference matrices for men and women
"""In the input matrices below, such as men's preferences and women's preferences, 
I am assuming that the first row of the men's preference matrix shows the preferences
of Men 1, and row 2 represents Men 2, and so on. The same applies to the women's preference matrix."""
men_prefs = [
    [1, 6, 5, 2, 4, 3, 7],
    [1, 4, 3, 2, 7, 6, 5],
    [7, 6, 5, 1, 2, 4, 3],
    [4, 3, 1, 2, 5, 7, 6],
    [3, 2, 1, 4, 5, 6, 7],
    [7, 6, 5, 4, 3, 2, 1],
    [6, 7, 4, 5, 3, 2, 1],
]

women_prefs = [
    [2, 6, 5, 1, 4, 3, 7],
    [1, 2, 5, 4, 3, 6, 7],
    [5, 3, 1, 2, 4, 7, 6],
    [4, 3, 1, 2, 5, 7, 6],
    [2, 3, 4, 1, 7, 6, 5],
    [7, 6, 5, 1, 2, 4, 3],
    [6, 5, 4, 7, 3, 2, 1],
]
num_pairs = len(men_prefs)                 # Get the number of pairs in the matching
def is_stable(matching, men_prefs, women_prefs):           
    for man in range(num_pairs):           # Iterate through each man in the matching
        woman = matching[man]              # Get the woman paired with the current man
        for other_man in range(num_pairs): # Iterate through all other men in the matching
            if other_man != man:           # Avoid comparing the man to himself
                other_woman = matching[other_man]  # Get the woman paired with the other man
                if (                       # Check if the current matching is unstable
                    (men_prefs[man].index(woman + 1) > men_prefs[man].index(other_woman + 1)
                    and women_prefs[woman].index(man + 1) > women_prefs[woman].index(other_man + 1))
                    or  
                    (men_prefs[other_man].index(other_woman + 1) > men_prefs[other_man].index(woman + 1)
                    and women_prefs[other_woman].index(other_man + 1) > women_prefs[other_woman].index(man + 1))
                ):
                    return False            # Matching is unstable
    return True                            # Matching is stable

def find_all_possible_matchings(): 
    all_possible_matchings = []            # List to store all possible matchings    
    men_permutations = itertools.permutations(range(num_pairs)) # Generate all possible permutations of men O(n!)  
    for permutation in men_permutations:   # Generate all possible matchings based on permutations
        matching = list(permutation)       # Create a matching from the permutation
        all_possible_matchings.append(matching)  # Add the matching to the list
    return all_possible_matchings

possible_matchings = find_all_possible_matchings() # Find all possible stable matchings

# Display all possible stable matchings
for i, matching in enumerate(possible_matchings):
    if is_stable(matching, men_prefs, women_prefs):
        print(f"Stable Matching {i + 1}:")
        for man in range(len(matching)):
            print(f"  Man {man + 1} <-> Woman {matching[man] + 1}")  # Display the stable matching
 
