### [Beppa and SwerChat](https://codeforces.com/problemset/problem/1776/H)

## Brief Description and Key Insights :
Instead of finding the minimum number of members that must have been online at least once<br>
between 9:00 and 22:00, let us study the complement of that set: What is the maximum number of<br>
members that have never been online? We have the following observations:<br>
• Members that have never been online must be a suffix of the sequence b. It cannot happen<br>
that member bi has been online but bi−1 has not, for 2 ≤ i ≤ n.<br>
• Consider two members x and y who have never been online. Their relative order in a and b is<br>
the same. Indeed, if someone else goes online the relative order of x and y in the list does not<br>
change.<br>
From the above observations, we deduce that the members who have not been online form a suffix<br>
of b that is also a subsequence of a. Let p : {1, 2, . . . , n} → {1, 2, . . . , n} be the function such<br>
that ap(x) = x; we say that a sequence s of length m is a subsequence of a if p(si−1) < p(si), for<br>
2 ≤ i ≤ m.<br>
It turns out that any “suffix of b that is a subsequence of a” can be a valid subset of members who<br>
have never been online as the following construction shows. For any such suffix bt, bt+1, . . . , bn, it<br>
could be that members bt−1, bt−2, . . . , b1 went online in this order between 9:00 and 22:00, leading<br>
to a valid list b of last seen online at 22:00.<br>
Thus, the answer to the problem is the length of the longest suffix of b that is also a subsequence<br>
of a. Let us explain how to find such length quickly.<br>
We first preprocess the sequence a to find the corresponding function p. Then, we iterate from bn<br>
to b1. If, for some i we discover that p(bi) < p(bi−1), then we know that bi−1 must have been online,<br>
and we denote this position i as r. In this way, br, br+1, . . . , bn is the sought longest suffix of b. The<br>
minimum number of members that must have been online at least once between 9:00 and 22:00 is<br>
then r − 1.

## Code :
```python
# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the size of the arrays
    n = int(input())
    
    # Read the elements of the arrays
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Create an array to map elements of a to their indices
    m = [0] * (n+1)
    for i in range(n):
        m[a[i]] = i
    
    # Iterate over the elements of b in reverse order
    k = 0
    for i in range(n-1, 0, -1):
        # If the current element is smaller than the previous element in b,
        # we have found the start of the suffix of b that is not a subsequence of a
        if m[b[i]] < m[b[i-1]]:
            k = i
            break
    
    # Print the index of the last element in the suffix
    print(k)

```
