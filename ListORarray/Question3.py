#How to find maximum product of two integer number in the array where all elements are positive
def maxProduct(arr, n):
	    
	maximumproduct=0
	for i in range(len(arr)):
	    for j in range(i,len(arr)):
	        if i==j:
	            continue
	        else:
	            tempproduct=arr[i]*arr[j]
	            if maximumproduct <=tempproduct:
	                maximumproduct=tempproduct
	return maximumproduct


print(maxProduct([2,4,8,8,9],8))



# def maxProduct(self,arr, n):
	
#     arr.sort()                        -------------> GFG
#     ans = arr[-1] * arr[-2]
#     return ans	                