import re

txt = "We need to inform him with latest information."
for i in re.finditer('inform', txt):
    lockup = i.span()
    print(lockup)