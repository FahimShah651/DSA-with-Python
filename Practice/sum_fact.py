def sum_fact(A):
    if (len(A)-1) < 0:
        return 0
    else:
        return sum_fact(A[:-1]) + A[0]

A = [1, 1, 1, 1, 1, 1, 1]
print("summmm", sum_fact(A))


def reversing(A):
    if len(A) <= 1: 
        return A 
    else:
        B = reversing(A[1:]) 
   
        B.append(A[0]) 

        return B 
     
A = [1,2,3,4,5,6,7]
print("Reversed : ",reversing(A))



def power(a,n):
    if n==0:
        return 1
    else:
        return a*power(a,n-1)
    
print(" 3 to the power of 5 : ",power(3,5))