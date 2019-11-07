## Overview

The CPR (Calibrated Population Resistance) tool is a program for analyzing populations of human immunodeficiency type 1 (HIV-1) sequences. CPR provides a standard approach for determining the proportion of submitted sequences containing a mutation suggestive of transmitted HIV-1 drug resistance.

CPR uses the list of surveillance drug-resistance mutations (SDRMs) as indicators of transmitted resistance. CPR ensures consistency in the analysis of molecular epidemiologic studies by providing investigators access to a standard protocol for handling missing data and identifying sequence artifacts. Unlike the HIVdb interpretation program, CPR does not provide a drug resistance interpretation.

Major updates since 2018:

- CPR 7.0 (2018-12-18): Updated to use the alignment process of the latest Sierra program (2.2.10) rather than the original stand-alone program.
- CPR 8.0 (2019-07-01): A list of 24 integrase SDRMs (SDRM\_2019) was added for analyzing integrase sequences.

## Input

### Query dataset

CPR accepts a set of FASTA-formatted HIV-1 RT, protease (PR) or integrase (IN) gene nucleotide sequences as input sequences. Sequences can be passed into the textbox or uploaded as a file containing up to 10,000 non-interleaved FASTA sequences. Consistent with the FASTA format, each sequence should be preceded by a line containing ">" followed by a sequence name and optionally followed by additional descriptors separated by pipes ("|"). However, a neighbor-joining tree will be generated only for sequence sets with 500 or fewer sequences.

### Surveillance drug-resistance mutation (SDRM) list

