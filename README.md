# 16S_rRNA_phylogeny
Generate phylogenic tree form 16S ribosomal RNA

# Install Requirments

## Muscle
```
mkdir apps
wget https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz
tar xvfz muscle3.8.31_i86linux64.tar.gz -C apps
mv apps/muscle3.8.31_i86linux64 apps/muscle
chmod +x apps/muscle
```

## PhyML
```
wget http://www.atgc-montpellier.fr/download/binaries/phyml/PhyML-3.1.zip
unzip PhyML-3.1.zip -d apps
mv apps/PhyML-3.1/PhyML-3.1_linux64 apps/phyml
```

# Download Data
Download 16S rRNA data from the following link:
https://github.com/yphsieh/16S-ITGDB/tree/master/data

We need Sequence-based ITGDB: ```seq_itgdb_seq.fasta``` (sequence file) and ```seq_itgdb_taxa.txt``` (taxonomy file)



# Run
## Select Organisms of interest
```
MSBN01003282.16303.18157, AACZ04068991.160832.162580, DQ457645.1.1793, 2529960
Human, Chimp, Panda, Watermelon
```

# Run the pipeline
```
mkdir files
apps/muscle -in selected.fasta -out files/msa.fasta
apps/muscle -in files/msa.fasta -out files/refined.phylip -refine -phyi
apps/phyml -i files/refined.phylip -m JC69 -o tlr
python plot.py files/refined.phylip_phyml_tree.txt files/refined.phylip results.jpg
```
