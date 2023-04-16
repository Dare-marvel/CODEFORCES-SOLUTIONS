### [LinkToProblem](https://codeforces.com/problemset/problem/1808/B)

## Brief Description:

## Key Insights:

## Time and Space Complexity:

## Code:
```python
# Working solution
def compare_col(v1, v2):
    return v1[1] < v2[1]

def sol():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(m):
        temp = []
        col_sum = 0
        for j in range(n):
            temp.append(a[j][i])
            col_sum += a[j][i]
        curr = 0
        temp.sort()
        for j in range(n):
            curr += temp[j]
            ans += abs((col_sum - curr) - (n - 1 - j) * temp[j])
    print(ans)

t = int(input())
for _ in range(t):
    sol()

```
