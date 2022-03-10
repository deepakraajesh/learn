def minion_game(string):
    vowels = ['A','E','I','O','U']
    kevinres = set()
    stuartres = set()
    allsubset = []

    for i in range(len(string)):
        temp = ""
        for j in range(i,len(string)):
            temp += string[j]
            allsubset.append(temp)

    for i in range(len(allsubset)):
        if allsubset[i][:1] not in vowels:
            stuartres.add(allsubset[i])
        elif allsubset[i][:1] in vowels:
            kevinres.add(allsubset[i])

    print("Total Subset:",allsubset)
    print("Stuart Has :",len(stuartres))
    print(stuartres)
    print("Kevin has: ", len(kevinres))
    print(kevinres)

        
if __name__ == '__main__':
    s = input()
    minion_game(s)


'''
The solution provided on Hackerrank is

def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")
        
#Refer VS Code for proper answer, the logic here might not get apply for all cases, but the VS Code solution will apply for new words as well.

if __name__ == '__main__':
    s = input()
    minion_game(s)
'''