def callthis(s):
    
        s = list(s)
        l =[]
        l1 = []
        l2 = ['~']
        for j,i in enumerate(s):
            if ord(i)>=3 and ord(i)<126:
                l.append(i.lower())
            else:
                l2.append(i)
                b = bytes(i,'utf-8')
                i = codecs.decode((codecs.encode(b,'hex')),'utf-8')
                i = '+' + str(j) + '?'+i
                #print(i)
                l1.append(i.upper())

        print("".join(l)+"".join(l1)+"".join(l2))
