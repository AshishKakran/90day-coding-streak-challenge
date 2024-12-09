
import re 

repeat = re.compile(r'(\w(?!_))\1') # first occurence of a repeating character

m  = re.search(repeat, input())


print(m.group(1)) if m else print(-1)

