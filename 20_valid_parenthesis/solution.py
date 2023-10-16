
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) < 2:
        return False

    open = ['(', '[', '{']
    close = [')', ']', '}']
    stk = []
    for a in s:
        if a in open:
            stk.append(a)
        elif a in close and len(stk) > 0:
            if open.index(stk.pop()) != close.index(a):
                return True
            else:
                return False
        else:
            return False
    if len(stk) == 0:
        return True
    return False
