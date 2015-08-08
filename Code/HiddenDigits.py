'''
Created on Aug 8, 2015
CodeEval Challenges - Hidden Digits
In this challenge you're given a random string containing hidden and visible digits.
The digits are hidden behind lower case latin letters as follows: 0 is behind 'a', 1 
is behind ' b ' etc., 9 is behind 'j'. Any other symbol in the string means nothing 
and has to be ignored. So the challenge is to find all visible and hidden digits in 
the string and print them out in order of their appearance. 
@author: toughbook
'''

if __name__ == '__main__':
    #import sys        if I wanna read the file by parameter
    test_cases = open('tests/testHiddenDigits', 'r')
    li = []
    for test in test_cases:
        str1 = ''
        for i in test:
            if i == 'a':
                str1 = str1 + '0'
            elif i == 'b':
                str1 = str1 + '1'
            elif i == 'c':
                str1 = str1 + '2'
            elif i == 'd':
                str1 = str1 + '3'
            elif i == 'e':
                str1 = str1 + '4'
            elif i == 'f':
                str1 = str1 + '5'
            elif i == 'g':
                str1 = str1 + '6'
            elif i == 'h':
                str1 = str1 + '7'
            elif i == 'i':
                str1 = str1 + '8'
            elif i == 'j':
                str1 = str1 + '9'
            elif i == '0':
                str1 = str1 + '0'
            elif i == '1':
                str1 = str1 + '1'
            elif i == '2':
                str1 = str1 + '2'
            elif i == '3':
                str1 = str1 + '3'
            elif i == '4':
                str1 = str1 + '4'
            elif i == '5':
                str1 = str1 + '5'
            elif i == '6':
                str1 = str1 + '6'
            elif i == '7':
                str1 = str1 + '7'
            elif i == '8':
                str1 = str1 + '8'
            elif i == '9':
                str1 = str1 + '9'
        if str1 != '':
            li.append(str1)
        else:
            li.append('NONE')
    for i in li:
        print(i)
    test_cases.close()
