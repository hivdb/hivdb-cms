**HIVdb-NGS** (beta) accepts user-submitted protease, RT, and/or integrase codon frequency tables (CodFreq Files) or AAVF files generated by the HYDRA pipeline. Results are returned at 8 mutation detection thresholds. At each threshold the program quantifies the number of unusual mutations and the number of signature APOBEC mutations. Thresholds with large numbers of unusual or signature APOBEC mutations are likely too low and pose unacceptable risks of identifying artifactual mutations caused either by machine error, PCR error, or G-to-A hypermutation.

By default, genotypic resistance interpretations are returned for the 20% threshold. A drop-down menu allows users to view results at lower thresholds. A multi-threshold mutation summary table is provided to help users identify thresholds to reduce the risk of identifying artifactual mutations. Genotypic resistance interpretations are suppressed at thresholds for which &gt;1% of positions have an unusual mutation. The appropriate mutation detection threshold, however, cannot be identified with certainty in the absence of a sequencing protocol that uses unique molecular identifiers (UMIs) for each virus template.

Mutations detected at low thresholds are difficult to interpret because they are at increased risk of being artifactual and because few data have linked such mutations with an increased risk of virological failure to contemporary ART regimens. Nonetheless, the genotypic resistance interpretation of HIVdb-NGS beta version currently does not consider the threshold at which a mutation is detected. Like the main HIVdb program, the purpose of HIVdb-NGS beta is educational with regard to its genotypic resistance interpretations and quality control analysis. The Release Notes for the main HIVdb program can be found [here](/page/release-notes/).

## Program input

### Codon frequency table

HIVdb-NGS (beta) accepts user-submitted protease, RT, and/or integrase codon frequency tables (CodFreq Files). CodFreq Files are tab- or comma-delimited text files containing the following 5 columns:

1. Gene (PR, RT, or IN);
2. Amino acid position;
3. Number of reads for the position (coverage);
4. Sequenced codon;
5. Number of reads containing the codon.

Below are three example CodFreq files, which can be viewed in your browser by clicking on them. These files can also be downloaded and viewed in Microsoft Excel. These same three files can be uploaded to HIVdb-NGS (beta) by clicking on the [Load Example Data](/hivdb/by-reads/) link on the Input sequence reads form.

- [SRR4071760]($$CMS_PREFIX$$downloads/codfreq-examples/SRR4071760.codfreq.txt)
- [SRX3881674]($$CMS_PREFIX$$downloads/codfreq-examples/SRX3881674.codfreq.txt)
- [DRR030302]($$CMS_PREFIX$$downloads/codfreq-examples/DRR030302.codfreq.txt)

