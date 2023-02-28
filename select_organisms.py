from Bio import SeqIO
import sys

# fasta_file = '/home/taha/phylogenic_tree/seq_itgdb_seq.fasta'
# result_file = '/home/taha/phylogenic_tree/selected.fasta'
# wanted_names = '/home/taha/phylogenic_tree/Selected.txt'

fasta_file = sys.argv[1]
wanted_names = sys.argv[2]
result_file = sys.argv[3]


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
