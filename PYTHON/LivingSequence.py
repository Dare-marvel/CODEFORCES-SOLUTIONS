# Link : https://codeforces.com/problemset/problem/1811/E

# Key Insights :

# Code :
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
    convLiveSeq()  # call previously defined function to convert and print the live sequence for each test case