The surveillance drug-resistance mutations (SDRMs) were designed to be sensitive and specific indicators of antiretroviral drug selection pressure. A standard list of SDRMs makes it possible to compare the results of sequencing studies performed in different regions or at different times. Mutations on the current SDRM list \[[appendix 1](#appendix.1.sdrm.lists)\] were selected for their suitability as indicators of transmitted resistance: (a) they are commonly recognized as causing or contributing to resistance; (b) they are nonpolymorphic in untreated persons; and (c) they are applicable to all HIV-1 subtypes. 

## Processing

### Sequence alignment and amino acid translation

Each submitted nucleotide sequence is aligned to [the consensus subtype B amino acid reference sequence](/page/release-notes/#appendix.1.consensus.b.sequences) using NucAmino [^Tzou2017] The aligned nucleotide sequence is translated in the correct reading frame. Nucleotide triplets containing IUPAC ambiguities (e.g. R indicates a mixture of A and G) are translated into each of the possible amino acids they encode. For example, ATR indicates a mixture of ATA (Isoleucine; I) and ATG (Methionine; M). Nucleotide triplets encoding >4 possible different amino acids or containing a 'N' (a highly ambiguity nucleotide indicating 'G', 'A', 'T' or 'C') at the first or second nucleotide in a codon are translated to "X". Amino acid differences from the reference sequence are referred to as mutations.

RT sequences with fewer than 150 amino acid positions, protease sequences with fewer than 60 amino acid positions, integrase sequences with fewer than 197 amino acid positions, or sequences of either gene with <50% identity to the consensus reference sequences will not be analyzed further.


[^Tzou2017]: Tzou PL, Huang X, Shafer RW. NucAmino: a nucleotide to amino acid alignment optimized for virus gene sequences. [BMC Bioinformatics 2017](https://www.ncbi.nlm.nih.gov/pubmed/28249562).

### Sequence and SDRM quality assessment

Sequences are assessed for their completeness and quality. Indicators of decreased quality include stop codons, frame-shifts, highly ambiguous nucleotides (B, D, H, V and N), evidence for APOBEC3G/F hypermutation \[[appendix 2](#appendix.2.apobec3g.f.hypermutations)\], previously unpublished insertions and deletions, and a marked excess of highly unusual amino acid mutations \[[appendix 3](#appendix.3.highly.unusual.amino.acid.mutations)\].

Each SDRM is also examined for its reliability by assessing whether the mutation could be a result of a regional sequence artifact. To this end, we determine whether (a) the SDRM resulted from a GG AG (APOBEC3G) or GA AA (APOBEC3F) mutation in a sequence that has evidence for APOBEC-mediated hypermutation; (b) the SDRM is a possible artifact of a gap present within the alignment; (c) the SDRM is adjacent to a stop codon, an amino acid translated to an 'X', or ≥2 highly unusual mutations; and (d) the SDRM is part of a complex mixture that cannot be explained as a transition from wild-type to mutant or vice versa \[[appendix 4](#appendix.4.highly.complex.and.rare.mixtures)\].

The QA criteria for sequence inclusion and SDRM exclusion is listed in [appendix 5](#appendix.5.sequence.sdrm.quality.assessment.criteria). Subtle changes to the QA criteria are likely to made in the future. These changes will result in a new version number for the program.

### Proportions of sequences with SDRMs by drug class

The following proportions of sequences containing an SDRM are calculated. For PRRT sequences:

a. proportion of sequences containing at least one NRTI, NNRTI, or PI SDRM;
b. proportion of sequences containing at least one NRTI SDRM (whether or not NNRTI or PI SDRMs is also present);
c. proportion of sequences containing at least one NNRTI SDRM (whether or not NRTI or PI SDRMs is also present);
d. proportion of sequences containing at least one PI SDRM (whether or not NRTI or NNRTI SDRMs is also present);
e. proportion of sequences containing both NRTI and NNRTI SDRMs;
f. proportion of sequences containing NRTI, NNRTI, and PI SDRMs.

For IN sequences:

a. proportion of sequences containing at least one INSTI SDRM.

### Phylogenetic analysis

A phylogenetic tree is created from the submitted sequences and a set of reference subtype sequences belonging to subtype A1, A2, B, C, D, F1, F2, G, H, J, K, CRF01\_AE and CRF02\_AG. The tree is created by the PAUP program using the neighbor-joining method applied to a matrix of genetic distances calculated using the HKY85 substitution model and a gamma distribution at variable sites. The tree is rooted with a group N sequence.

The median pairwise distance of submitted sequences is also calculated using PAUP.

A 500 sequences limitation is applied for this analysis.

## Output

The CPR report consists of a Summary page and four additional detailed reports accessible using the tabs located at the top of the page: Summary, Methods, QA Details, Complete Mutation List, and Genetic Diversity.

### Title Area

Version of SDRM list, date of CPR report generation, version of Sierra and HIVDB algorithm used for this report. Options for downloading the same summary page in pdf and the CPR analysis details in excel.

### Summary

#### Number of input sequences

A table summarizing the numbers of sequences by gene in the input data set. This table also notes whether sequences were filtered because they were too short or were considered to have too many errors to be analyzable.

For PRRT sequences, the table contains five rows: (a) sequences: number of sequences submitted regardless of gene or sequence length; (b) sequences containing either RT or PR: sequences of sufficient length containing RT and/or PR; (c) sequences containing RT (±PR); (d) Sequences containing PR (±RT); (e) sequences containing both RT and PR.

For IN sequences, the table contains two rows: (a) sequences: number of sequences submitted regardless of gene or sequence length; (b) Sequences containing IN: sequences of sufficient length containing IN.

If any sequences are filtered, those sequences and the criteria used for filtering will be listed in QA Details.

#### SDRM position coverage

For each ARV drug class, a table lists for each SDRM position (a) the number of sequences not encompassing an SDRM position, (b) the number of sequences for which the SDRM position was sequenced but considered not evaluable, and (c) the number of sequences that were evaluable for the presence of the SDRM.

#### Proportion of sequences with SDRMs
For PRRT sequences: (a) proportion of sequences containing at least one NRTI, NNRTI, or PI SDRM; (b) proportion of sequences containing at least one NRTI SDRM (whether or not NNRTI or PI SDRMs are also present); (c) proportion of sequences containing at least one NNRTI SDRM (whether or not NRTI or PI SDRMs are also present); (d) proportion of sequences containing at least one PI SDRM (whether or not NRTI or NNRTI SDRMs are also present); (e) proportion of sequences containing both NRTI and NNRTI SDRMs; (f) proportion of sequences containing NRTI, NNRTI, and PI SDRMs.

For IN sequences: proportion of sequences containing at least one INSTI SDRM.

#### Sequences with SDRMs

A table listing each of the SDRMs for those sequences containing one or more SDRMs.

### Methods

This page summarizes (a) the list of SDRMs, (b) sequence inclusion criteria and (c) SDRM position exclusion criteria used for CPR analysis.

### QA Details

#### Number of input sequences

The same table as [the first table](#number.of.input.sequences) on the Summary page.

#### QA analysis results of each submitted sequence

Table listing the QA analysis results for each sequence and for each gene:

a. **gene** - gene name (PR, RT or IN). RT, PR and IN sequences from the same individual will follow one another;
b. **first pos** - the first amino acid position sequenced;
c. **last pos** - the last amino acid position sequenced;
d. **No. of stops, insertions/deletions and Xs** - the total number of stop codons + previously unpublished insertions/deletions + codons translated to X;
e. **No. A3GF** - number of APOBEC3G/F hypermutations;
f. **No. highly unusual** - number of highly unusual mutations;
g. **Sequence filtered** - a check mark if the sequence does not meet a sequence inclusion criteria;
h. **SDRM position excluded** - a list of SDRM positions excluded from counting as SDRMs if any;
i. **Mutation list** - the complete list of amino acid differences from the consensus reference sequence. Stop codons, insertions/deletions/Xs were indicated in color orange, APOBEC3G/F hypermutations in yellow, highly unusual mutations in gray, and SDRMs in red.

### Complete mutation list

#### Proportion of sequences with SDRMs

The same table as [the Proportion of sequences with SDRMs table](#proportion.of.sequences.with.sdrms) on the Summary page.

#### Sequences with SDRMs

The same table as [the Sequences with SDRMs table](#sequences.with.sdrms) on the Summary page.

#### Number of sequences according to number of SDRMs

Table listing the number of sequences according to the number of SDRMs for each drug class.

#### SDRM analysis results of each sequence

A table listing for each sequence. For PRRT sequences: (a) a complete PR mutation list; (b) a complete RT mutations; (c) number of PI SDRMs; (d) number of NRTI SDRMs; (e) number of NNRTI SDRMs.

For IN sequences: (a) a complete IN mutation list; (b) number of INSTI SDRMs.

SDRMs are indicated in red.

### Genetic Diversity

A simple representation of phylogenetic tree of submitted sequences. A number was assigned to each sequence name to ensure the sequence name is unique for creating a tree. For sequences containing SDRMs, the list of SDRMs was indicated in the sequence name and it was colored in red. The names of subtype reference sequences and a group N sequence for rooting were indicated in color blue. The median pairwise distance of submitted sequences is shown on the top of the tree.

The nexus tree file can be downloaded for viewing the tree using tree viewing tools. The distance matrix created by Paup can also be downloaded.

## Appendices

### Appendix 1: SDRM lists

[SDRM 2009 (PRRT)](/page/who-sdrm-list/)[^Benett2009] / [SDRM 2019 (IN)](/page/insti-sdrm-list/)[^Tzou2019]

[^Benett2009]: Bennett DE, Camacho RJ, Otelea D, Kuritzkes DR, Fleury H, Kiuchi M, Heneine W, Kantor R, Jordan MR, Schapiro JM, Vandamme AM, Sandstrom P, Boucher CA, van de Vijver D, Rhee SY, Liu TF, Pillay D, Shafer RW. Drug resistance mutations for surveillance of transmitted HIV-1 drug-resistance: 2009 update. [PLoS One 2009](https://www.ncbi.nlm.nih.gov/pubmed/19266092).
[^Tzou2019]: Tzou PL, Rhee SY, Descamps D, Clutter DS, Hare B, Mor O, Grude M, Parkin N, Jordan MR, Bertagnolio S, Schapiro JM, Harrigan PR, Geretti AM, Marcelin A, Shafer RW. Integrase Strand Transfer Inhibitor Resistance Mutations for Surveillance of Transmitted HIV-1 Drug Resistance. [J Antimicrob Chemother 2019](https://www.ncbi.nlm.nih.gov/pubmed/31617907) ([pdf](https://hivdb.stanford.edu/pages/pdf/Tzou.2019.JAC.pdf)).

### Appendix 2: APOBEC3G/F hypermutations

HIV-1 sequences occasionally contain an excess of guanine (G) to adenine (A) substitutions introduced by the sequence editing activity of host enzymes belonging to the APOBEC family of cytidine deaminases, most notably APOBEC3G (GG → AG) and APOBEC3F (GA → AA). Although it has been suggested that some degree of sub-lethal editing by APOBEC enzymes may contribute to HIV-1 evolution, extensive G-to-A editing generally leads to mutational impairment of viruses. Sequence variation in lethally edited viruses reflects qualitatively different biological processes to variation in viable viral genomes (i.e. sequence editing as opposed to purifying selection). It is therefore useful to identify lethally edited sequences in analyses that assume data to represent viable genetic material under selection, such as genotypic estimation of drug resistance.

The APOBEC3G/F hypermutations[^Gifford2008][^Rhee2016] are rare substitutions that are commonly found in sequences that have been extensively edited by APOBEC3G/F, but are uncommon in other sequences. The occurrences of three or more APOBEC3G/F mutations within a single PR-RT sequence is taken as indicating a >99% probability of a background of likely lethal, APOBEC-mediated editing.

[APOBEC3G/F v.1](/page/release-notes/#data.files)

[^Gifford2008]: Gifford RJ, Rhee SY, Eriksson N, Liu TF, Kiuchi M, Das AK, Shafer RW. Sequence editing by Apolipoprotein B RNA-editing catalytic component-B and epidemiological surveillance of transmitted HIV-1 drug resistance. [AIDS 2008](https://www.ncbi.nlm.nih.gov/pubmed/18356601).
[^Rhee2016]: Rhee SY, Sankaran K, Varghese V, Winters MA, Hurt CB, Eron JJ, Parkin N, Holmes SP, Holodniy M, Shafer RW. HIV-1 Protease, Reverse Transcriptase, and Integrase Variation. [J Virol 2016](https://www.ncbi.nlm.nih.gov/pubmed/27099321).

### Appendix 3: Highly unusual amino acid mutations

The Stanford HIV Drug Resistance Database is updated regularly with new sequence data and maintains a list of 'usual' mutations in the protease-RT region of HIV-1 group M viruses. Mutations that are not on this list (i.e. unusual or atypical mutations) may represent rare polymorphisms, novel drug resistance mutations, or artifacts introduced during sequencing or conceptual translation (e.g. when attempting to infer codons from sequences containing nucleotide mixtures).

[Usual mutations v.1: protease, RT, and integrase](/page/release-notes/#data.files)

### Appendix 4: Highly complex and rare mixtures

Mixtures of three and more amino acids that are not included in the list of allowable complex mixtures.

[Allowable complex mixtures v.1][complexMixturesTextFile]

### Appendix 5: Sequence & SDRM quality assessment criteria

Version 1: July, 2011

<table><!--
  --><caption>Table 1. Sequence inclusion criteria</caption><!--
  --><thead><!--
    --><tr><!--
      --><th></th><th>RT</th><th>PR</th><th>IN</th><!--
    --></tr><!--
  --></thead><!--
  --><tbody><!--
    --><tr><!--
      --><td>Minimum amino acid(AA) coverage</td><!--
      --><td>Positions 65 to 215</td><!--
      --><td>Positions 30 to 90</td><!--
      --><td>Positions 66 to 263</td><!--
    --></tr><!--
    --><tr><!--
      --><td>Maximum number of stop codons + unpublished AA insertions or deletions + highly ambiguous nucelotides (B,D,H,V,N)</td><!--
      --><td>4</td><td>2</td><td>3</td><!--
    --></tr><!--
    --><tr><!--
      --><td>Maximum number of <a href="#appendix.2.apobec3g.f.hypermutations">APOBEC3G/F hypermutated AAs</a></td><!--
      --><td>3</td><td>2</td><td>3</td><!--
    --></tr><!--
    --><tr><!--
      --><td>Maximum number of <a href="#appendix.3.highly.unusual.amino.acid.mutations">highly unusual AA mutations</a></td><!--
      --><td>15</td><td>8</td><td>10</td><!--
    --></tr><!--
  --></tbody><!--
--></table>

<br />
<table><!--
  --><caption>Table 2. SDRM exclusion criteria</caption><!--
  --><tbody><!--
    --><tr><td>PR SDRM D30N, M46I, G73S, RT SDRM D67N, M184I, G190SE, and IN SDRM G118R, E138K, G140S, R263K in sequences containing >= 2 APOBEC3G/F hypermutated AAs</td></tr><!--
    --><tr><td>SDRMs adjacent to an insertion or deletion or frame-shift</td></tr><!--
    --><tr><td>SDRMs adjacent to >=2 highly unusual AA mutations, AAs with highly ambiguous nucleotides, or stop codons</td></tr><!--
    --><tr><td>SDRMs as a part of a <a href="#appendix.4.highly.complex.and.rare.mixtures">highly complex mixture</a></td></tr><!--
  --></tbody><!--
--></table>

[complexMixturesTextFile]: $$CMS_PREFIX$$downloads/cpr/allowable-complex-mixtures-v1.txt
