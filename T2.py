def check(s):
    stack = []
    result = [' '] * len(s)  #

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result[i] = '?'

    while stack:
        result[stack.pop()] = 'x'

    return ''.join(result)

if __name__ == "__main__":
    try:
        while True:
            s = input().strip()
            if not s:
                break
            print(s)
            print(check(s))
    except EOFError:
        pass
