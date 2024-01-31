s = '0' + '1' * 45
while '0' in s or '01' in s:
    if '01' in s:
        s = s.replace('01', '10')
    else:
        s = s.replace('0', '111')
print(s.count('1'))
