def reverse_words_in_a_given_string(string):
    n = len(string)
    words = []
    count = 0
    for i in range(n):
        if string[i]==' ':
            words.append(string[count:i])
            count = i + 1
    words.append(string[count:])
    return(words[::-1])     

answer = reverse_words_in_a_given_string("geeks quiz practice code")
print(answer)