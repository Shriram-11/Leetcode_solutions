s = input('Enter')
s1 = ''
for a in s:
    if a == ' ':
        s1 += '_'
    else:
        s1 += a
print(s1)
