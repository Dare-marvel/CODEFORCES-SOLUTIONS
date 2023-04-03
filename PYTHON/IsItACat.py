# Link : https://codeforces.com/contest/1800/problem/A

# Key Insight : We convert the string to lowercase 
# We loop over the entire string once and add the current character to the result string if current character is not equal to next character
# By this we eliminate the duplicates in the string 
# finally we check whether the string is equal to 'meow' or not and return the result accordingly

# Taking input for the number of test cases
t = int(input())

# Running the loop for the number of test cases
for i in range(t):

    # Taking input for the length of the string and converting it to lowercase
    n = int(input())
    catStr = input().lower()

    # Setting result to empty string
    result = ''

    # Looping through the string to check for consecutive identical characters
    for i in range(len(catStr)-1):

        # If the current character is not equal to the next character, add the current character to result
        if catStr[i] != catStr[i+1]:
            result += catStr[i]

    # Add the last character to result
    result += catStr[-1]

    # Check if the resulting string is 'meow', and print the appropriate output
    if result == 'meow':
        print("Yes")
    else:
        print('No')
