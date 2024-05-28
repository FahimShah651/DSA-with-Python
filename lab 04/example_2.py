
import array
from array import*
new1 = array('i', [4,5,6,7,8,9])
# print the array by traversing
print("Array before insertion")
for a in new1:
 print(a)
#Add new element
new1.append(10)
print("Array after insertion")
for a in new1:
 print(a)
#Remove an element
new1.pop(3)
print("Array after removing")
for a in new1:
 print(a)
#Update an element
new1[3]=11
print("Array after updating")
for a in new1:
 print(a)

