import re
for i in range(int(input())):
    # color: #FFFFF -- this colon is mentioned in regex':?.'
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')