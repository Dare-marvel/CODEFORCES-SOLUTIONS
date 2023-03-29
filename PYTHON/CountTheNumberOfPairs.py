# Link : https://codeforces.com/problemset/problem/1800/B

# Key Insight : 

# Code :
# read the number of test cases
t = int(input())

# loop over the test cases
for _ in range(t):
    # read the values of n and k for this test case
    n, k = map(int, input().split())
    
    # read the string for this test case
    newL = list(input().strip())  # strip() added to remove trailing whitespace
    
    # initialize a dictionary to store the frequency of each character in the string
    burDict = {}
    
    # loop over the characters in the string and update the dictionary
    for let in set(newL):
        burDict[let] = newL.count(let)
    
    # initialize a variable to store the number of pairs of characters that can be removed
    burl = 0
    
    # loop over the characters in the dictionary
    for char in burDict:
        # check if the uppercase/lowercase counterpart of the character is also in the dictionary
        if char.swapcase() in burDict:
            # remove pairs of characters until one of the characters has no more remaining pairs
            while burDict[char] > 0 and burDict[char.swapcase()] > 0:
                burDict[char] -= 1
                burDict[char.swapcase()] -= 1
                burl += 1
    
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
