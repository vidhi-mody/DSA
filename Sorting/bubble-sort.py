def bubbleSort(a,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if(a[i]>a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp


def main():
    n = int(input("Enter length of array: "))
    arr = []

    for i in range(n):
        num = int(input("Enter the element of the array: "))
        arr.append(num)

    print ("\nGiven array is") 
    for i in range(n): 
        print (arr[i]), 

    bubbleSort(arr,n) 

    print ("\n\nSorted array is") 
    for i in range(n): 
        print (arr[i]), 

main()