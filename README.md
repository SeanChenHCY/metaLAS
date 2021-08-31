# metaLAS
Workflow for Metagenomics assembly with Long reads And Short reads to recover prokaryotic metagenomics-assembled genomes. The workflow is developed based on Snakemake.

Detailed information can be found in our [Publication](https://www.nature.com/articles/s42003-021-02510-6) or [preprint](https://www.biorxiv.org/content/10.1101/2021.05.07.443067v1.full) \
"Salvaging complete and high-quality genomes of novel microbial species from a meromictic lake using a workflow combining long- and short-read sequencing platforms"   
\
![alt text](https://github.com/SeanChenHCY/metaLAS/blob/main/scheme.png)
\

## Installation
1. First, you have to install [Anaconda](https://www.anaconda.com/) or [miniconda3](https://conda.io/en/latest/miniconda.html)
2. Second, you have to install [snakemake](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html) and mamba via conda.
3. Change the working directory to the directory you want to put workflow and then pull the repository using git:
```
cd {where you want to put the workflow}
git clone https://github.com/SeanChenHCY/metaLAS.git
```
4. **[Optional]** [Singularity](https://sylabs.io/guides/3.0/user-guide/installation.html) can be installed so that the workflow can be run with containerized conda packages used in the workflow. 

5. Download [CheckM](https://github.com/Ecogenomics/CheckM/wiki/Installation#how-to-install-checkm) database if you do not have (Remember to extract it). Skip this step if you want to run with Singularity because CheckM database has been wrapped into the images.


## Usage
1. First, you have to change parameters in configfile. You have to specify the locations of reads files and checkm database. (If you want to run with singularity, you don't have to download and set checkm database)
2. Activcate snakemake conda environment
```
conda activate snakemake
```
3. Run the workflow with snakemake. You have to specify the location of metaLAS after -s and config file after --configfile. Also you can allocate thread number to this workflow.
```
snakemake -s {/path/to/metaLAS} --configfile {path/to/config.yaml} --use-conda --cores {threads}
```

4. Alternatively, you can run with singularity so no conda package downloads are necessary.
If you want to do this way, please add two arugments : --use-singularity --singularity-args '--bind /yourrootdirectories/ ' as below
```
snakemake -s {/path/to/metaLAS} --configfile {path/to/config.yaml}  --use-singularity \
--singularity-args '--bind /yourrootdirectories/ --use-conda --cores {threads}
```

## Output 
```
Output/   #you can specify directory of output in config file
├── 1.megahit_result
├── 2.metaflye_result
├── 3.polished_metaflye
├── 4.quickmerge
├── 5.binning
├── 6.bin_refinement
├── 7.read_retrieval
├── 8.reassembly
├── 9.final_polish
├── 10.selected_bin
├── 11.filtered_bin
└── 12.circular_contig

```

## Used tools & References
If you the workflow, please includes the following references into your manuscript

* **Megahit**
  * Li D, Liu CM, Luo R, Sadakane K, Lam TW: MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph. Bioinformatics      2015, 31(10):1674-1676.

* **Flye & metaFlye**
  * Kolmogorov M, Bickhart DM, Behsaz B, Gurevich A, Rayko M, Shin SB, Kuhn K, Yuan J, Polevikov E, Smith TPL et al: metaFlye: scalable long-read metagenome assembly using repeat graphs. Nat Methods 2020, 17(11):1103-1110.
  * Kolmogorov M, Yuan J, Lin Y, Pevzner PA: Assembly of long, error-prone reads using repeat graphs. Nature Biotechnology 2019, 37(5):540-+.

* **quickmerge**
  * Chakraborty M, Baldwin-Brown JG, Long AD, Emerson JJ: Contiguous and accurate de novo assembly of metazoan genomes with modest long read coverage. Nucleic Acids Res 2016, 44(19):e147.

* **Pilon**
  * Walker BJ, Abeel T, Shea T, Priest M, Abouelliel A, Sakthikumar S, Cuomo CA, Zeng Q, Wortman J, Young SK et al: Pilon: an integrated tool for comprehensive microbial variant detection and genome assembly improvement. PLoS One 2014, 9(11):e112963.

* **BWA-MEM**
  * Li H, Durbin R: Fast and accurate short read alignment with Burrows-Wheeler transform. Bioinformatics 2009, 25(14):1754-1760.

* **MetaWRAP**
  * Uritskiy GV, DiRuggiero J, Taylor J: MetaWRAP-a flexible pipeline for genome-resolved metagenomic data analysis. Microbiome 2018, 6(1):158.

* **Unicycler**
  * Wick RR, Judd LM, Gorrie CL, Holt KE: Unicycler: Resolving bacterial genome assemblies from short and long sequencing reads. PLoS Comput Biol 2017, 13(6):e1005595.

* **CheckM**
  * Parks DH, Imelfort M, Skennerton CT, Hugenholtz P, Tyson GW: CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes. Genome Res 2015, 25(7):1043-1055. 

## Contact 
Please contact Yu-Hsiang Chen (s871818@gmail.com or GitHub Issues) for any questions, concerns, or feedbacks.
