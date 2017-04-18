#Tiffany Gassmann
#BIMM 185
#Week 2 Assignment 2

import sys, gzip, textwrap

from collections import defaultdict

def main():
    table = readfile_table()
    genome = readfile_fasta()

    #out = assemble(table,genome)

    #with open('genome_out.txt', 'w') as file:
    #    for item in out:
    #        print >> file, item

    #out2 = codon_usage_file(table,genome)

    #with open('condon_out.txt', 'w') as file:
    #    for item in out2:
    #        print  >> file, item

def readfile_fasta():
    #open and read file
    file = gzip.open("ecoli_genome.fna.gz")
    contents = file.readlines()

    #removes /n char
    for i in xrange(len(contents)):
        contents[i] = contents[i].strip()
    #returns only sequence
    return "".join(contents[1:])

def readfile_table():
    file = open("table.txt")
    table = file.readlines()


    for i in xrange(len(table)):
        #making table into list of lists without tab
        table[i] = table[i].strip().split("\t")

    return table[1:]


#Reverse Compliment Handle
def reverse_comp(text):
    #dictionary of complements
    complement_dict = {'A':'T', 'T':'A', 'C':'G', 'G': 'C'}
    #reverse text
    reverse = text[::-1]
    complement = ""
    #for each nucleotide
    for x in reverse:
        complement = complement + complement_dict[x]

    return complement
    
#arrannge output of file
def assemble(table, genome):
    res = []
    #constant columns in table index
    START = 2
    END = 3
    DIR = 4
    LOCUS = 6
    TAG = 7
    PROTEIN = 8

    #header + squence cut
    for row in table:
        name = row[PROTEIN]
        locus = row[LOCUS]
        tag = row[TAG]

        header = name + '|' + locus + '|' + tag + '\n'

        #cut index for the genome sequence
        cut = genome[int(row[START])-1:int(row[END])]

        #reverse compliment handling
        if row[DIR] == '-':
            cut = reverse_comp(cut)

        #sequence for each locus
        seq = '\n'.join(textwrap.wrap(cut, 70, break_long_words=True)) + '\n'

        res.append(header + seq)

    return res

def codon_usage_file(table, genome):
    #global column var
    LOCUS = 7
    START = 2
    END = 3
    DIR = 4
    res = []

    #get the name
    for row in table:
        locus = row[LOCUS]
        #formatting

        header = locus + '\t'

        #sequence cut index
        cut = genome[int(row[START]) - 1:int(row[END])]

        #revrse compliment if '-' direction
        if row[DIR] == '-':
            cut = reverse_comp(cut)


        res.append(header + cut)

    return res



if __name__ == '__main__':
    main()
