#Ellene Gay S. Daniel
#Sorting and Searching Algorithm



def bubblesort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

def binary_search(arr,val):
    if len(arr) == 0 or (len(arr)==1 and arr[0]!=val):
        print (val, "is NOT a Prime Number!")
        return False

    mid = arr[len(arr)/2]
    if val == mid:
        print (val,"is a Prime Number")
        return True
    if val < mid: return binary_search(arr[:len(arr)/2],val)
    if val > mid: return binary_search(arr[len(arr)/2+1:],val)

if __name__ == "__main__":
    def prime():
        nlist = [2,5,7,11,3,23,17,19,13,37,43,31,29,47,41,53,67,61,59,97,83,73,71,89,83,79]
        bubblesort(nlist)

        print ("You may enter an integer and check if it's prime number or not!")

        x = input("Enter an integer: ")

        print (nlist,)
        return prime()
    prime()
