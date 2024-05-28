def merge_sort(s):
    n = len(s)
    if n < 2:
        return 
    mid =  n//2
    s1 = s[0:mid]
    s2 = s[mid:n]
    print(f"{type(s1)}    {s1}  :: {type(s2)}   {s2}")
    merge_sort(s1)
    print("2nd sort rec")
    merge_sort(s2)
    
    merge(s1,s2,s)
    
def merge(s1,s2,s):
    if s1[0] > s2[0] :
        s[0]= s2[0]
        s[1]= s1[0]
        
        
arr = [5,2,9,7]
merge_sort(arr)
print(arr)