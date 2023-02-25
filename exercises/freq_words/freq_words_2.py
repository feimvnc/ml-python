def frequency_words():
    s=input("enter words: ")
    sp=s.split()
    d={}
    for i in sp:
        if i in d:
            d[i]+=d[i]
        else:
            d[i]=1
    print(d)
frequency_words()
