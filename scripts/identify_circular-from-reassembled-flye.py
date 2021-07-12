#sys.argv[1] = bin_dir, sys.argv[2] = flye_info, sys.argv[3] = output_dir, sys.argv[3] = output_dir

import os, sys

bin_name=sys.argv[1]
bin_dir = sys.argv[2]
output_dir = sys.argv[3]



large_circular = []
flye_info = open(bin_dir + '/assembly_info.txt','r')
read_info = True
while read_info:
	read_info = flye_info.readline()
	entry = read_info.split('\t')
	if len(entry) > 3:
		if (entry[3] == "Y") and (int(entry[1]) > 2000000):
			large_circular.append(entry[0])


for i in large_circular:
	os.system('seqkit grep -n -p '+ i + ' '  + bin_dir + '/assembly.fasta -o ' +output_dir + '/' +  bin_name + '_'+ i + '_unpolished_rf.fasta' )


