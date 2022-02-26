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