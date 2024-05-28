import os
import ctypes
##############################################################


def tclear():
    # os.system('cls' if os.name == 'nt' else 'clear')
    os.system("cls")


tclear()

############################################################


class Mera_list:
    def __init__(self):
        self.size = 1  # total size of array
        self.n = 0    # Elements in the array
        # make a c type array with the capacity of size
        self.A = self.make_c_arr(self.size)

    def make_c_arr(self, capacity):
        # return c type array with size of capacity
        return (capacity*ctypes.py_object)()
       
    # this will return a number of elements in the array
    def __len__(self):
        return self.n

    def append(self, item):
        if self.n == self.size:
            # Resize
            self.resizing((self.size)*2)
            self.append(item)
        else:
            self.A[self.n] = item
            self.n = self.n + 1
 
    def resizing(self,new_size):
         #  New array of the double size is made
        B = self.make_c_arr(new_size)
        self.size = new_size
        # copy the content of the first array to the new array
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        
    def __str__(self) -> str:
        res = '['
        
        for i in range(self.n):
            res =res + str(self.A[i])
            if i <= (self.n)-2 :
                res = res+","
        res = res+"]"
        return res
    
    #Get indexexing 
    def __getitem__(self,indexex):
        if 0 <= indexex < self.n:
            return self.A[indexex]
        else:
            return "indexex Error -- indexex out of range"
        
    def pop(self,indexex=0):
        indexex = indexex
        if self.n == 0:
            print("Empty List")
        elif indexex == 0:
            self.n = self.n-1  
        
    def clear(self):
        self.n=0
        self.size = 1
        
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        else:
            return "Value Error--Not in list"
        
    def insert(self,item,index):
        if self.n == self.size:
            self.resizing(self.size*2)
            self.insert(item,index)   
        else:
            for i in range(self.n, index, -1):
                self.A[i]=self.A[i-1] 
            self.A[index]=item
            self.n = self.n+1
              
    def __delitem__(self,pos):
        if 0 <= pos <= self.n:
            for i in range(pos,self.n - 1):
                self.A[i]=self.A[i+1]
            
            self.n = self.n - 1
               
        else:
            print("Index not found")
                
    def remove(self,item):
        ind = self.find(item)
        if type(ind) == int:
            self.__delitem__(ind)
        else:
            print(ind)
                
            



l = Mera_list()
#print(l.size)
l.append(2)
#print(l.size)
l.append(23)
#print(l.size)
l.append("world")
l.append(34)
l.append(True)


l.insert("ali",2)

l.insert("lii",4)
print(l)

l.remove(True)
print(l)



