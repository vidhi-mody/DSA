def reverse_words_in_a_given_string(string):
    string = string.strip()
    n = len(string)
    words = []
    count = 0
    for i in range(n):
        if string[i]==' ' and string[i+1]!=' ':
            words.append(string[count:i])
            count = i + 1
    words.append(string[count:])
    words = words[::-1]
    return " ".join(x.strip() for x in words)  

answer = reverse_words_in_a_given_string("     geeks    quiz    practice    code")
print(answer)

"""
Output: code practice quiz geeks
"""