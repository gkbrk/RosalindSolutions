import sys

def get_hamming_distance(string1, string2):
    hamming_distance = 0
    for nucleotide_no in range(string1.__len__()):
        if string1[nucleotide_no] != string2[nucleotide_no]:
            hamming_distance += 1
    return hamming_distance

dna_string_1 = sys.argv[1]
dna_string_2 = sys.argv[2]

hamming_distance = get_hamming_distance(dna_string_1, dna_string_2)
print hamming_distance
