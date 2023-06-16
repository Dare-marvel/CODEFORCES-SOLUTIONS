### [Teleporters (Easy Version)](https://codeforces.com/problemset/problem/1791/G1)

## Key Insights : 
Add the respective indexes starting from 1 to each value of cost of teleportation list<br>
Sort the list <br>
Find the minimum sum less than or equal to number of coins we have from the list<br>


## Code :
```python
# Read the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):

    # Read the input values
    n, c = map(int, input().split())

    # Read the values at which teleporters are present and set their indices accordingly starting from 1
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
 ```
