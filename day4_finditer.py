import re
s = input()
print("\n".join(match if (match := re.findall(r"(?=[^aeiou]([aeiou]{2,})[^aeiou])",s,re.IGNORECASE)) else ["-1"]))
