def is_matched(expression):
    stack = []
    for c in expression:
        if c == '{' or c == '(' or c == '[':
            stack.append(c)
        else:
            if stack:
                bracket = stack.pop()
                if c == '}' and bracket != '{':
                    return False
                elif c == ']' and bracket != '[':
                    return False
                elif c == ')' and bracket != '(':
                    return False
            else:
                return False
    '''
    (!) (!) (!) 

    Was just returning True here, which ingonred the
    possibility that open brackets remained in the stack.
    
    (!) (!) (!)
    '''
    return len(stack) == 0 
            
t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")