def check_symmetry(expression):
    stack = []
    opening = {'(': ')', '{': '}', '[': ']'}
    closing = {')', '}', ']'}

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack and opening[stack[-1]] == char:
                stack.pop()
            else:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"

# Приклади використання
examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for example in examples:
    result = check_symmetry(example)
    print(f"{example}: {result}")