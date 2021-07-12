#sys.argv[1] = bin_dir, sys.argv[2] = flye_info, sys.argv[3] = output_dir, sys.argv[3] = output_dir

import os, sys

bin_dir = sys.argv[1]
flye_info_file = sys.argv[2]
output_dir = sys.argv[3]



large_circular = []
flye_info = open(flye_info_file,'r')
read_info = True
while read_info:
    read_info = flye_info.readline()
    entry = read_info.split('\t')
    if len(entry) > 3:
        if (entry[3] == "Y") and (int(entry[1]) > 2000000):
            large_circular.append(entry[0])



bin_name=""
contig_bins={}
for bin_file in os.listdir(bin_dir):
	if bin_file.endswith("_o.fasta") or bin_file.endswith("_o.fa"): 
		bin_name=".".join(bin_file.split("/")[-1].split(".")[:-1])
		write_output_bool = False
		write_output = ''
		for line in open(bin_dir+"/"+bin_file):
			if line[0] == ">":
				if write_output_bool:
					write_output.close()
				write_output_bool = False
				if line[1:-1] in large_circular:
					write_output_bool = True
					write_output = open(output_dir+"/"+line[1:-1]+'_in_'+bin_name+'.fasta','w')
					large_circular.remove(line[1:-1])
			if write_output_bool :
				write_output.write(line)



                    


