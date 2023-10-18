# Stable-Matching
Comparing brute force approach and Gale Shapley algorithm for stable matching

Preference matrix of both Men and Women
<img width="851" alt="Screenshot 2023-10-17 at 8 25 44 PM" src="https://github.com/KishorekumarBS/Stable-Matching/assets/69570231/9906ce90-3c05-478c-ad66-73e3ff6ce9f3">


## Brutte force:
### i. is_stable Function:
>•	The is_stable function checks whether a given matching (a pairing of men and women) is stable or not.<br>
>•	It takes three arguments:<br>
>>•	matching: A list that represents the current matching, where the index of each element corresponds to a man, and the value at that index corresponds to the woman he is matched with.<br>
>>•	men_prefs: The preference matrix for men.<br>
>>•	women_prefs: The preference matrix for women.<br>
•	The function iterates through each man in the matching and compares his current partner with all other men in the matching to determine if there's a more preferred partner for him.<br>
•	It checks if any man would prefer another woman over his current partner, and if any woman would prefer another man over her current partner.<br>
•	If such a preference inversion exists for any pair, the matching is considered unstable, and the function returns False. Otherwise, it returns True to indicate that the matching is stable.<br>

### ii. find_all_possible_matchings Function:
>•	The find_all_possible_matchings function generates all possible matchings of men and women based on permutations of men.<br>
>•	It initializes an empty list all_possible_matchings to store the generated matchings.<br>
>•	It uses itertools.permutations to generate all possible permutations of the indices of men (0 to N-1), where N is the number of men.<br>
>•	For each permutation, it creates a matching by pairing the men with women in the order specified by the permutation.<br>
>•	The generated matching is added to the all_possible_matchings list.<br>
>•	Finally, it returns the list of all possible matchings.<br>

## 2.	Time Complexity of brute force code:
>i.	Generating Permutations of Men:<br>
>>•	I am using itertools.permutations to generate all possible permutations of men. The number of permutations for 'n' men is n!, where 'n' is the number of men in the list.<br>
•	Time Complexity: O(n!)<br>
>ii.	Checking Stability of Each Matching:<br>
>>•	For each generated permutation, the code checks if it forms a stable matching by iterating through all men and comparing their preferences.<br>
>>•	For each man, it iterates through all other men in the matching. In the worst case, this results in (n-1) iterations for each man.<br>
>>•	Within the inner loop, it checks the preferences of each man and woman, which involves finding the index of their preferences in their respective preference matrices. This is done using the .index method, which can take up to 'n' comparisons.<br>
>>•	So, the time complexity for checking the stability of one matching is O(n^2).<br>
>iii.	Total Time Complexity:<br>
>>•	The total time complexity is the product of the time complexities of generating permutations and checking each permutation for stability.<br>
>>•	Total Time Complexity = O(n!) * O(n^2) = O(n! * n^2)<br>

### Output Screenshot:
>After seeing the number of operations, it takes to find the stable match, brute force the worst option to find the stable matching.<br>
<img width="215" alt="image" src="https://github.com/KishorekumarBS/Stable-Matching/assets/69570231/2fce6a36-a472-4689-af1f-ab8ba71fb1e2"><br>

## Gale Shapley:
### i.	Initialization:
>•	Calculating the total number of men and women (n) based on the length of the preference lists.<br>
>•	Initializing two lists, men_status and women_status, to represent the current status of men and women. -1 in these lists means that the person is free.<br>
>•	Initializing a list proposal to keep track of how many women each man has proposed to.<br>
### ii.	While Loop:
>•	The while loop runs until there are no free men left (-1 in men_status checks for this). =>worstcase: O(n)<br>
>•	For each man (indexed by man) in the loop:<br>
>>•	Check if the man is free (men_status[man] == -1).<br>
>>•	If the man is free, find the woman he wants to propose to from his preference list using proposals[man] as an index.<br>
>>•	Increment proposals[man] to remember that this man has proposed to one more woman.<br>
>>•	Check if the woman is also free (women_status[woman-1] == -1). If she is, they become a couple:<br>
>>>•	Set women_status[woman-1] to the man, indicating that this woman is no longer free.<br>
>>>•	Set men_status[man] to the woman, indicating that this man is no longer free.<br>
>>•	If the woman is not free, it means she already has a partner (current_husband):<br>
>>>•	Compare the current man's index in the woman's preference list (women_pref[woman-1].index(man + 1)) with the current husband's index in the woman's preference list (women_pref[woman-1].index(current_husband + 1)).<br>
>>>•	If the current man is preferred by the woman over her current husband, update the matching:<br>
>>>>•	Set women_status[woman-1] to the current man.<br>
>>>>•	Set men_status[man] to the woman.<br>
>>>>•	Set men_status[current_husband] to -1, indicating that the current husband is now free.<br>

### 2.	Time complexity:
>•	The while loop iterates until all men are matched, and in the worst case, it can run 'n' iterations because there are 'n' men. This while alone takes O(n). Inside the loop, there is a for loop:<br>
>>•	In each iteration of the while loop, the code performs operations related to proposing and updating the matching. These operations involve accessing preference lists and making comparisons. The dominant factor here is finding the woman's preference index, which takes O(n) time in the worst case because it searches through the preference list. Therefore, the code inside the while loop contributes O(n) to the time complexity.<br>
>So overall the time complexity is O(n^2).

### Output Screenshot:
<img width="337" alt="image" src="https://github.com/KishorekumarBS/Stable-Matching/assets/69570231/3c2fa8fc-7c5f-41b0-a442-214e58e50587">

