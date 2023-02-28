mkdir files
python select_organisms.py seq_itgdb_seq.fasta Selected.txt files/selected.fasta
apps/muscle -in files/selected.fasta -out files/msa.fasta
apps/muscle -in files/msa.fasta -out files/refined.phylip -refine -phyi
apps/phyml -i files/refined.phylip -m JC69 -o tlr
python plot.py files/refined.phylip_phyml_tree.txt results.jpg
