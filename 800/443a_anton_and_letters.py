import re
formatted = set(re.sub(r'[{},]', '', input()).split())
print(len(formatted))
