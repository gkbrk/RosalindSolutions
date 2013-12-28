import sys, re

dna_string = sys.argv[1]
dna_motiv = sys.argv[2]

for match in re.finditer("(?=%s)" % dna_motiv, dna_string): #Positive lookahead with regex.
    print match.start() + 1,
