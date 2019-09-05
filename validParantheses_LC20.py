BRACKET_MAP = {"[":"]", "{":"}", "(":")"}

def isValid(s):
    stack = []
    for bracket in s:
        if bracket in BRACKET_MAP:
            stack.append(BRACKET_MAP[bracket])
        elif not stack or bracket != stack.pop():
            return False
    return not stack

string = "{[]{()}}"
print(string, "-", isValid(string))

# Runtime: 12 ms, faster than 96.56% of Python online submissions for Valid Parentheses.
# Memory Usage: 11.9 MB, less than 39.50% of Python online submissions for Valid Parentheses.





