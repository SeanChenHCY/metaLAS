#iterative pilon

#genome in $1, forward reads in $2, reverse reads in $3, cpus in $4, final output in $5

import sys
import os
orignal_bin = sys.argv[1]
forward_reads = sys.argv[2]
reverse_reads = sys.argv[3]
cpus = sys.argv[4]
final_outfile = sys.argv[5]

if not os.path.isfile(orignal_bin):
	print ('bin not found')
	sys.exit()
if not os.path.isfile(forward_reads):
	print ('R1 not found')
	sys.exit()
if not os.path.isfile(reverse_reads):
	print ('R2 not found')
	sys.exit()


def mean_coverage(sam_coverage_file):
	openfile = open(sam_coverage_file,'r')
	covered_base = 0
	total_base = 0
	total_depth = 0
	for line in openfile:
		if 'startpos' in line:
			continue
		if line:
			entry = line.split('\t')
			total_base += int(entry[2])
			covered_base += int(entry[4])
			total_depth += float(entry[6])*int(entry[4])
	openfile.close()
	mean_depth = round(total_depth/total_base,2)
	return (mean_depth)


polish_time = 0
for i in range(5): 
	if i == 0:
		genome=orignal_bin
		os.system("echo Start working on "+genome)
		os.system("bwa index "+genome)
		os.system('bwa mem -t '+ cpus +' '+genome + ' '+ forward_reads + ' ' + reverse_reads + ' | samtools view -@ '+cpus+' -bS - | samtools sort -m 8g -@ '+cpus+' -o '+genome+'.bam -')
		os.system('samtools coverage ' +genome+ '.bam -o '+genome+'.coverage')
		coverage = mean_coverage(genome+'.coverage')
		if coverage > 150:
			used_fraction = 150/coverage
			os.system("echo Sampling on "+genome)
			os.system('samtools view -@ '+cpus+' -b -s ' + str(used_fraction) + ' ' +genome+ '.bam | samtools sort -@ '+cpus+' -o '+genome+'_sub.bam -')
			os.system('samtools index '+genome+'_sub.bam')
			os.system('pilon -Xms4g -Xmx16g --genome '+genome+' --frags '+genome+'_sub.bam --output '+orignal_bin+".pilon"+str(i)+' --threads '+cpus+' --changes')
			os.system("sed -i 's/_pilon//g' " + orignal_bin+".pilon"+str(i)+".fasta")
			os.remove(genome+'.amb')
			os.remove(genome+'.ann')
			os.remove(genome+'.bwt')
			os.remove(genome+'.pac')
			os.remove(genome+'.bam')
			os.remove(genome+'_sub.bam.bai')
			os.remove(genome+'_sub.bam')
			os.remove(genome+'.sa')
			if os.stat(orignal_bin+".pilon"+str(i)+'.changes').st_size == 0 :
				print('Finshed')
				polish_time = i
				break
		else : 
			os.system('samtools index '+genome+'.bam')
			os.system("echo Working on "+genome)
			os.system('pilon -Xms4g -Xmx16g --genome '+genome+' --frags '+genome+'.bam --output '+orignal_bin+".pilon"+str(i)+' --threads '+cpus+' --changes')
			os.system("sed -i 's/_pilon//g' " + orignal_bin+".pilon"+str(i)+".fasta")
			os.remove(genome+'.amb')
			os.remove(genome+'.ann')
			os.remove(genome+'.bwt')
			os.remove(genome+'.pac')
			os.remove(genome+'.bam')
			os.remove(genome+'.bam.bai')
			os.remove(genome+'.sa')
			if os.stat(orignal_bin+".pilon"+str(i)+'.changes').st_size == 0 :
				print('Finshed')
				break


	elif i > 0:
		x=i-1
		genome=orignal_bin+".pilon"+str(x)+".fasta"
		os.system("echo Working on "+genome)
		os.system("bwa index "+genome)
		if coverage > 150:
			os.system("echo sampling "+genome)
			os.system('bwa mem -t '+ cpus +' '+genome + ' '+ forward_reads + ' ' + reverse_reads + ' | samtools view -@ '+cpus+' -bS -s '+ str(i+used_fraction) + ' - | samtools sort -@ '+cpus+' -o '+genome+'.bam -')

		else :
			os.system('bwa mem -t '+ cpus +' '+genome + ' '+ forward_reads + ' ' + reverse_reads + ' | samtools view -@ '+cpus+' -bS - | samtools sort -@ '+cpus+' -o '+genome+'.bam -')

		os.system('samtools index '+genome+'.bam')
		#now run pilon
		os.system(' pilon -Xms4g -Xmx16g --genome '+genome+' --frags '+genome+'.bam --output '+orignal_bin+".pilon"+str(i)+' --threads '+cpus+' --changes')
		os.system("sed -i 's/_pilon//g' " + orignal_bin+".pilon"+str(i)+".fasta")
		os.remove(genome+'.amb')
		os.remove(genome+'.ann')
		os.remove(genome+'.bwt')
		os.remove(genome+'.pac')
		os.remove(genome)
		os.remove(genome+'.bam')
		os.remove(genome+'.bam.bai')
		os.remove(genome+'.sa')
		if os.stat(orignal_bin+".pilon"+str(i)+'.changes').st_size == 0 :
			print('Finshed')
			polish_time = i
			break
	polish_time = i

os.system("cp " + orignal_bin+".pilon"+str(polish_time)+".fasta  " + final_outfile)

