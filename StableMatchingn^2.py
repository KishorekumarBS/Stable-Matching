def gale_shapley(men_pref, women_pref):
    n = len(men_pref)
    # Initialize all men and women as free
    men_status = [-1] * n  # -1 represents free
    women_status = [-1] * n  # -1 represents free
    proposals = [0] * n #This list is to keep track of how many women have been proposed by each men

    # Continue until all men are matched
    while -1 in men_status:
        for man in range(n):
            # If the current man is free
            if men_status[man] == -1:
                # Get the woman he wants to propose to
                woman = men_pref[man][proposals[man]]
                proposals[man] += 1
                # If the woman is also free
                if women_status[woman-1] == -1:
                    women_status[woman-1] = man
                    men_status[man] = woman
                else:
                    # If the woman has a current partner (current_husband)
                    current_husband = women_status[woman-1]
                    # Check if the woman prefers the current man over her current partner
                    if women_pref[woman-1].index(man + 1) < women_pref[woman-1].index(current_husband + 1):
                        # If yes, update the matching
                        women_status[woman-1] = man
                        men_status[man] = woman
                        men_status[current_husband] = -1
    # Return the stable matching
    return men_status


# Define preference matrices (starting from 1)
"""In the input matrices below, such as men's preferences and women's preferences, 
I am assuming that the first row of the men's preference matrix shows the preferences
of Men 1, and row 2 represents Men 2, and so on. The same applies to the women's preference matrix."""

men_pref = [
    [1, 6, 5, 2, 4, 3, 7],
    [1, 4, 3, 2, 7, 6, 5],
    [7, 6, 5, 1, 2, 4, 3],
    [4, 3, 1, 2, 5, 7, 6],
    [3, 2, 1, 4, 5, 6, 7],
    [7, 6, 5, 4, 3, 2, 1],
    [6, 7, 4, 5, 3, 2, 1],
]

women_pref = [
    [2, 6, 5, 1, 4, 3, 7],
    [1, 2, 5, 4, 3, 6, 7],
    [5, 3, 1, 2, 4, 7, 6],
    [4, 3, 1, 2, 5, 7, 6],
    [2, 3, 4, 1, 7, 6, 5],
    [7, 6, 5, 1, 2, 4, 3],
    [6, 5, 4, 7, 3, 2, 1],
]

# Get the stable matching
matching = gale_shapley(men_pref, women_pref)

# Print the stable matching
for man, woman in enumerate(matching):
    print(f"Man {man + 1} is matched with Woman {woman}")
