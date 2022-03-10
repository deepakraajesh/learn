if __name__ == '__main__':
    records=[]
    marks=[]
    stored = []
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp=[name,score]
        records.append(temp)
        
    for i in range(0,len(records)):
        if records[i][1] not in stored:
            stored.append(records[i][1])
    stored.sort()
    
    for i in range(0,len(records)):
        if (records[i][1]==stored[1]):
            result.append(records[i][0])

    result.sort()
    for i in result:
        print(i)