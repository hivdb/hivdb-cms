## Introduction

This document outlines the methodology and results of creating and analyzing databases for three viruses: Crimean-Congo Hemorrhagic Fever Virus (CCHFV), Nipah Virus (NiV), and Lassa Virus (LASV). The database integrates GenBank sequence data and related publications to provide a comprehensive resource for researchers.

## How to create a Database

1. **Download GenBank file**: Retrieve all sequences for a specific virus from GenBank.
2. **Search PubMed**: Find all related literature for the virus, download PDFs, and extract relevant information (accession numbers, isolate country, isolate year, host and specimen) from the documents either manually or using AI.
3. **Generate the database**: Use this [tool](https://github.com/hivdb/GenBankRefs) to create the database using the files from steps 1 and 2.
4. **View the database**: Open and explore the database with [SQLite Viewer](https://inloop.github.io/sqlite-viewer).


## CCHFV

- [Download CCHFV Database](https://github.com/hivdb/GenBankRefs/releases/latest/download/CCHF.db)
- [Database Overview: Tables, Matches, and Phylogenetic Insights](/page/pgl-CCHF)

### Database Statistics

- **Total GenBank Submission Sets**: 225
- **GenBank Submission Sets After Filtering Out Non-Clinical and No-Gene Entries**: 217
- **Total Publications with Sequence Data**: 233

- **Number of Matched Submission Sets**: 184
- **Number of Matched Publications**: 184

- **GenBank Submission Sets without Matched Publication**: 33
- **Publications without Matched GenBank Submission**: 49

- **Number of Submission Sets & Publications Matched Manually (Excluding PMID Matches)**: 62


### Related literatures - Phylogenetic studies

- Bente, D.A.; Forrester, N.L.; Watts, D.M.; McAuley, A.J.; Whitehouse, C.A.; Bray, M. Crimean-Congo Hemorrhagic Fever: History, Epidemiology, Pathogenesis, Clinical Syndrome and Genetic Diversity. Antiviral Research 2013, 100, 159–189, doi:10.1016/j.antiviral.2013.07.006.
- Carroll, S.A.; Bird, B.H.; Rollin, P.E.; Nichol, S.T. Ancient Common Ancestry of Crimean-Congo Hemorrhagic Fever Virus. Molecular Phylogenetics and Evolution 2010, 55, 1103–1110, doi:10.1016/j.ympev.2010.01.006.
- Lukashev, A.N.; Klimentov, A.S.; Smirnova, S.E.; Dzagurova, T.K.; Drexler, J.F.; Gmyl, A.P. Phylogeography of Crimean Congo Hemorrhagic Fever Virus. PLOS ONE 2016, 11, e0166744, doi:10.1371/journal.pone.0166744.


## Nipah

- [Download Nipah Database](https://github.com/hivdb/GenBankRefs/releases/latest/download/Nipah.db)
- [Database Overview: Tables, Matches, and Phylogenetic Insights](/page/pgl-Nipah)

### Database Statistics

- **Total GenBank Submission Sets**: 53
- **GenBank Submission Sets After Filtering Out Non-Clinical and No-Gene Entries**: 45
- **Total Publications with Sequence Data**: 37

- **Number of Matched Submission Sets**: 34
- **Number of Matched Publications**: 34

- **Clinical GenBank Submission Sets without Matched Publication**: 11
- **Publications without Matched GenBank Submission**: 3

- **Number of Submission Sets & Publications Matched Manually (Excluding PMID Matches)**: 8


### Related literatures - Phylogenetic studies


-  de Campos, G.M.; Cella, E.; Kashima, S.; Alcântara, L.C.J.; Sampaio, S.C.; Elias, M.C.; Giovanetti, M.; Slavov, S.N. Updated Insights into the Phylogenetics, Phylodynamics, and Genetic Diversity of Nipah Virus (NiV). Viruses 2024, 16, 171, doi:10.3390/v16020171.
-  Hauser, N.; Gushiken, A.C.; Narayanan, S.; Kottilil, S.; Chua, J.V. Evolution of Nipah Virus Infection: Past, Present, and Future Considerations. Tropical Medicine and Infectious Disease 2021, 6, 24, doi:10.3390/tropicalmed6010024.
-  Lo Presti, A.; Cella, E.; Giovanetti, M.; Lai, A.; Angeletti, S.; Zehender, G.; Ciccozzi, M. Origin and Evolution of Nipah Virus. Journal of Medical Virology 2016, 88, 380–388, doi:10.1002/jmv.24345.



## LASV

- [Download LASV Database](https://github.com/hivdb/GenBankRefs/releases/latest/download/Lassa.db)
- [Database Overview: Tables, Matches, and Phylogenetic Insights](/page/pgl-Lassa)

### Database Statistics

- **Total GenBank Submission Sets**: 105
- **GenBank Submission Sets After Filtering Out Non-Clinical and No-Gene Entries**: 88
- **Total Publications with Sequence Data**: 72

- **Number of Matched Submission Sets**: 68
- **Number of Matched Publications**: 66

- **GenBank Submission Sets without Matched Publication**: 20
- **Publications without Matched GenBank Submission**: 6

- **Number of Submission Sets & Publications Matched Manually (Excluding PMID Matches)**: 24


### Related literatures - Phylogenetic studies

-  Andersen, K.G.; Shapiro, B.J.; Matranga, C.B.; Sealfon, R.; Lin, A.E.; Moses, L.M.; Folarin, O.A.; Goba, A.; Odia, I.; Ehiane, P.E.; et al. Clinical Sequencing Uncovers Origins and Evolution of Lassa Virus. Cell 2015, 162, 738–750, doi:10.1016/j.cell.2015.07.020.
-  He, C.-Q.; Kong, C.; He, M.; Chen, G.-X.; Liu, S.-M.; Ding, N.-Z. Intrasegmental Recombination as an Evolutionary Force of Lassa Fever Virus. Front. Microbiol. 2024, 15, doi:10.3389/fmicb.2024.1411537.

