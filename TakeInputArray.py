'''
#Take Array Input-
1.Using split() for space-separated input
2.Using split() for comma-separated input
3.Taking input for a fixed-size array
4.Using NumPy for numerical operations

import numpy as np
np.array(list(map(int, input().split())))
'''
n1 = int(input("  Enter a number:   ").strip(" "))
print(n1)
#lst=input().split()  # 2 3 5
#lst= map(str, input().split())
lst= list(map(str, input().split()))
#lst= list(map(int, input().split()))
#lst= "".join(map(str, input().split()))
print(lst)


'''
#int_input1= list(map(int,input().split()))
str_input = ",".join(map(str, input().split()))
print(str_input)
'''
'''
_________________________________________
1).arr=list(map(int,input().split()))
4
1 3 5 6
[1, 3, 5, 6]
_________________________________________________
2). [1 3 5 6]    
# for this - use
 arr = " ".join(map(str, input().split()))
 print("["+arr+"]")
________________________________________________
3).arr = " ".join(map(str, input().split()))
4
1 3 5 6
1 3 5 6
________________________________________
4).arr=list(map(int,input().split())) 
print(*arr) # 1 3 5 6

______________________________________________
5).arr = ",".join(map(str, input().split()))
4
1 3 5 6
1,3,5,6
___________________________________________
'''
'''
1).input().split() - reads user input as a single string.
Reads a line of input (always in string format) from a user & converts/splits it into list of sub-string (words) based on white space by default.

2).map(int,...) - converts each string in the list to an integer.  
  or apply int() function to each element(which is always in string format element).
  list(map(int, input().split()))

3).map(str,...) - converts each element string or apply str() function to each element(that is always in string format).
               "".join(map(int, input().split()))
list(...) - collects integers into a list
"".join(map(str, input().split())) - joins  elements/strings of the list into a single string without spaces.
*varName - unpacks the list, so that each element is printed with a space in between.

'''






