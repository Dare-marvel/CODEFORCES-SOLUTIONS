### [Living Sequence](https://codeforces.com/problemset/problem/1811/E)

## Key Insights : 
For solving problems related to sequences use the following site : [OEIS](https://oeis.org/)<br>
Here we can as there are only 9 different types of numbers in the number system , it's a number system of base 9<br>
Hence as per the logic given on site : <br>
FORMULA:<br>
### a(n) = replace digits d > 3 by d + 1 in base-9 representation of n - 1.<br>
Hence we first convert the given index to a number to the base 9<br>
and then we replace each digit greater than 3 by (digit + 1)<br>

## Code :
```python
def decimalTobase9(num):
    digits = []
    if num == 0:
        return '0'
    while num != 0:
        digits.append(num % 9)  # take the remainder when dividing by 9 and append to list
        num //= 9  # integer divide by 9 to get the quotient
    return digits[::-1]  # reverse the list and return

def convLiveSeq():
    num = int(input())  # read integer input from user
    finalOp = []  # initialize an empty list
    base9 = decimalTobase9(num)  # convert input to base-9 using previously defined function
    for num in base9:  # loop through each digit in the base-9 representation
        if num > 3:  # if the digit is greater than 3, add 1 to it
            num +=1
        finalOp.append(str(num))  # convert the digit to a string and append to final output list
    print(''.join(finalOp))  # join the output list into a string and print to console

t = int(input())  # read number of test cases from user
for _ in range(t):  # loop through each test case
    convLiveSeq()  # call previously defined function to print the number at the desired index in the live sequence
```
