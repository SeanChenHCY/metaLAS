#usage: 
# ./nanopore_reads_extract.py original_bin_folder output_dir sam_file
import sys, os

# load bin contigs
print ("loading contig to bin mappings...")
contig_bins={}
for bin_file in os.listdir(sys.argv[1]):
	if bin_file.endswith(".fa") or bin_file.endswith(".fasta"): 
		bin_name=".".join(bin_file.split("/")[-1].split(".")[:-1])
		for line in open(sys.argv[1]+"/"+bin_file):
			if line[0]!=">": continue
			contig_bins[line[1:-1]]=bin_name

# store the read names and what bins they belong in in these dictionaries
# strict stores only perfectly aligning reads and permissive stores any aligned reads

print ("Parsing sam file and writing reads to appropriate files depending what bin they alligned to...")
files={}
opened_bins={}
samfile = open(sys.argv[3],'r')
read_sam= samfile.readline()
while read_sam :
	line = read_sam 
	read_sam= samfile.readline()
	if line[0]=="@": continue
	F_line = line 
	F_cut = F_line.strip().split("\t")


	# skip non aligned reads
	if F_cut[2]=="*" : continue
	
	contig=F_cut[2]
	if contig not in contig_bins: continue
	bin_name = contig_bins[contig]


	# open the revelant output files
	if bin_name not in opened_bins:
		opened_bins[bin_name]=None
		files[sys.argv[2]+"/"+bin_name+".nanopore.txt"]=open(sys.argv[2]+"/"+bin_name+".nanopore.txt", "w")



	# write
	files[sys.argv[2]+"/"+bin_name+".nanopore.txt"].write(F_cut[0] +"\n")


print("closing files") 
for f in files:
	files[f].close()


print ("Finished splitting reads!")
