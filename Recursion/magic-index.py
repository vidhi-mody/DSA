#A magic index in an array A[ 0••• n -1] is defined to be an index such that A[ i] = i. 
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

def findMagicIndex(arr,first,last):
    mid = (first + last)//2
    if(mid == arr[mid]):
        return(mid)
    elif(mid > arr[mid]):
        return(findMagicIndex(arr,mid+1,last))
    else:
        return(findMagicIndex(arr,first,mid))

 
 
# Driver code
arr = [-1, 0, 1, 2, 4, 10]
n = len(arr)
print(findMagicIndex(arr,0,n))