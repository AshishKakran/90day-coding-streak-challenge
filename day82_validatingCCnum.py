# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

check1 = r'(?=(.)(-?\1){3,}.*)' # repeat
validcredit = r'^(4|5|6)[0-9]{3}(-?[0-9]{4}){3}$'

check1 = re.compile(check1)
check2 = re.compile(validcredit)

t = int(input())

for i in range(t):
    num = input()
    if check1.search(num):
        print("Invalid")
    elif check2.match(num):
        print("Valid")
    else:
        print("Invalid")
    

