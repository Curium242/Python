"""Problem Statement
Convert time format
You have been given a time in the 12-hour AM/PM format. Your task is to convert the given time into military (24-hour) format.

Please note the following conversion rules:
12:00:00 AM on a 12-hour clock is equivalent to 00:00:00 on a 24-hour clock.
12:00:00 PM on a 12-hour clock is equivalent to 12:00:00 on a 24-hour clock.
Apply the following steps to convert the time format:
Analyze the given time in the 12-hour AM/PM format.
If the time is before noon (AM), leave it as is unless it is exactly 12:00:00 AM, which needs to be converted to 00:00:00 in the 24-hour format.
If the time is in the afternoon (PM), add 12 hours to the hour component of the time, except when it is exactly 12:00:00 PM, which remains the same in the 24-hour format.
Represent the converted time in the military (24-hour) format."""



import sys
def doSomething(inval):
    if 'AM' in inval:
        period = 'AM'
        time = inval.replace('AM', '')
    elif 'PM' in inval:
        period = 'PM'
        time = inval.replace('PM', '')
    hrs,mins,sec=map(int,time.split(':'))
    if period=="AM":
        if hrs==12:
            hrs=0
    else:
        if hrs!=12:
            hrs+=12
    outval="{:02d}:{:02d}:{:02d}".format(hrs,mins,sec)
    return outval
inputVal = input()    
outputVal = doSomething(inputVal)
print (outputVal)
                     