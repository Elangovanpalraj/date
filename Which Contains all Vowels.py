# Python Program to Accept the Strings Which Contains all Vowels
# =============================================================\n
'''
Input : geeksforgeeks
Output : Not Accepted
All vowels except 'a','i','u' are not present

Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present
'''
# Using Regular Expressions
# ========================\n
import re
 
sampleInput = "aeioAEiuioea"
 

c = re.compile('[^aeiouAEIOU]')
 

if(len(c.findall(sampleInput))):
    print("Not Accepted")  
else:
    print("Accepted")  
