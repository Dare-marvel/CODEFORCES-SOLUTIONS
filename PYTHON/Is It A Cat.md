### [Is It A Cat](https://codeforces.com/contest/1800/problem/A)

## Key Insights : 
We convert the string to lowercase<br>
We loop over the entire string once and add the current character to the result string if current character is not equal to next character<br>
By this we eliminate the duplicates in the string <br>
finally we check whether the string is equal to 'meow' or not and return the result accordingly<br>

## Code :
```python
t = int(input()) # Taking input for the number of test cases

for i in range(t): # Taking input for the number of test cases

    n = int(input())  # Taking input for the length of the string and converting it to lowercase
    catStr = input().lower()

    result = '' # Setting result to empty string

    for i in range(len(catStr)-1): # Looping through the string to check for consecutive identical characters

        if catStr[i] != catStr[i+1]: # If the current character is not equal to the next character, add the current character to result
            result += catStr[i]

    result += catStr[-1] # Add the last character to result

    if result == 'meow': # Check if the resulting string is 'meow', and print the appropriate output
        print("Yes")
    else:
        print('No')
```
