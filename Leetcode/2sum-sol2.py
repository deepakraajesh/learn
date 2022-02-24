nums = [1,2,4,3]
target = 6
hashm = {}
for i,val in enumerate(nums):
    diff = target - val
    if diff in hashm:
        return [hashm[diff],i]
    hashm[val]=i
return

""""
nums[1,2,4,3] & Target = 6
First loop = i=0 & val=1
6-1 = 5 (5 is not in hashmap)
index[0] => 1 added to hash map
HASHMAP NOW:
1 it's index

Second loop = i=1 & val=3
6-2=4
4 is not in hashmap. (4 is found in array but not on hashmap)
index[1] => 2 is added to hashmap
HASHMAP NOW;
1 it's index
2 it's index

Third loop = i=2 & val=4
6-4=2
2 is already found in HASHMAP

return (index of 2,index of 4)
"""