class check:
    def alpha(self,s):
        ans=False
        #contains Alphabet
        for i in s:
            if i.isalpha():
                ans = True
                break
        return ans
    
    def numb(self,s):
        ans=False
        #Contains Digit
        for i in s:
            if i.isdigit():
                ans = True
                break
        return ans

    def lower(self,s):
        ans=False
        #Contains Lowercase
        for i in s:
            if i.islower():
                ans = True
                break
        return ans

    def upper(self,s):
        ans=False
        #Contains Uppercase
        for i in s:
            if i.isupper():
                ans = True
                break
        return ans
        
if __name__ == '__main__':
    s = input()
    #is Alpha Numeric
    print (s.isalnum())
    ch = check()
    if(ch.alpha(s)):
        print("True")
    else:
        print("False")
    if(ch.numb(s)):
        print("True")
    else:
        print("False")
    if(ch.lower(s)):
        print("True")
    else:
        print("False")
    if(ch.upper(s)):
        print("True")
    else:
        print("False")
    