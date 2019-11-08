This page lists the change logs of current and previous versions of Sierra program since December 2017. For algorithm change logs (scoring tables and comments) please access
[Algorithm Updates](/page/algorithm-updates/) page.

## Version 2.4.2 update 2019-11-01

1. Replace HIVDB-implemented drug resistance score calculator by FrontierScience ASI Interpreter. The ASI Interpreter is 2 - 3 times slower than the original score calculator. However it provides us more flexibility through using the standard ASI files.
2. Upgrade ASI Interpreter to version 1.5.0.1 (HIVDB forked version [b446985](https://github.com/hivdb/asi_interpreter/commit/b446985221aa704a8b0184c33c5316ebc063de1a)).
3. Release [HIVDB Drug Resistance Algorithm Version 8.9-1](/page/algorithm-updates/#version.8.9-1.update.2019-11-01).  
   The version 8.9-1 requires ASI Interpreter >1.5.0.1. It has the same rules and mutation comments as version 8.9, but introduced "drug-level" comments through the new ASI syntax.

## Version 2.4.1 update 2019-10-28

This version fixed a bug that DRMs were not highlighted in sequence quality assessment graph of HIVdb, HIVseq and HIValg program.

## Version 2.4.0 update 2019-10-24

We included the first beta version of HIVDB program for NGS sequence reads in this release. Users can access [this link](/hivdb/by-reads/) to experience this new feature.

Please find the HIVdb-NGS (Beta) Release Notes [here](/page/hivdb-ngs-release-notes/).

## Version 2.3.5 update 2019-10-07

We upgraded the [HIVDB Drug Resistance Algorithm to V8.9](/page/algorithm-updates/#version.8.9.update.2019-10-07).

## Version 2.3.4 update 2019-09-13

In this bugfix release, we identified and fixed an issue: when a reverse complement of sequence was entered, the subtype and "pretty pairwise" output were incorrect.

As far as we know, the mutation list and drug resistance interpretation result are not affected by this bug.

## Version 2.3.3 update 2019-08-13

In this release, we updated the list of usual/unusual mutations, the list of signature APOBEC mutations, and the list of APOBEC context drug resistance mutations. The latest version of the three lists are included in the [HIVFacts](https://github.com/hivdb/hivfacts/releases/tag/2019.8) library (previously known as "HIV-AAPcnt") as version 2019.8.

This is the first time since 2016 we updated our APOBEC-related lists. The steps of identifying signature APOBEC mutations and APOBEC context DRMs were described in this document: [HIV-1 Signature APOBEC Mutations](/page/apobecs/).

## Version 2.3.2 update 2019-07-17

1. Upgrade ASI Interpreter to version 1.4.0.0 (HIVDB modified version [ee4481](https://github.com/hivdb/asi_interpreter/tree/ee4481).
2. Fix an issue that in certain circumstance, part of a mixture mutation is not included in "partialScores" explanation. Although the mutation is not included, we can confirm that the final drug resistance score is not affected at all.
3. (Frontend) Release new look of the home page.

### Version 2.3.2-1 update 2019-07-24

Frontend added [News & Updates](/pages/updates/) page.

## Version 2.3.1 update 2019-07-01

Follow changes was made in this release:
1. [A list of 24 INSTI SDRMs](/page/insti-sdrm-list/) has been added for our analyses.
2. GraphQL API is now accepting a custom list of mutations as a filter option for retrieving a list of mutations.
3. Upgrade CPR to version 8.0 (accepting IN sequences now).

## Version 2.3.0 update 2019-02-13

Three updates are introduced in this release:

1. [HIVDB Drug Resistance Algorithm V8.8](/page/algorithm-updates/#version.8.8.update.2019-02-13): INSTI rule and comment changes.
2. A new set of subtype & CRF sequences is created for determining the subtype for each input HIV-1 sequence. These subtype & CRF sequences and their description can be found in following study:
   Rhee SY and Shafer RW (2018). [Geographically-stratified HIV-1 group M pol subtype and circulating recombinant form sequences.](/pages/pdf/Rhee.2018.SData.pdf) *Scientific Data*. 2018 July 31.
3. Frontend interface improvement of [SGS database](/project/sgs/).

## Version 2.2.11 update 2019-01-10

ANRS Algorithm has been upgraded to v29 (Nov 2018): [XML][asiAnrs29], [PDF][ANRS_PDF_29]  
Rules were added for two new drugs: FTR (fostemsavir) and BIC (bictegravir). Three rules were changed for DOR (doravirine).

In addition, we changed the type of mutation RT:106I from "Other" to "NNRTI".

## Version 2.2.10 update 2018-11-26

In this release, we introduce a new version-controlled library [HIV-AAPcnt](https://github.com/hivdb/hiv-aapcnt) for the unusual mutations process. The HIV-AAPcnt version used by this release is 2018.11-2.

Correspondingly, we also updated our [Release Notes](/page/release-notes/) to reflect this change.

## Version 2.2.9 update 2018-10-19

Two upgrades are introduced in this release:

1. Released [HIVDB Algorithm V8.7][asi87].
2. Miscellaneous frontend improvements: e.g. 1) dependency upgrades; 2) rewrite sequence QA graph.

## Version 2.2.8 update 2018-09-13

Two major upgrades are introduced in this release:

1. Upgrade to [NucAmino 0.2.0-beta.2](https://github.com/hivdb/nucamino/releases/tag/0.2.0-beta.2).
2. Improve performance by adding an option to use AWS Lambda for sequence alignment (NucAmino). The detail can be found here: [README.md#nucamino-on-aws-lambda](https://github.com/hivdb/sierra/blob/94dc1f/README.md#nucamino-on-aws-lambda).

## Version 2.2.7 update 2018-07-12

Two major changes were made in this version:

1. Released [HIVDB Algorithm V8.6][asi86].
2. [Changed a post-alignment parameter](https://github.com/hivdb/sierra/commit/11ca00) so we don't remove too many sites from both sides of sequence alignment.

### Post-release 2.2.7-1

A post-release of HIVDB algV8.6.1 which updated comments for PIs and INSTIs.

## Version 2.2.6 update 2018-06-11

Two changes were made in this version:

1. ANRS Algorithm has been upgraded to v28 (Apr 2018): [XML][asiAnrs28], [PDF][ANRS_PDF_28]  
   Since v28, drug code DRV/r and DTG have been removed from the ASI file. Instead, we now use DRV/r\_QD, DRV/r\_BID, DTG\_QD and DTG\_BID to indicate the rules for low and high dose DRV/r and DTG, respectively.
2. [Resistance Notes for INSTI](/dr-summary/resistance-notes/INSTI/) has been updated in order to reflect the recent changes in HIVDB algorithm (8.4 to 8.5).

### Post-release 2.2.6-1

Fixed a mistake in the ASI file of ANRS v28 (doesn't affect scores).

## Version 2.2.5 update 2018-04-10

This version includes a bugfix of Sierra program, a new warning message and a compatible interface change to the Sierra GraphQL Web Service.

1. Fixed a bug which caused incomplete spreadsheet output. The bug was triggered when a reverse complement sequence was submitted.
2. A warning was added when the submitted sequence was a reverse complement.
3. A boolean value "isReverseComplement" was added to the GraphQL output "SequenceAnalysis" object.

### Post-release 2.2.5-1

HIVDB Drug Resistance Algorithm has been updated to version 8.5 in this release. Following one modification was made to reflect this upgrade.

1. A New ARV "BIC" was added to "INSTI" section in drug display options of [HIVDB Program](/hivdb/by-mutations/).

## Version 2.2.4 update 2018-03-29

This version includes a frontend update and a bugfix of Sierra Web Service.

1. Several important mutations were added to the mutations entering interface (e.g. [HIVDB Program](/hivdb/by-mutations/)): RT65E, RT68d, RT70d, PR73DV, IN74I, IN138T, IN143AGS, and IN148N.
2. Instead of returning an empty resistance result, mutations analysis and pattern analysis (GraphQL) are now able to return a totally sensitive report if all present gene positions are wild type amino acids.

## Version 2.2.3 update 2018-01-22

Limitations were applied to sequences analysis (GraphQL) in this update to prevent server out-of-resources issue.

The number of sequences that can be submitted per each HTTP request is now limited to 120 sequences. The maximum length of each sequence is now limited to 15,000 nucleotides.

This change will affected some third-party clients if they didn't split a large set of sequences into chunks before sending those sequences to HIVDB. To fix this issue, we suggest you to modify your client to send 20 sequences to HIVDB per each request. If you need assistance of this modification, please contact Philip Tzou &lt;philiptz[at]stanford.edu&gt;. This technique has been implemented in both SierraPy and our website for years. Users who are using SierraPy or our website are not affected.

## Version 2.2.2 update 2018-01-19

This update added a new field to GraphQL object `Mutation`:

<pre>
...
mutations {
  ...
  <strong>isSDRM</strong>  # indicate a mutation is a Surveillance Drug
          # Resistance Mutation (SDRM) or not
  ...
}
...
</pre>

## Version 2.2.1 update 2018-01-09

This update replaced the algorithms of ANRS and Rega to their latest versions.

1. ANRS Algorithm was upgraded to v27 (Sep 2017): [XML][asiAnrs27], [PDF][ANRS_PDF_27]
2. Rega Institute Algorithm was upgraded to 10.0.0 (May 2017): [XML][asiRega], [PDF][REGA_PDF]

### Post-release 2.2.1-1

The ANRS algorithm was updated to version 27 (see PDF) on January 9. We have since made two modifications to this update.

The ANRS algorithm has different scores for dolutegravir (DTG) 50mg QD and DTG 50mg BID as well as for darunavir/r (DRV/r) 600mg/100mg BID and DRV/r 800mg QD. We have modified the ASI implementation of the algorithm as follows. The rules for low and high dose DTG are indicated by DTGQD and DTGBID, respectively. The rules for low and high dose DRV/r are indicated by DRV/r\_QD and DRV/r\_BID, respectively.

For users of HIValg, DTG will contain the same rules as DTGQD and DRV/r will contain the same rules as those for DRV/r\_QD.

## Version 2.2.0 update 2017-12-18 (code name "NucAmino")

This is a major update to the HIVDB genotypic resistance interpretation program software Sierra. The main part of this update is a change from the alignment program [LAP (Local Alignment Program)](https://www.ncbi.nlm.nih.gov/pubmed/9021268) to an open source alignment program [NucAmino](https://github.com/hivdb/nucamino). This change has allowed us to open source the complete software pipeline for the HIVDB genotypic resistance interpretation program ([github.com/hivdb/sierra](https://github.com/hivdb/sierra)). The new version of Sierra which uses NucAmino is now called 2.2 and the older version of Sierra which used LAP is now called 2.1.

This change from Sierra 2.1 to Sierra 2.2 provides additional impetus for users of the old Sierra 1.1 SOAP web service to migrate to the Sierra 2 GraphQL web service. Although the interpretation system has not been changed, the change in alignment, quality control, and warnings will affect the interpretations of a small subset of sequences. Therefore, if you are still using the SOAP version of Sierra, please visit [this page](/page/webservice/). Feel free to [contact us](mailto:hivdbteam@stanford.edu) if you need any help with migration.

The switch from LAP to NucAmino has been accompanied by several additional changes to the process of aligning submitted sequences to HIV-1 pol:

1. Each submitted sequence is aligned to the complete HIV-1 pol reference subtype B sequence rather than to PR, RT, and IN separately. This results in slightly different handling of the small number of sequences that previously exhibited alignment anomalies at the PR/RT and RT/IN boundaries.
2. We have also introduced stricter criteria for quality control at the beginning and end of sequences.
3. We have introduced a new set of warnings for sequences (i) containing very short regions of PR, RT, or IN; (ii) containing poor quality at its boundaries; and (iii) containing inappropriate concatenations of noncontiguous regions of pol.

As with any change to an alignment algorithm, there will be minor differences in the placement of frameshifts and unusual indels and in the handling low quality regions at sequence boundaries. To determine the effect of the change from LAP to NucAmino, we ran Sierra versions 2.1 and 2.2 on 115,118 HIV-1 pol-containing GenBank sequences. For each sequence we recorded the GenBank accession number, pol sequence coverage, the list of mutations (including indels) and frameshifts. We have created a spreadsheet that contains 5,501 sequences for which Sierra versions 2.1 and 2.2 yielded non-identical results:

1. For 3,639 sequences, Sierra 2.2 applied stricter filtering of amino acids found at the sequence’s 5’ and 3’ ends. For these sequences, the median number of filtered amino acids was 3 (range: 1 to 145). For 34 of these sequences, a DRM (defined as a mutation that receives a drug-resistance mutation penalty) was filtered. The filtered mutations included: PR10F (2), PR20T (2), PR82L (1), RT41L (1), RT108I\_115F\_138G (1), RT184I (1), RT188F (1), RT215A\_210R (1), RT215S\_227L (1), RT219Q (1), RT221Y (1), RT225H (1), RT227L (2), RT230I (3), RT238T (1), RT318F (3), RT348I (9), IN155H (1), IN263K (1). Each of these cases was reviewed manually to ensure that filtering was appropriate. Additionally, a warning is provided to indicate the number of amino acids filtered at sequence boundaries. For four sequences, Sierra 2.2 applied a less strict filter and a median of 2.5 addition amino acids (range: 1 to 4).
2. For 1,045 sequences, there was a difference in how frameshifts were handled. This occurs due to a largely unavoidable amount of stochasticity in the alignment process when frameshifts (which are usually technical artifacts) are present. This resulted in 11 sequences with different DRMs. For eight sequences, Sierra 2.1 detected DRMs not detected by Sierra 2.2 including RT41L (1), RT65R (1), RT100I (1), RT100I\_103N (1), RT103N (2), and RT215N (2). For three sequences, Sierra 2.2 detected DRMs not detected by Sierra 2.1 including RT65E (1), RT67N (1), and RT70R (1). In each of these examples, the version that did not detect the DRM placed the frameshift at the DRM position or detected a highly unusual mutation at the DRM position. In each of these cases, it could not be inferred which version produced the preferable alignment. Additionally, a warning is provided to indicate the presence of the frameshift.
3. There were 695 sequences containing a protease sequence concatenated to a section of RT that did not include the 5’ part of its sequence. For example, the RT sequence would often begin at about position 35. This was common in sequences generated by the TruGene Assay. Sierra 2.1 occasionally found that the end of PR could align to the beginning of RT resulting in an inappropriate sequence overlap. This has now been corrected. This change did results in any difference in detectable DRMs.
4. For 47 sequences, the placement of an indel (an insertion or deletion of one or more nucleotide triplets), differed between Sierra 2.1 and Sierra 2.2 largely as a result of  unavoidable stochasticity: (i) For 24 of these sequences, there was an insertion in the PR codon 33/41 loop region. In two cases this resulted in the detection of PR33F by Sierra 2.2 but not Sierra 2.1; (ii) For 20 of these sequences, there was an indel in either PR, RT, or IN. The changed placement of the indel did not result in a change in detectable DRMs; and (iii) For 3 sequences, Sierra 2.1 detected a deletion at RT codon 69, whereas Sierra 2.2 placed the deletion at RT codon 70. Each of these deletions receive a similar mutation penalty. Of note, Sierra 2.1 and 2.2 agreed on the placement of deletions in this region in the remaining 61 sequences containing a deletion at each of these positions. The two versions always agreed on the placement of insertions in this region (placing them at codon 69) as a result of post-processing performed after the alignment.
5. There were 38 sequences with (i) short gene fragments, which were generally of low quality; (ii) deletions or more than 30 bp; or (iii) an unusual concatenation of multiple partial genes were filtered by Sierra 2.2 but not Sierra 2.1.
6. There were 33 sequences containing concatenations of multiple partial genes, separated by ‘N’s. This resulted in some partial gene sequences being detected by Sierra 2.2 but not Sierra 2.1. Fifteen of these 33 sequences contained PI-resistance mutations. These sequences were accompanied by a warning indicating that the complete gene had not been sequenced.

The raw comparison result can be found in this Excel spreadsheet: [download][sierra21v22].

[sierra21v22]: $$CMS_PREFIX$$downloads/release-notes/sierra-comparison-v2_1-vs-v2_2.xlsx
[asiAnrs27]: $$CMS_PREFIX$$downloads/asi/ANRS_27-stanford2.xml
[asiAnrs28]: $$CMS_PREFIX$$downloads/asi/ANRS_28.xml
[asiAnrs29]: $$CMS_PREFIX$$downloads/asi/ANRS_29.xml
[asi86]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.6.xml
[asi87]: $$CMS_PREFIX$$downloads/asi/HIVDB_8.7.xml
[asiRega]: $$CMS_PREFIX$$downloads/asi/Rega_10.0.xml
[ANRS_PDF_27]: http://www.hivfrenchresistance.org/2017/Algo2017-hiv1.pdf
[ANRS_PDF_28]: http://www.hivfrenchresistance.org/2018/Algo2018-hiv1.pdf
[ANRS_PDF_29]: http://www.hivfrenchresistance.org/2018b/Algo-nov2018-HIV1.pdf
[REGA_PDF]: https://rega.kuleuven.be/cev/avd/software/rega-hiv1-rules-v10.pdf