'''
Created on Aug 5, 2015
CodeEval Challenges - Details
The detail Y starts moving left (without any turn) until it bumps into the X 
detail at least with one cell. Determine by how many cells the detail Y will be moved. 
@author: toughbook
'''

if __name__ == '__main__':
    #import sys     if I wanna read the file by parameter
    test_cases = open('test', 'r')
    for test in test_cases:
        part = test.split(',')
        li=[]
        for a in part:
            i = 0
            p = i + 1
            c = 0
            mini = len(a)
            while i < len(a) and p < len(a):
                if a[i] != a[p]:
                    if a[p] == '.':
                        p += 1
                        c += 1
                    elif a[p] == 'Y':
                        if c < mini:
                            mini = c
                            break 
                else:
                    i = p
                    p = i + 1
                    c = 0
            li.append(mini)
        print(min(li))
    test_cases.close()
         
                
    
