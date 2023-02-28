DB=$1
Selected=$2
result=$3

mkdir $result -p

# Seperate the wanted species
python select_organisms.py $DB $Selected $result/selected.fasta

# Alsign sequqnces
apps/muscle -in $result/selected.fasta -out $result/msa.fasta -quiet
apps/muscle -in $result/msa.fasta -out $result/refined.phylip -refine -phyi -quiet

# Build the tree
apps/phyml -i $result/refined.phylip -m JC69 -o tlr

# Plot
python plot.py $result/refined.phylip_phyml_tree.txt $result/results.jpg
