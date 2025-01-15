import re
t = int(input())

# this relies on greedy nature of positive and negative lookahead
reg = re.compile(r'''
    (?=.*[A-Z].*[A-Z].*)        # at least two uppercase alphabets
    (?=.*[0-9].*[0-9].*[0-9].*) # at least three digits
    (?=\w{10})                  # only ten alphanumeric characters in total
    (?!.*(.).*\1.*)             # no repetition of the same characters
    ''', re.VERBOSE)

for i in range(t):
    if reg.match(input().strip()):
        print("Valid")
    else:
        print("Invalid")
