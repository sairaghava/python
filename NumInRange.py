#num1 = input("enter the low num: \n")
#num2 = input("enter the high num: \n")
#num3 = input("enter any num:\n")
def numInRange(num3):
    if num3 in range(10,21):
        print("the given no %d is in the given range" %(num3))
    else:
        print("the given no %d is not in the given range"%(num3))
numInRange(20)

