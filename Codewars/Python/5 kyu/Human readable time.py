'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

import time
def make_readable(seconds):
    output = time.strftime('%H:%M:%S',(time.gmtime(seconds)))
    output = str(int(seconds/60/60)).zfill(2) + output[2:]
    return output



print(make_readable(0), "00:00:00")
print(make_readable(5), "00:00:05")
print(make_readable(60), "00:01:00")
print(make_readable(86399), "23:59:59")
print(make_readable(359999), "99:59:59")