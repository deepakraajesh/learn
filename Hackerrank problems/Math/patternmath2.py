for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (((10**(i)//9)*(10**(i)//9)))
    # We have seen in previous problem that (10^i//9) generates 1,11,111,1111 etc until i =9
    # Here we need a palindrome number, so 1x1=1, 11x11=121, 111x111=12321 etc.. to generate this, instead of *i, we can use the same function to generates 1's depending upon i.