from Bio import SeqIO
import sys

# fasta_file = '/home/taha/phylogenic_tree/seq_itgdb_seq.fasta'
# result_file = '/home/taha/phylogenic_tree/selected.fasta'
# wanted = 'MSBN01003282.16303.18157 AACZ04068991.160832.162580 DQ457645.1.1793 2529960'
# names = 'Human Chimp Panda Watermelon'

fasta_file = sys.argv[1]
result_file = sys.argv[2]
wanted_names = sys.argv[3]

file1 = open(wanted_names, 'r')
Lines = file1.readlines()
file1.close()

wanted = Lines[0].split(' ')
names = Lines[1].split(' ')

name_dict = dict()
for i in range(len(wanted)):
    name_dict[wanted[i]] = names[i]

fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')

with open(result_file, "w") as f:
    for seq in fasta_sequences:
        if seq.id in wanted:
            
            my_name = name_dict[seq.id]
            seq.id = my_name
            seq.description=''
            print(my_name)
            SeqIO.write([seq], f, "fasta")
