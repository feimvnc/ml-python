def freq_words():
    l=[i.strip(".").strip(".") for i in input("enter a string: ").split()]
    for w in set(l): print(f"'{w}' : {l.count(w)}", end="," )
freq_words()
