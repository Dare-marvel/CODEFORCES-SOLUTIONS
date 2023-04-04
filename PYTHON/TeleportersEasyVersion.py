# Link : https://codeforces.com/problemset/problem/1791/G1

# Key Insights : 
# Add the respective indexes starting from 1 to each value of cost of teleportation list
# Sort the list 
# Find the minimum sum less than or equal to number of coins we have from the list


# Code :
# Read the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):

    # Read the input values
    n, c = map(int, input().split())

    # Read the teleValues and add their corresponding index values
    teleValue = list(map(int, input().split()))
    for i, num in enumerate(teleValue):
        teleValue[i] += (i+1)

    # Sort the teleValues in increasing order
    teleValue.sort()

    # Initialize the variables for the while loop
    i, sumTrack = 0, 0

    # Continue adding the teleValues until the sum is greater than c
    while i < len(teleValue) and sumTrack + teleValue[i] <= c:
        sumTrack += teleValue[i]
        i += 1

    # Print the number of teleports used
    print(i)
