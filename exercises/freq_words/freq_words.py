def freq_words():
    str=input("enter a string: ")
    li=str.split()   # convert str to words
    d={}  # create an empty map 

    for i in li: 
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)

freq_words()
