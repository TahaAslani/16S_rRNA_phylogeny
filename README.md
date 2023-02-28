# 16S_rRNA_phylogeny
Generate phylogenic tree form 16S ribosomal RNA

# Install

## Muscle
```
mkdir apps
wget https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz
tar xvfz muscle3.8.31_i86linux64.tar.gz -C apps
mv apps/muscle3.8.31_i86linux64 apps/muscle
chmod +x apps/muscle
rm muscle3.8.31_i86linux64.tar.gz
```

## PhyML
```
wget http://www.atgc-montpellier.fr/download/binaries/phyml/PhyML-3.1.zip
unzip PhyML-3.1.zip -d apps
mv apps/PhyML-3.1/PhyML-3.1_linux64 apps/phyml
rm PhyML-3.1.zip
```

## Download Data
Download 16S rRNA data from the following link:
https://github.com/yphsieh/16S-ITGDB/tree/master/data

We need Sequence-based ITGDB: ```seq_itgdb_seq.fasta``` (sequence file) and ```seq_itgdb_taxa.txt``` (taxonomy file)

## Download This Repo
```
wget https://github.com/TahaAslani/16S_rRNA_phylogeny/archive/refs/heads/main.zip
unzip main.zip
cp 16S_rRNA_phylogeny-main/* .
rm -r 16S_rRNA_phylogeny-main
```

# Run

## Select Organisms of interest
```
echo "MSBN01003282.16303.18157 AACZ04068991.160832.162580 DQ457645.1.1793 2529960\nHuman Chimp Panda">Test.txt
echo "Human Chimp Panda">Test.txt

```

## Run the pipeline
```
bash Run.sh seq_itgdb_seq.fasta Test.txt Results
```