These example files were generated from FASTQ files in the [NCBI Sequence Read Archive (SRA)](https://www.ncbi.nlm.nih.gov/sra). We have also created a library of FASTQ and CodFreq files from the NCBI (SRA) which are available [here](http://ngs-meta-fastq.hivdb.org/). The steps required to convert a FASTQ file or SAM file to a CodFreq file can be found [here](/page/codfreq/).

#### Amino Acid Variant Format (AAVF)

HIVdb-NGS (beta) also accepts another file format called the AAVF which was developed by the [Winnipeg Consensus](https://doi.org/10.1002/jia2.25193). Files in this format are produced by several third party NGS pipelines, such as [HyDRA](https://hydra.canada.ca/pages/home) and [PASeq](https://paseq.org/). More information about this format can be found [here](https://github.com/winhiv/aavf-spec).



## Program output

### Sequence reads summary

This section describes the regions of HIV-1 PR, RT, and/or IN encompassed in the uploaded CodFreq file. The Read Depth describes the median number of reads encompassing each position (read coverage). The subtype is assessed using the consensus of all reads at the 20% mutation detection threshold. The methods of subtyping is similar to that used by the main HIVdb program and is described [here](https://hivdb.stanford.edu/page/hiv-subtyper/).

The Minimal Read Depth drop down menu allows users to instruct the program to ignore positions with reads below the specified depth. It will also prompt the program to return a warning reporting the number of codons containing reads below the specified depth. If the drop down menu is not used, the minimal read depth used by the program will be 1,000.

The Mutation Detection Threshold allows the user to specify the proportion of reads that must contain an amino acid for it to appear on the report. By default, this is set to 20%.

The Read Coverage button at the upper-right displays a figure which illustrates the read coverage across the pol regions encompassed by the CodFreq file.

Clicking on the SDRM button results in the addition of rows to the Sequence Read Summary listing the surveillance DRMs for each gene included in the CFT. The complete list of PR, RT, and IN SDRMs and can be found on these pages: [PR/RT](/page/who-sdrm-list/), [IN](/page/insti-sdrm-list/).

### Multi-threshold mutation summary table

This section contains a table with the following columns:

1. Mutation detection threshold: 20%, 10%, 5%, 2%, 1%, 0.5%, 0.2%, and 0.1%
2. \# usual mutations: number of amino acid differences from the consensus B sequence excluding unusual mutations.
3. \# unusual mutations: number of amino acids with a prevalence &lt;0.01% in  published direct PCR dideoxynucleotide (Sanger) group M sequences in HIVDB. Mutations that are known drug-resistance mutations (i.e., have a mutation penalty score) are excluded from this list even if their prevalence is &lt;0.01%. The procedure for identifying unusual mutations is defined [here](/page/unusual-mutations/).
4. \# DRMs: number of drug-resistance mutations defined as any mutation with a mutation penalty score (including polymorphic mutations and those with low scores).
5. \# signature APOBEC mutations: # mutations suggestive of G-to-A hypermutation defined according to a procedure outlined [here](/page/apobecs/). The presence of ≥3 signature APOBEC DRMs in a _pol_ sequence
6. \# APOBEC-context DRMs: DRMs that could result from the activity of APOBEC-mediated G-to-A hypermutations.

Mutation detection thresholds with large numbers of unusual or signature APOBEC mutations are likely too low and pose an unacceptable risk of identifying artifactual mutations caused either by machine error, PCR error, or G-to-A hypermutation. Genotypic resistance interpretations are suppressed for the 0.1% and 0.2% thresholds and for thresholds for which &gt;1% of positions have an unusual mutation. Genotypic resistance interpretations are currently not suppressed for samples containing ≥3 signature APOBEC DRMs. However, APOBEC-context DRMs present at the same threshold are at risk of resulting from APOBEC-mediated G-to- A hypermutation and are likely of questionable clinical significance.

### Warnings

Warnings appear to the right of the Mutation Statistics Table.

### Low abundance mutations

The graph button at the upper-right produces a histogram showing the prevalence of all variants present in &lt;20% of sequence reads. Grey histograms indicate usual mutations and red histograms indicate unusual mutations. A blue dot above the histogram indicates a drug-resistance mutation. The same mutation may be present below more than one histogram if it was encoded for by more than one codon. .

The spreadsheet button at the upper-right allows the user to download a spreadsheet listing all low-abundance codons in descending order of their prevalence within the NGS reads. The spreadsheet contains 13 columns:

1. Gene
2. Amino acid position
3. Number of reads for the position
4. Sequenced codon
5. Number of reads containing the codon
6. The codon’s amino acid translation
7. The % of reads containing the codon
8. The prevalence of the amino acid in HIVDB group M Sanger sequences
9. The prevalence of the codon in HIVDB group M Sanger sequences
10. DRM: Yes vs. empty field
11. Unusual: Yes vs. empty field
12. Signature APOBEC: Yes vs. empty field
13. APOBEC-context DRM: Yes vs. empty field

### Gene-specific drug-resistance interpretations

Interpretations are provided for mutations present above the mutation detection threshold provided the selected threshold was ≥0.5% and fewer than 1% of positions had an unusual mutation. The appropriate mutation detection threshold, however, cannot be identified with certainty in the absence of a sequencing protocol that uses unique molecular identifiers (UMIs) for each virus template.

Mutations detected at low thresholds are difficult to interpret because they are at increased risk of being artifactual and because few data have linked such mutations with an increased risk of virological failure in persons receiving contemporary ART regimens. Nonetheless, the genotypic resistance interpretation of HIVdb-NGS beta version currently does not consider the threshold at which a mutation is detected. Like the main HIVdb program, the purpose of HIVdb-NGS beta is educational with regard to its genotypic resistance interpretations and quality control analysis. The procedure for developing the drug-resistance interpretation system is outlined [here]($$CMS_PREFIX$$downloads/release-notes/genotypic-resistance-test-interpretation-system-oct2019.pdf).
