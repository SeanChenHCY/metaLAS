
#Select bins between orginal bins and reassembled bins based on the value of completeness - 0.5 x contamination

#checkm_output in $1, bin_dir in $2, selection_output_dir in $3, filter_output_dir in $4, file extension in $5 (need".", e.g.: .fa or .fasta)

import sys
import os
import math
checkm_output = sys.argv[1]
polish_dic = sys.argv[2]
selection_output_dir = sys.argv[3]
filter_output_dir = sys.argv[4]
extension = sys.argv[5]



read_table = open(checkm_output,'r').read().split('\n')

reassembly_dic={}
origin_dic={}
pick_list = []
filtered_list = []


read_table_dic={}
for i in read_table[1:]:
    read_table_dic[i.split('\t')[0]]=i


for i in read_table:
    if not i :
        continue 
    if 'Bin Id' in i :
        continue
    entry = i.split('\t')
    if entry[0][-1]=='r':
        reassembly_dic[entry[0]]=[entry[5],entry[6],entry[12]]
    
    if entry[0][-1]=='o':
        origin_dic[entry[0]]=[entry[5],entry[6],entry[12]]



for k,v in origin_dic.items():
    reassembly_ID = k[:-1]+'r'
    if reassembly_ID not in reassembly_dic:
        pick_list.append(k)
        continue
    if float(reassembly_dic[reassembly_ID][0]) < 50 or float(reassembly_dic[reassembly_ID][1]) > 10:
        pick_list.append(k)
        continue
    evaluation_i = float(v[0])-2.5*float(v[1])+math.log10(int(v[2]))
    evaluation_R = float(reassembly_dic[reassembly_ID][0])-2.5*float(reassembly_dic[reassembly_ID][1])+math.log10(int(reassembly_dic[reassembly_ID][2]))
    
    if evaluation_i > evaluation_R :
        pick_list.append(k)
        continue
    elif evaluation_i < evaluation_R:
        pick_list.append(reassembly_ID)
        continue
    elif evaluation_i == evaluation_R:
        if v[2] > reassembly_dic[reassembly_ID][2]:
            pick_list.append(k)
        elif v[2] < reassembly_dic[reassembly_ID][2]:
            pick_list.append(reassembly_ID)
        elif v[2] == reassembly_dic[reassembly_ID][2]:
            pick_list.append(reassembly_ID)


for i in pick_list :
    if i in origin_dic :
        evaluation = float(origin_dic[i][0])-5*float(origin_dic[i][1])
    else :
        evaluation = float(reassembly_dic[i][0])-5*float(reassembly_dic[i][1])
    if evaluation >= 50  :
        filtered_list.append(i)
    


for i in pick_list:
    os.system("echo Select bin "+i)
    os.system("cp "+ polish_dic+"/"+i+extension + " " + selection_output_dir+"/" + i+extension)



for i in filtered_list:
    os.system("echo bin "+i + " meet GTDB criteria")
    os.system("cp "+ polish_dic+"/"+i+extension + " " + filter_output_dir+"/" + i+extension)
    



with open(filter_output_dir+'/filtered_summary.tsv','w') as filtered_summary:
    filtered_summary.write(read_table[0]+'\n')
    for i in filtered_list:
        filtered_summary.write(read_table_dic[i]+'\n')

    
with open(selection_output_dir+'/selected_summary.tsv','w') as selected_summary:
    selected_summary.write(read_table[0]+'\n')
    for i in pick_list:
        selected_summary.write(read_table_dic[i]+'\n')
 
