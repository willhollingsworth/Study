def timeConversion(s):
    if s[:2] == '12' and s[-2] == 'A':
        return '00'+s[2:-2]
    if s[-2] == 'P':
        if s[:2] == '12':
            return s[:-2]
        h = int(s[:2])+12
        return str(h)+s[2:-2]
    return s[:-2]
    
    
    
    
# print(timeConversion('07:05:45PM'))
print(timeConversion('12:45:54PM'))
# print(timeConversion('07:05:45AM'))