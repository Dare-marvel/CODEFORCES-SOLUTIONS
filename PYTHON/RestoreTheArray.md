### [Restore The Array](https://codeforces.com/problemset/problem/1811/C)

## Key Insights:
The first element and the last element of the result is the same as input array<br>
Rest elements are calculated using min of the current element and the previous element<br>

## Time and Space Complexity:
`Time complexity:`

The for loop that constructs the new list a by finding the minimum of adjacent values runs n-2 times, so its time complexity is O(n).<br>

`Space complexity:`

The space used by the program is dominated by the lists b and a, which each take up O(n) space.<br>
Therefore, the overall space complexity of the code is O(n).<br>

## Code:
```python
# Read in the number of test cases
t = int(input())

# Loop over each test case
for _ in range(t):
    # Read in the length of the list and the list itself
    n = int(input())
    b = list(map(int,input().split()))

    # Compute the new list a based on the values in b
    a = []
    a.append(b[0])
    for i in range(1,len(b)):
        a.append(min(b[i-1],b[i]))
    a.append(b[len(b)-1])

    # Print the elements of a on a single line, separated by spaces
    for element in a:
        print(element,end=" ")
```
