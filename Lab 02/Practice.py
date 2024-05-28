"""
n = int(input("Enter The Number : "))
start =[0,1]
fabonacci =1
for i in range(0,n):
    print("   ",fabonacci)
    fabonacci = start[len(start)-2]+start[len(start)-1]
    start.append(fabonacci)
    if fabonacci > n:
        break
        
    """
    
# n = int(input("Enter The Number : "))
# num1 =0
# num2 =1
# fabonacci =1
# for i in range(0,n):
#     print("   ",fabonacci)
#     fabonacci = num1 + num2
#     num1 = num2
#     num2 = fabonacci
#     if fabonacci > n:
#         break1