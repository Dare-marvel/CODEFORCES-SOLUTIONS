### [Playing in A Casino](https://codeforces.com/problemset/problem/1808/B)

## Key Insights:
For each column, the contribution to the answer depends only on the values in the column, not on their position in the matrix.<br>
The contribution of each value in a column to the answer depends on the sum of all values in the column and the position of the value in the sorted list of values.<br>
Sorting the list of values in a column allows us to efficiently compute the contribution of each value to the answer.<br>
The total answer is the sum of the contributions of all values in all columns.<br>

## Time and Space Complexity:
* Time Complexity
The time complexity of the above approach is O(nm log n), where n is the number of rows and m is the number of columns of the matrix. This is because the algorithm iterates over each column and performs a sort operation on the column, which takes O(n log n) time.

* Space Complexity 
The space complexity of the algorithm is O(nm), as it creates a new list temp of size n for each column, and also creates a variable col_sum to store the sum of the values in the column. Additionally, the a matrix takes up O(nm) space in memory. Overall, the space complexity is dominated by the matrix itself.

## Code:
```python
# This function compares two columns based on the sum of their values.
# It returns True if the sum of v1 is less than the sum of v2, and False otherwise.
def compare_col(v1, v2):
    return v1[1] < v2[1]

# This function reads the input, solves the problem, and prints the answer.
def sol():
    # Read the dimensions of the matrix.
    n, m = map(int, input().split())
    # Read the matrix.
    a = [list(map(int, input().split())) for _ in range(n)]
    # Initialize the answer to zero.
    ans = 0
    # For each column of the matrix:
    for i in range(m):
        # Create a list of the values in the column.
        temp = []
        # Compute the sum of the values in the column.
        col_sum = 0
        # For each row of the matrix:
        for j in range(n):
            # Add the value in the column to the list.
            temp.append(a[j][i])
            # Add the value in the column to the sum.
            col_sum += a[j][i]
        # Initialize the current sum to zero.
        curr = 0
        # Sort the list of values in the column.
        temp.sort()
        # For each value in the sorted list:
        for j in range(n):
            # Add the value to the current sum.
            curr += temp[j]
            # Compute the contribution of this value to the answer.
            ans += abs((col_sum - curr) - (n - 1 - j) * temp[j])
    # Print the answer.
    print(ans)

# Read the number of test cases.
t = int(input())
# For each test case:
for _ in range(t):
    # Solve the problem.
    sol()

```
