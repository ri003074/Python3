import re

data = """
    start aaaaaaaa
        aaaaaaaa
        aaaaaaaa
    end
    start
        bbbbbbb
        bbbbbbb
        bbbbbbb
    end
"""

matches = re.findall("(start.*?end)", data, flags=re.DOTALL)

print(matches)
