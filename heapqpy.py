
#code for finding the nlargest /nsmallest element in list
#using heapq
import heapq

elm=[4,7,9,54,8,599,77,43,321,77,9]

print("Largest element::")
print(heapq.nlargest(3,elm))
print("smallest element::")
print(heapq.nsmallest(3,elm))