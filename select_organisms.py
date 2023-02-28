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


name_dict = dict()
for line in Lines:
    
    name, code = line.replace('\n', '').split(',')
    name_dict[code] = name
    

fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')

print('Found sequences:')

with open(result_file, "w") as f:
    for seq in fasta_sequences:
        if seq.id in name_dict.keys():
            
            my_name = name_dict[seq.id]
            seq.id = my_name
            seq.description=''
            
            SeqIO.write([seq], f, "fasta")
            
            print(my_name, end=" - ")
