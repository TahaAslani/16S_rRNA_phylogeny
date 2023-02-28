DB=$1
Selected=$2
result=$3

echo "Generate phylogenic tree form 16S ribosomal RNA"
echo "credit: Taha Aslani"
echo "https://github.com/TahaAslani/16S_rRNA_phylogeny"

mkdir $result -p

echo "Seperate the DNA sequqnce of the selected organisms..."
python select_organisms.py $DB $Selected $result/selected.fasta

echo "Alsign sequqnces..."
apps/muscle -in $result/selected.fasta -out $result/msa.fasta -quiet
apps/muscle -in $result/msa.fasta -out $result/refined.phylip -refine -phyi -quiet

echo "Build the tree..."
apps/phyml -i $result/refined.phylip -m JC69 -o tlr --quiet

echo "Plot"
python plot.py $result/refined.phylip_phyml_tree.txt $result/results.jpg
