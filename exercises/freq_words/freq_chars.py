def freq_words():
    s = input("enter a sentence or words: ")
    d={}
    for i in s:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i]=1
    print(d)
freq_words()

