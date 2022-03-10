import re
def wrapper(f):
    def fun(l):
        res = []
        out = []
        for i in range(len(l)):
            if(re.match("^\d{10}$",l[i])):
                res.append(l[i][0:10])
            elif(re.match("^0\d{10}$",l[i])):
                res.append(l[i][1:11])
            elif(re.match("^91\d{10}$",l[i])):
                res.append(l[i][2:12])
            elif(re.match("^\+91\d{10}$",l[i])):
                res.append(l[i][3:13])
            res.sort()
        for i in res:
            out.append("+91 "+i[0:5]+" "+i[5:10])
        print(*out, sep="\n")
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)