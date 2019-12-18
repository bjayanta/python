import re

pattern = r"[aeiou]"

if re.match(pattern,"anuuuuindbnudu"):
    print("Matched!")

if re.match(pattern, "ggggg"):
    print("Matched!")

pattern = r"[A-Z]+"
if re.match(pattern,"Aggggghhhh"):
    print("Matched!")