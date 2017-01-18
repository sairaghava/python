def count_letter(string):
    words = string.split()
    print(words)
    print(len(words))
    count = 0
    for i in range(len(string)):
        if string[i].isalpha():
            count += 1
    return count

print("the no of characters in the word is:")
print(count_letter('The grey old fox is an idiot.'))