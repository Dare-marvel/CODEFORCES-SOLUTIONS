# Link : https://codeforces.com/problemset/problem/1800/B

# Key Insight : First we subtract the minimum frequency of the character and it's counterpart swapped case character(if it exists)
# Then we check whether any charcter has frequency more than one so that the case of one of them can be swapped and we can get a pair
# Also we need to check that we don't exceed the number of operation provided i.e. value of k , so we take the minimum of k and the 
# calculated value ( we divide the frequency by 2 because 2 characters make one pair ) and we are interested in the number of pairs

# Code :
# read the number of test cases
t = int(input())
# loop over the test cases
for _ in range(t):
    # read the values of n and k for this test case
    n, k = map(int, input().split())
    
    newL = list(input().strip())  # strip() added to remove trailing whitespace

    # initialize a dictionary to store the frequency of each character in the string
    burDict = {}

    # initialize a variable to store the number of pairs of characters that can be removed
    burl = 0

    # loop over the characters in the string and update the dictionary
    for let in set(newL):
        burDict[let] = newL.count(let)

    # loop over the characters in the dictionary
    for char in burDict:
        # check if the uppercase/lowercase counterpart of the character is also in the dictionary
        if char.swapcase() in burDict:
            if burDict[char] > 0 and burDict[char.swapcase()] > 0:
                # Directly adding the minimum number of pairs to the count of burls
                pairs_to_add = min(burDict[char], burDict[char.swapcase()])
                burl += pairs_to_add
                burDict[char] -= pairs_to_add
                burDict[char.swapcase()] -= pairs_to_add

    # loop over the characters in the dictionary again
    for i in burDict:
        # if the character has more than one occurrence and there are still pairs that can be removed
        if burDict[i] > 1 and k > 0:
            # calculate the number of pairs of this character that can be removed
            pairs_to_add = min(burDict[i] // 2, k)
            # update the total number of pairs and the remaining pairs
            burl += pairs_to_add
            k -= pairs_to_add
    # print the total number of pairs that can be removed for this test case
    print(burl)
