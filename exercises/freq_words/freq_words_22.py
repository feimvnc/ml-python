def freq_words():
    str=input("enter a string: ")
    li=str.split()
    d={}
    for i in li:
        d[i]=d.get(i,0)+1
    print(d)
freq_words()    