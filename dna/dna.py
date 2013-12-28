import sys

dna_string = sys.argv[1]

a = 0
t = 0
g = 0
c = 0

for nucleotide in dna_string:
    if nucleotide == "A":
        a += 1
    elif nucleotide == "T":
        t += 1
    elif nucleotide == "G":
        g += 1
    elif nucleotide == "C":
        c += 1

print "%s %s %s %s" % (a, c, g, t)
