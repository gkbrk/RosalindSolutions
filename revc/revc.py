import sys

def complement(dna_string):
    complemented_string = ""
    for nucleotide in dna_string:
        if nucleotide == "A":
            complemented_string += "T"
        elif nucleotide == "T":
            complemented_string += "A"
        elif nucleotide == "G":
            complemented_string += "C"
        elif nucleotide == "C":
            complemented_string += "G"
    return complemented_string

dna_string = sys.argv[1]
complemented_dna = complement(dna_string)
reverse_complement = complemented_dna[::-1]
print reverse_complement
