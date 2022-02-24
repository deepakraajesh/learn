class Miss:
    def find_missing(self):
        l=[1,8,6,4,5,3,2]
        l.sort()
        for i in range (0, l[-1]):
            if l[i]==i:
                continue
            else:
                print (i,"is missing here")