# 16S_rRNA_phylogeny
Generate phylogenic tree form 16S ribosomal RNA

# Install

## Dependencies

### Conda (skip if you already have conda installed)
Conda can be installed using these instructions:
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

### Environment
Create a conda environment and install packages
```
conda create -n 16S -c conda-forge biopython matplotlib -y
conda activate 16S
```

### Muscle
```
mkdir apps
wget https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz
tar xvfz muscle3.8.31_i86linux64.tar.gz -C apps
mv apps/muscle3.8.31_i86linux64 apps/muscle
chmod +x apps/muscle
rm muscle3.8.31_i86linux64.tar.gz
```

### PhyML
```
wget http://www.atgc-montpellier.fr/download/binaries/phyml/PhyML-3.1.zip
unzip PhyML-3.1.zip -d apps
mv apps/PhyML-3.1/PhyML-3.1_linux64 apps/phyml
rm PhyML-3.1.zip
```

## This Repo
```
wget https://github.com/TahaAslani/16S_rRNA_phylogeny/archive/refs/heads/main.zip
unzip main.zip
cp 16S_rRNA_phylogeny-main/* .
rm -r 16S_rRNA_phylogeny-main
rm main.zip
```

## Data
Download 16S rRNA data from the following link:
https://github.com/yphsieh/16S-ITGDB/tree/master/data

We need Sequence-based ITGDB: ```seq_itgdb_seq.fasta``` (sequence file) and ```seq_itgdb_taxa.txt``` (taxonomy file)


# Run
Run command
```
bash Run.sh seq_itgdb_seq.fasta input_file output_folder
```
The input_file is a comma-separated text file. Each row is an organism and has two columns: The first column is the name of the organism (that you choose) and the second column is the corresponding code in the ```seq_itgdb_taxa.txt```.

Run the pipeline for the test_species.csv species
```
bash Run.sh seq_itgdb_seq.fasta test_species.csv Results
```

For other choice of species, look up their code in ```seq_itgdb_taxa.txt``` and replace them in test_species.
