import unittest

import sys

def findSmallestInt(arr):

    min=arr[0]

    for item in arr:
        if min>item:
            min=item
        else:
            pass
    return min

def solution(string):
    result=[]
    int=1
    while int<=len(string):
        result.append(string[-int])
        int+=1
    return ''.join(result)

def duplicate_count1(text):
    myhash={}
    int=0
    duplicati=0
    while int<len(text.capitalize()):
        if text[int].capitalize() not in myhash.keys():
            myhash[text[int].capitalize()]=[text[int].capitalize(),1]
        else:
            pass
            myhash[text[int].capitalize()] = [myhash[text[int].capitalize()][0] ,myhash[text[int].capitalize()][1]+1 ]
        int += 1
    for key in myhash.keys():
        if myhash[key][1]>1:
            duplicati+=1
    print(myhash.items())
    print(str(duplicati))
    return duplicati


def duplicate_count2(text):
    singleList=[]
    duplicateList=[]
    duplicati=0
    for char in text.capitalize():
        if char.capitalize() in singleList and char.capitalize() not in duplicateList:
            duplicateList.append(char.capitalize())
        else:
            if char.capitalize() in duplicateList or char.capitalize() in singleList:
                pass
            else:
                singleList.append(char.capitalize())
    return len(duplicateList)


#Double Char
def double_char(s):
    l=['']
    for char in s:
        l.append(char)
        l.append(char)
    #print(''.join(l))

    return ''.join(l)
def summation(num):
    return sum(list(range(num+1)))









if __name__ == '__main__':
    duplicate_count2('indivissssibilitttty')
    double_char('String')
    test = unittest.TestCase ()
    test.assertEquals(double_char("String"),"SSttrriinngg")
    test.assertEquals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
    test.assertEquals(double_char("1234!_ "),"11223344!!__  ")
    test.assertEquals (findSmallestInt ([78 , 56 , 232 , 12 , 11 , 43]) , 11)
    test.assertEquals (findSmallestInt ([-78 , 56 , -2 , 12 , 8 , -33]) , -78)
    test.assertEquals (findSmallestInt ([0 , -1 - sys.maxsize , sys.maxsize]) , -1 - sys.maxsize)
    test.assertEquals (solution ('world'), 'dlrow')
    test.assertEquals (solution ('hello') , 'olleh')
    test.assertEquals (solution ('') , '')
    test.assertEquals (solution ('h') , 'h')
    test.assertEquals(summation(1), 1)
    test.assertEquals(summation(8), 36)