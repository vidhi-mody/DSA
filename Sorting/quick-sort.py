
def partition(arr, low, high): 
    i = (low-1) 
    pivot = arr[high]
  
    for j in range(low, high): 
  
        if arr[j] <= pivot: 

            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
  
def quickSort(arr, low, high): 
    if len(arr) == 1: 
        return arr 

    if low < high: 
  
        p = partition(arr, low, high) 
  
        quickSort(arr, low, p-1) 
        quickSort(arr, p+1, high) 

def main():
    n = int(input("Enter length of array: "))
    arr = []

    for i in range(n):
        num = int(input("Enter the element of the array: "))
        arr.append(num)

    print ("\n\nGiven array is") 
    for i in range(n): 
        print (arr[i]),

    quickSort(arr, 0, n-1) 

    print ("\n\nSorted array is") 
    for i in range(n): 
        print (arr[i]),

main()