#Is Unique :Implement an alogorithm to determine if a list has all unique characters ,using Python.
# def checkUnique(nums):
#     for i in nums:
#         count=nums.count(i)
#         if count >1:
#             return True
     
#     return False
        
# print(checkUnique([2,14,18,22,22]))




def isUnique(nums):
    if len(nums)==len(set(nums)):
        return False
    else:
        return True