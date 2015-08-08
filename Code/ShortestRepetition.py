'''
Created on Aug 5, 2015
Write a program to determine the shortest repetition in a string.
A string is said to have period p if it can be formed by concatenating one or more 
repetitions of another string of length p. For example, the string "xyzxyzxyzxyz" 
has period 3, since it is formed by 4 repetitions of the string "xyz". It also has
periods 6 (two repetitions of "xyzxyz") and 12 (one repetition of "xyzxyzxyzxyz"). 
@author: toughbook
'''

if __name__ == '__main__':
    #import sys      if I wanna read the file by parameter
    test_cases = open('tests/testShortestRepetition', 'r')
    li = []
    for test in test_cases:
        i = 0
        p = i + 1
        stri = test[0]
        while p < len(test):
            if test[len(test)-1]!='\n':
                test=test+'\n'
            if test[0]==test[len(test)-2]:
                li.append(1)
                break
            elif test[i]!=test[p]:
                stri = stri + test[p]
                if test == stri:
                    li.append(len(stri)-1)
                p+=1
            else:
                li.append(len(stri))
                break
                
        
    for r in li:
        print(r)
             
        
        
        
        
        """
        li = []
        i = 0
        p = i + 1
        stri = test[0]
        while p < len(test):
            if test[0]==test[len(test)-2]:
                cant.append(1)
                break
            elif test[len(test)-1]!='\n':
                test=test+'\n'
            else:
                if test[i] != test[p] and test[p]!='\n':
                    stri = stri + test[p]
                    p += 1
                else:
                    li.append(stri)
                    stri = test[i]
                    i = p
                    p = i + 1

        if li:
            cant.append(len(li[0]))
        else:
            cant.append(len(stri))
    #for i in range(0,len(cant)):
     #   print(cant[i])
    for r in cant:
        print(r)
        """
            
            
                        
        
        """
        li = []
        i = 0
        p = i + 1
        stri = test[0]
        while i < len(test) and p < len(test):
            if test[i] != test[p]:
                stri = stri + test[p]
                p += 1                    print(test[p])

            else:
                li.append(stri)
                stri = test[i]
                i = p
                p = i + 1
            
        if not li:      #si la lista esta vacia  
            cant.append(stri.count(stri))
        else:
            cant.append(li.count(li[0]))
    for i in range(0,len(cant)):
        print('linea %d: %d '%(i,cant[i]+1))
        """
    test_cases.close()
