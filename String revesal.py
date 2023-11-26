"""Problem Statement
Reverse a string
Imagine you are a software engineer working on a text processing application. Your task is to develop a function that reverses a given string while preserving the position of punctuation marks, spaces, and the case of the letters. This function will be used to process input from users and provide them with the reversed string as an output.

Example :
Input: "No lemon, no melon"
Output: "no lemon, no meloN"

Input: "Race car"
Output: "race caR"

Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

Exercise-1

Input:
Litcoder is best

Output:
tsebsire do ctiL
"""

import sys
def doSomething(inval):
    let = [a for a in inval if a.isalpha()]
    revlet = let[::-1]
    outval=''
    index=0
    for char in inval:
        if char.isalpha():
            outval+=revlet[index]
            index+=1
        else:
            outval+=char
    return outval
inputVal = input()    
outputVal = doSomething(inputVal)
print (outputVal)