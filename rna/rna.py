import sys

dna_string = sys.argv[1]
rna_string = ""

for nucleotide in dna_string:
    if nucleotide == "T":
        rna_string += "U"
    else:
        rna_string += nucleotide

print rna_string
