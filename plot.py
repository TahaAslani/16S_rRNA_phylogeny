from Bio import Phylo
import sys
import matplotlib
import pylab

input_path = sys.argv[1]
output_path = sys.argv[2]


matplotlib.use('Agg')

tree=Phylo.read(input_path,'newick')
Phylo.draw(tree, do_show=False)

pylab.savefig(output_path ,dpi=1500)
pylab.savefig(output_path+'.pdf')

#print("Phylogenetic tree can bee seen in this file", output_path)
