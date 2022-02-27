for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ([i for j in range (0,i)])
    #but this provides list of numbers
    '''
       [1]
       [2, 2]
       [3, 3 , 3]
       which is not required
    '''
    print (((10**(i)//9)*i))
    # We need to make first part as '1' so that 1timesi x i which is like
    # 1 x 1, 11 x 2, 111 x 3, 1111 x 4 and it goes on until 9 
    # (10^i//9) generates 1,11,111,1111 etc until i =9