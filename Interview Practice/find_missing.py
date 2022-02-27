class Miss:
    def find_missing(self,l):
        for i in range (1, max(l)):
            if i not in l:
                print(str(i) + " is not found in the array")

print ("Enter an array of numbers with space")
arr = list(map(int,input().split()))
m = Miss()
m.find_missing(arr)