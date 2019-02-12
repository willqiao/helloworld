def balance_check(str):
    stack = []
    if len(str) <= 1:
        return False
    for char in str:
        if char == "{" or char == "(" or char == "[":
            stack.append(char)
        else:
            if len(stack) > 0:
                temp = stack.pop()
                if temp == "{" and char != "}":
                    return False
                elif temp == "(" and char != ")":
                    return False
                elif temp == "[" and char != "]":
                    return False
            else:
                return False
    
    if len(stack) > 0:
        return False
    else:
        return True


print(balance_check("({["))