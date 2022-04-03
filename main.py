f2freq =[]
print("This program only deals with sine tones.")
f2freq = input("Enter two frequencies, separate by space-bar:")
freqcal = f2freq.split()
fa = float(freqcal[0])
fb = float(freqcal[1])
n = 1
nqn = []
while n < 24:
    f1a = fa/n
    f1b = fb/(n+1)
    ratio = f1b/f1a
    if ratio > 0.95 and ratio < 1:
        nqn.append(n)
        nqn.append(1-ratio)
    elif ratio < 1.05 and ratio > 1:
        nqn.append(n)
        nqn.append(ratio-1)
    elif ratio == 1:
        nqn.append(n)
        nqn.append(1-ratio)
    else:
        pass
    n += 1
print(nqn)
index = nqn.index(min(nqn))
p = index-1
Fundamental = fa/nqn[p]
print("Harmonic order as:", nqn[p], ". Difference:", min(nqn)*100, "%", ". Fundamental frequency:",
      Fundamental,"Hz")
