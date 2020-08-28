## Aug 2020

**[Sierra 3.0.7](/page/program-updates/#version.3.0.7.update.2020-08-28)** - Bugfix release. See [program release notes](/page/program-updates/#version.3.0.7.update.2020-08-28) for more details.

## July 2020

**[Sierra 3.0.6](/page/program-updates/#version.3.0.6.update.2020-07-23)** - Bugfix release. See [program release notes](/page/program-updates/#version.3.0.6.update.2020-07-23) for more details.

## June 2020
**Database update:**
- HIVDB: 82 new studies entered 
- GenBank: 79 new GenBank submissions imported

**[DTG resistance reference library](/pages/refLib/DTG.html)**  - 79 new studies annotated

**[Sierra 3.0.5](/page/program-updates/#version.3.0.5.update.2020-06-24)** - Bugfix release. See [program release notes](/page/program-updates/#version.3.0.5.update.2020-06-24) for more details.

## May 2020
**[Sierra 3.0.0](/page/program-updates/#version.3.0.0.update.2020-05-10), [Sierra 3.0.1](/page/program-updates/#version.3.0.1.update.2020-05-11), [Sierra 3.0.2](/page/program-updates/#version.3.0.2.update.2020-05-12), [Sierra 3.0.3](/page/program-updates/#version.3.0.3.update.2020-05-19), and [Sierra 3.0.4](/page/program-updates/#version.3.0.4.update.2020-05-21)** - Major refactoring upgrade of Sierra software and HIVDB website. See [program release notes](/page/program-updates/#version.3.0.0.update.2020-05-10) for more details.


## April 2020
**[Sierra 2.5.1](/page/program-updates/#version.2.5.1.update.2020-04-29)** - Bugfix: an issue that Sierra didn't return validation results for mutations analysis correctly.

## February 2020
**Database update:**
- HIVDB: 9 new studies entered 
- GenBank: 34 new GenBank submissions imported

**ACTG 5175 Clinical Trial [Dataset](/pages/clinicalStudyData/ACTG5175.html):**
- Kantor, et al., Pretreatment HIV Drug Resistance and HIV-1 Subtype C Are Independently Associated With Virologic Failure: Results From the Multinational PEARLS (ACTG A5175) Clinical Trial. [Clin Infect Dis. 2015 May 15;60(10):1541-9](https://academic.oup.com/cid/article/60/10/1541/338500)

## January 2020
**[Sierra 2.5.0](/page/program-updates/#version.2.5.0.update.2020-01-24)** - In HIVdb, HIValg, and HIVseq program, we previously ignored a mixture consisted by more than four amino acids. We have changed this threshold to six for reducing the chance of false negative reports. (Update: In an early version, the threshold was incorrectly stated as changed "to eight". It should be changed to six.)

## November 2019
**[Sierra 2.4.2](/page/program-updates/#version.2.4.2.update.2019-11-01) and [HIVDB Algorithm 8.9-1](/page/algorithm-updates/#version.8.9-1.update.2019-11-01)** - we replaced HIVDB-implemented drug resistance score calculator by FrontierScience ASI Interpreter, which gives us more flexibility of rule customization and therefore allows us to provide more features in the near future, such as selection of HIVDB algorithm versions. HIVDB Drug Resistance Algorithm is therefore upgraded to version 8.9-1 to adopt the new "drug-level comment" syntax introduced by the latest ASI Interpreter. No change was made to the 8.9 rules or mutation comments.

## October 2019
**[HIVdb-NGS (beta)](/hivdb/by-reads/)** - a program for accepting NGS HIV-1 pol data and returning a genotypic resistance interpretation and quality control information helpful to selecting a mutation detection threshold.

Last month Jonathan Schapiro, Daniel Kuritzkes, and Michelle Moorhouse joined an **[Advisory Committee](/pages/Committee_HIVdb.html)** to provide recommendations for the HIV genotypic resistance interpretation system. Their input was reflected in the most recent update to the HIVDB algorithm - version 8.9. This update included score changes and updated comments for the NNRTI class (particularly doravirine) and for the INSTI class (particularly DTG and BIC).

**[HIVDB Algorithm version 8.9](/page/algorithm-updates/#version.8.9.update.2019-10-07)**
- Updated INSTI and NNRTI scores and comments

## September 2019
**[Annotated HIV2 resistance reference library](/pages/refLib/HIV2.html)**

**Database update:**
- HIVDB: 33 new studies entered 
- GenBank: 73 new GenBank submissions imported

## August 2019
**Update to HIVDB phenotype queries:**
- Retrieved datasets downloadable as tab-delimited file

**Update of Signature APOBEC mutations and other lists**
- First time since 2016 we updated the list of signature APOBEC mutations and the list of APOBEC context drug resistance mutations. ([list & rules](/page/apobecs/))
- The usual and unusual mutations list were updated according to the latest HIVDB database.
- The Sierra program version has been updated to 2.3.3 (2019-08-13) accordingly to refect the above two updates.

## July 2019
**ACTG 5275 Clinical Trial [Dataset](/pages/clinicalStudyData/ACTG5275.html):**
- Lennox JL, et al., Efficacy and tolerability of 3 nonnucleoside reverse transcriptase inhibitor-sparing antiretroviral regimens for treatment-naive volunteers infected with HIV-1: a randomized, controlled equivalence trial. [Ann Intern Med. 2014 Oct 7;161(7):461-71](https://annals.org/aim/fullarticle/1911116/efficacy-tolerability-3-nonnucleoside-reverse-transcriptase-inhibitor-sparing-antiretroviral-regimens)

**"Amino Acid Prevalence of HIV-1 pol Mutations by Direct PCR and Single Genome Sequencing" published in [AIDS Res Human Retrovirus](https://www.liebertpub.com/doi/abs/10.1089/AID.2018.0289)**
- Contains meta-analysis of data from the [HIV-1 pol Single Genome Sequence Database page](/project/sgs/)

## June 2019
**[Interactive map](/page/surveillance-map/) of HIV-1 drug resistance rates in untreated populations:**
- Updated to reflect published studies in GenBank from 2014-2018; 442 studies of 95,024 persons

**Provisional list of INSTI surveillance DRMs (SDRMs):**
- [Calibrated Population Resistance (CPR)](/cpr/) updated with option to upload IN sequences with mutation prevalence determined using INSTI SDRMs
- [Manuscript](/pages/pdf/Tzou.2019.JAC.pdf) submitted describing the derivation of the list of INSTI SDRMs

**"A systematic review of the genetic mechanisms of dolutegravir resistance" published in [J Antimicrob Chemother](https://academic.oup.com/jac/advance-article/doi/10.1093/jac/dkz256/5529201)**

**Update to most HIVDB queries:**
- Retrieved datasets downloadable as either fasta file or tab-delimited file

## April 2019
**Updated release of [Steps and Criteria for Classifying Unusual Mutations](https://github.com/hivdb/hivfacts)**

**"National and International Dimensions of Human Immunodeficiency Virus-1 Sequence Clusters in a Northern California Clinical Cohort." published in [Open Forum Infect Dis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6483754/)**

**"Multiplex Solid-Phase Melt Curve Analysis for the Point-of-Care Detection of HIV-1 Drug Resistance." published in [J Mol Diagn](https://www.sciencedirect.com/science/article/pii/S1525157818302745?via%3Dihub)**

**ACTG 5208 Clinical Trial [Dataset](/pages/clinicalStudyData/ACTG5208.html):**
- Lockman S, et al., Nevirapine- versus lopinavir/ritonavir-based initial therapy for HIV-1 infection among women in Africa: a randomized trial. [PLoS Med. 2012;9(6):e1001236](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1001236)

## March 2019
**Update to HIVDB phenotype queries:**
- added HIV2 phenotypes

## February 2019
**[Annotated dolutegravir (DTG) resistance reference library](/pages/refLib/DTG.html)**

**[HIVDB Algorithm version 8.8](/page/algorithm-updates/#version.8.8.update.2019-02-13)**
- Updated INSTI and NNRTI notes
- Updated Major HIV Drug Resistance Mutations [PDF handout](/assets/media/resistance-mutation-handout-feb2019.b0204a57.pdf)


