# Write a program to find all pairs of integer whose sum is equal to a given number

def findingPairs(list,num):
    pairsList=[]
    for i in range(len(list)):
        for j in range(i,len(list)):
            if list[i]==list[j]:
                continue
            elif list[i] + list[j]==num:
                pairsList.append([i,j])
                
    return pairsList
                
myList=[2,6,3,9,11]
print(findingPairs(myList,9))



# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pairsList=[]
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 if i==j:                          ----------------> LeetCODE
#                     continue
#                 elif nums[i] + nums[j]==target:
#                     pairsList.append(i)
#                     pairsList.append(j)

#         return pairsList