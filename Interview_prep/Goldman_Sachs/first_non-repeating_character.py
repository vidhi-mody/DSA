from collections import OrderedDict

def firstNonRepeating(string):
    od = OrderedDict()
    n = len(string)
    for i in range(n):
        if(string[i] in od):
            od[string[i]] += 1
        else:
            od[string[i]] = 1
    for key, value in od.items():
        if(value==1):
            return key
    return("Not found!")

string = "hello"
answer = firstNonRepeating(string) 
print(answer)