class Chess:
    def calc(self):
        n = int(input("Enter n value: "))
        ans = 0
        for i in range (0,n):
            ans = ans + ((i+1)*(i+1))
        print ("Number of Squares is", ans)

ch = Chess()
ch.calc()