# Link to the problem : https://codeforces.com/problemset/problem/1809/A

# Take an integer input t - the number of test cases
t = int(input())

# Loop through each test case
for i in range(t):
    
    # Take a string input num - the number for the current test case
    num = str(input())
    
    # Initialize maxc to 0
    maxc = 0
    
    # Convert the string num into a list l
    l = list(num)
    
    # If all the characters in the list are the same, then the answer is -1
    if len(set(l)) == 1:
        print('-1')
    else:
        # Loop through each unique character in the list l
        for i in set(l):
            
            # Find the maximum frequency of any character in the list l
            maxc = max(l.count(i), maxc)
        
        # If the maximum frequency is 1 or 2, then the answer is 4
        if maxc == 2 or maxc == 1:
            print('4')
        # If the maximum frequency is 3 or more, then the answer is 6
        else:
            print('6')
