def sort_baasesdOnFreeQ(lst):
    prev=0
    exist_lst=[]
    sort_lst=[]
    for i in lst:
        if i not in exist_lst:
            exist_lst.append(i)
            count=lst.count(i)
            if count>prev:
                for k in range(count):
                    sort_lst.insert(0,i)
            else:
                for j in range(count):
                    sort_lst.append(i)
            prev=count
    return sort_lst  

# print(sort_baasesdOnFreeQ([4,4,6,3,1,1,1]))   
print(sort_baasesdOnFreeQ([4, 4, 1, 1, 1, 3, 6]))            
                    
    
                
            
            
        
        
        