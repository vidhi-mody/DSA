def sortArrayInWaveForm(array):
    greater = 1
    for i in range(len(array)-1):
        if(greater == 1):
            if(array[i]<array[i+1]):
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
            greater = 0
        else:
            if(array[i]>array[i+1]):
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
            greater = 1
    return array

array = [20, 10, 8, 6, 4, 2]
answer = sortArrayInWaveForm(array) 
print(answer)

