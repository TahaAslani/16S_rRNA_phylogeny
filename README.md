# 16S_rRNA_phylogeny
Generate phylogenic tree form 16S ribosomal RNA

# Install Requirments

## Muscle
wget https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz
tar xvfz muscle3.8.31_i86linux64.tar.gz -C apps
mv apps/muscle3.8.31_i86linux64 apps/muscle
chmod +x apps/muscle

## PhyML
wget http://www.atgc-montpellier.fr/download/binaries/phyml/PhyML-3.1.zip
unzip PhyML-3.1.zip -d apps
mv apps/PhyML-3.1/PhyML-3.1_linux64 apps/phyml


apps/muscle -in toy.fasta -out msa.fasta
apps/muscle -in msa.fasta -out refined.phylip -refine -phyi

apps/phyml -i refined.phylip -m JC69 -o tlr

python plot.py refined.phylip_phyml_tree.txt refined.phylip results.jpg
