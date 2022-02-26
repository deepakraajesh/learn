n = int(input())
lint, loct, lhex, lbin = [],[],[],[]
for i in range(0,n+1):
    lint.append(str(i))
    loct.append(str(oct(i))[2:])
    lhex.append(str(hex(i))[2:].upper())
    lbin.append(str(bin(i))[2:])

wid = len(lbin[-1])
for i in range(1,n+1):
    print(lint[i].rjust(wid)+" "+loct[i].rjust(wid)+" "+lhex[i].rjust(wid)+" "+lbin[i].rjust(wid))