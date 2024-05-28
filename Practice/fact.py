def abc(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n*abc(n-1)
    
print(f"Factorial: {abc(5)}")
    