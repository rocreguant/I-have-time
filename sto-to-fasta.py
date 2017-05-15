import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

if(len(sys.argv) <3):
    print('two arguments needed: input path, output path')
    exit(2)


with open(sys.argv[1],'r') as inFile:
    with open(sys.argv[2], "w") as output_handle:
        SeqIO.write(list(SeqIO.parse(inFile,'stockholm')), output_handle, "fasta")

