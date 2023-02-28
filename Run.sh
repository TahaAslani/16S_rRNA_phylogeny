DB=$1
Selected=$2
result=$3

echo "GENERATE PHYLOGENIC TREE FORM 16S RIBOSOMAL RNA"
echo ""
echo "credit: Taha Aslani"
echo "https://github.com/TahaAslani/16S_rRNA_phylogeny"
echo ""

mkdir $result -p

echo ""
echo "Seperate the DNA sequqnce of the selected organisms..."
python select_organisms.py $DB $Selected $result/selected.fasta
echo -ne "Done!"

echo ""
echo "Allign sequqnces using Muscle..."

echo "Step 1..."
apps/muscle -in $result/selected.fasta -out $result/msa.fasta -quiet

echo "Step 2..."
apps/muscle -in $result/msa.fasta -out $result/refined.phylip -refine -phyi -quiet

echo -ne "Done!"

echo ""
echo "Build the tree using PhyML ..."
apps/phyml -i $result/refined.phylip -m JC69 -o tlr --quiet
echo -ne "Done!"

echo "Plot..."
python plot.py $result/refined.phylip_phyml_tree.txt $result/results.jpg
echo -ne "Done!"
