'''
(Q)How to take multiple integer inputs from user in Python & print it?
Ans: a,b,c,..=map(int, input().split()) , to convert- use [] for list, () for tuple, {} for set, key-value for dictionary

This line is a concise way to take multiple space-separated integer inputs from the user,
& assigned them to the variables a,b,c.Let's understand , How it works step-by-step:-

# input(): This method reads a line of input from the user as a single string.
  Ex- input: 4 5 6 | output: 4 5 6 (as string)
  
# split(): This method splits/breaks the input string into a list of substring.
  Ex- input: 4 5 6  | output:['4','5','6']
  
# map(int...): This function applies the int function to each element in the list returned by split()
  Ex- input: 4 5 6 | output: 4 5 6(as integers)
'''
#------------------
a=input() #input: hi hello , output: hi hello
b=input().split() #input hi hello , output: ['hi], 'hello']
print(a)
print(b)
#------------------
a,b,c =  map(int, input().split())
print(a,b,c) # input: 4 5 6 , output: 4 5 6 

# input: 4 5 6 , output: a = 4 b = 5 c = 6  in all 3 ways to print
print('a =',a,  'b =',b, 'c =',c)  # using commas

print('a = ' +str(a)+ ' b = '+str(b)+ ' c = ' +str(c))   #string concatenation using '+'

print(f"a = {a} b = {b} c = {c} ") # using f-string
#--------------------------------------
#Note: THe best approach to print is f-string, coz it is clear, readable,flexible.