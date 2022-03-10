s,num = input(),input().split()
print(all([int(i)>0 for i in num]) and any([j==j[::-1] for j in num]))

'''
#ANOTHER WAY OF SOLVING MY MATHEMATICAL EXPRESSION

s,num = input(),list(map(int,input().split()))
print(all(i>0 for i in num) and any(i < 10 or i % 11 == 0 for i in num))

#4 digit palindrom numbers are divisble by 11. (It might get deviate in rare cases)
'''