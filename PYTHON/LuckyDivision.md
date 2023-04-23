### [Lucky Division](https://codeforces.com/contest/122/problem/A)

## Brief Description:
If the lucky number divides the number evenly print 'YES' else print 'NO'

## Time and Space Complexity:
`Time Complexity`:
The time complexity of this code is O(1), which is constant time. 
This is because the code performs a fixed number of integer divisions and comparisons, regardless of the input value of n.

`Space Complexity`:
The space complexity of this code is also O(1), which is constant space. 
This is because the code only uses a fixed amount of memory to store the input integer n, a few integer constants for the lucky numbers, and a few boolean and string constants for the if statement and the print statement. 
The amount of memory used does not depend on the input value of n.

## Code:
```python
# Get the input integer from the user
n = int(input())

# Check if any of the lucky numbers divide the input integer
if n % 4 == 0 or n % 7 == 0 or n % 44 == 0 or n % 47 == 0 or n % 74 == 0 or n % 77 == 0 or n % 444 == 0 or n % 447 == 0 or n % 474 == 0 or n % 477 == 0:
    print('YES')
else:
    print('NO')

```
