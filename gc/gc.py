import sys

def parse_fasta(filehandler):
    fasta_db = {}
    current_label = ""
    for line in filehandler.read().splitlines():
        if line.startswith(">"):
            current_label = line.lstrip(">")
        else:
            if current_label in fasta_db:
                fasta_db[current_label] += line
            else:
                fasta_db[current_label] = line
    return fasta_db

def get_gc(dna_string):
    gc_count = 0
    for nucleotide in dna_string:
        if nucleotide == "G" or nucleotide == "C":
            gc_count += 1
    return (float(gc_count) / dna_string.__len__()) * float(100)

fasta_file = sys.argv[1]
fasta_db = parse_fasta(open(fasta_file))

highest_label = ""
highest_gc = 0
for fasta_label in fasta_db:
    if get_gc(fasta_db[fasta_label]) > highest_gc:
        highest_label = fasta_label
        highest_gc = get_gc(fasta_db[fasta_label])

print highest_label
print highest_gc
