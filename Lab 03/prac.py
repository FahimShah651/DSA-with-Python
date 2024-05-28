import os
def cls() :
    os.system("cls" if os.name == "nt" else "clear")



class PASSION :
    def intr():
        print("I am The Into Function ",end="")
    

# cleaning all the previous outputs
cls()
#

passionObject = PASSION

PASSION.intr()