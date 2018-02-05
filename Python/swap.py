def swap(str):
    s = list(str)
    for i in range(0,len(s),2):
        t=s[i]
        s[i]=s[i+1]
        s[i+1]=t
    

    return "".join(swap(s))
