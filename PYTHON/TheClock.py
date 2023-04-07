# Link : https://codeforces.com/problemset/problem/1692/D

# Key Insights : We use the datetime object to reduce complications while adding time
# In the while loop we add time and check whether the string is palindromic or not until the newTime is not equal to currentTime

# Code : 
from datetime import datetime, timedelta 

# read the number of test cases
t = int(input())

# process each test case
for i in range(t):
    # read the start time and time increment
    s , x = input().split()
    x = int(x)
    
    # create a datetime object with the start time
    currTime = datetime(year=2023, month=4, day=7, hour=int(s[0:2]), minute=int(s[3:]))
    
    # initialize a counter for palindromic times
    count = 0
    
    # loop until we reach the original time again
    while True:
        # check if the current time is palindromic
        if currTime.hour // 10 == currTime.minute % 10 and currTime.hour % 10 == currTime.minute // 10:
            count += 1
        
        # increment the current time by x minutes
        currTime += timedelta(minutes=x)
        
        # exit the loop if we have reached the original time again
        if currTime.strftime('%H:%M') == s:
            break
    
    # print the number of palindromic times
    print(count)
