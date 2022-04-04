f2freq =[]
print("This program deals with tones with up to 4th harmonics.")
f2freq = input("Enter two frequencies, separate by space-bar:")
freqcal = f2freq.split()
fa = float(freqcal[0])
fa2 = fa*2
fa3 = fa*3
fa4 = fa*4
fb = float(freqcal[1])
fb2 = fb*2
fb3 = fb*3
fb4 = fb*4
farow = [fa,fa2,fa3,fa4]
fbrow = [fb,fb2,fb3,fb4]
n = int(1)
nqn = []
maxfreq = [0]
a = int(0)
b = int(0)
c = 0
while n < 25:
    if b == 3 and a == 4:
        a = 0
        b = 0
        n += 1
    elif a == 4:
        a = 0
        b += 1
    else:
        pass
    f1a = float(farow[a])/n
    f1b = float(fbrow[b])/(n+1)
    ratio = f1b/f1a
    if ratio > 0.95 and ratio < 1:
        nqn.append(n)
        nqn.append(ratio)
        fundamental = f1a/n
        if fundamental < fa and fundamental > 20:
            maxfreq.append(fundamental)
        else:
            pass
    elif ratio < 1.05 and ratio > 1:
        nqn.append(n)
        nqn.append(ratio)
        fundamental = f1a/n
        if fundamental < fa and fundamental > 20:
            maxfreq.append(fundamental)
        else:
            pass

    elif ratio == 1:
        nqn.append(n)
        nqn.append(1-ratio)
        print("There is a perfect fit:",fb-fa,"Hz")
        break
    else:
        pass
    a += 1
    c += 1


def most_frequent(nqn):
    counter = 0
    num = nqn[0]

    for i in nqn:
        curr_frequency = nqn.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num
if ratio < 1 or ratio > 1:
    print("Highest frequency:",max(maxfreq),"Hz","\nPossible result(s):",sorted(maxfreq,reverse=True),
      "\n",most_frequent(nqn))
    print(nqn)
else:
    pass
closer = most_frequent(nqn)
x = 0
#Fundamental = fa/nqn[p]
#print("Harmonic order as:", nqn[p], ". Difference:", min(nqn)*100, "%", ". Fundamental frequency:",
      #Fundamental,"Hz")
