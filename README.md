# metaLAS
Workflow for Metagenomics assembly with Long reads And Short reads to recover prokaryotic metagenomics-assembled genomes. The workflow is developed based on Snakemake.

Detailed information can be found in our [preprint](https://www.biorxiv.org/content/10.1101/2021.05.07.443067v1.full) \
"Salvaging complete and high-quality genomes of novel microbial species from a meromictic lake using a workflow combining long- and short-read sequencing platforms"   


## Installation
1. First, you have to install [Anaconda](https://www.anaconda.com/) or [miniconda3](https://conda.io/en/latest/miniconda.html)
2. Second, you have to install [snakemake](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html) via conda.
3. **[Optional]** [Singularity](https://sylabs.io/guides/3.0/user-guide/installation.html) can be installed so that the workflow can be run with containerized conda packages used in the workflow.





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
