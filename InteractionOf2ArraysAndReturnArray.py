'''
Interaction of two arrays-
Problem: Given two integer arrays nums1 and nums2, 
return an array of their intersection. 
Each element in the result must be unique and 
you may return the result in any order.

ex1: Input: nums1 = [1,2,2,1]  nums2 = [2,2]  o/p: [2]
ex2: Input: nums1 = [4,9,5],   nums2=[9,4,9,8,4]   o/p: [9,4]
Explanation: [4,9] is also accepteed. 
'''
#-----------------------------------------------------------------------------------------
#First way is better for clarity & performance
#way1 : T.C = O(n+m) S.C=O(n+m)  Efficient? = Yes Comment=Best for performance & readability.
nums1=[2,4,3]
nums2= [4,6,2,1]
print( list(set(nums1) & set(nums2)) ) 
#interaction opertaion only works on set so convert list into set then use this opertaor.
#since a/c to Q return array ,so convert set into list back

#------------------------------------------------------------------------------------------
#Way2 : T.C = O(n+m) S.C= O(n+k)  Efficienct? = Yes Comment= Efficient but more manual
set1 =set(nums1)
result= set()
for num in nums2:
    if num in set1:
        result.add(num) #in set use add() for adding element in array use append()
print(list(result))  

#-------------------------------------------------------------------------------------------      
#Way3 : T.C = O(n*m)  S.C= O(k) Efficient? = No  Comment= inefficient for large data
result=[]
for num in nums1: #n time
    if num in nums2 and num not in result: #not use & for and Each element is added only once #m time, so algo takes n*m time
        result.append(num)
print(result)  
#let's supppose set1 takes space O(n) , set2 takes O(m) ,result=[] takes O(k)
 
#Conclusion:   
#way1 takes most space O(n+m), like for 3 lists i.e (nums1, nums2 & list)
#Way3 takes most time ,but least space only for 1 list i.e (result) 
#way2 is balanced middle ground & takes space for two sets i.e (set1 & result).
#------------------------------------------------------------------------------------------------        
   


