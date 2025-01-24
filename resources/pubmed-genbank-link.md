## Introduction

This document outlines the methodology and results of creating and analyzing databases for three viruses: Crimean-Congo Hemorrhagic Fever Virus (CCHFV), Nipah Virus (NiV), and Lassa Virus (LASV). The database integrates GenBank sequence data and related publications to provide a comprehensive resource for researchers.

## How to create a Database

1. **Download GenBank file**: Retrieve all sequences for a specific virus from GenBank.
2. **Search PubMed**: Find all related literature for the virus, download PDFs, and extract relevant information (accession numbers, isolate country, isolate year, host and specimen) from the documents either manually or using AI.
3. **Generate the database**: Use this [tool](https://github.com/hivdb/GenBankRefs) to create the database using the files from steps 1 and 2.
4. **View the database**: Open and explore the database with [SQLite Viewer](https://inloop.github.io/sqlite-viewer).


## CCHFV

- [Download CCHFV Database](https://github.com/hivdb/GenBankRefs/releases/latest/download/CCHF.db)
- [Database Summary and Tables](/page/pgl-CCHF)

### Database Statistics

- **Number of GenBank Accessions**: 4,848
- **Number of GenBank Submission Sets**: 310
- **Non-Clinical Isolation Accessions**: 21
- **GenBank MetaData Gaps**:
  - Hosts: 280
  - Specimens: 2,195
  - Country: 182
  - Isolate Year: 96

- **Number of Publication from PubMed search**: 2114
- **Number of Publication included after Full Text Review**: 196

- **Number of Matched Submission Sets**: 198
- **Number of Matched Publications**: 169
- **Number of Submission Sets without Matched Publication**: 112
- **Number of Submission Sets supplemented by Publication Data**:
    - Host: 23 (Numseq 205)
    - Speciemens: 52 (Numseq 925)
    - Country: 9 (Numseq 52)
    - Isolate Year: 40 (Numseq 271)



### Related literatures

- Bente, D.A.; Forrester, N.L.; Watts, D.M.; McAuley, A.J.; Whitehouse, C.A.; Bray, M. Crimean-Congo Hemorrhagic Fever: History, Epidemiology, Pathogenesis, Clinical Syndrome and Genetic Diversity. Antiviral Research 2013, 100, 159–189, doi:10.1016/j.antiviral.2013.07.006.
- Carroll, S.A.; Bird, B.H.; Rollin, P.E.; Nichol, S.T. Ancient Common Ancestry of Crimean-Congo Hemorrhagic Fever Virus. Molecular Phylogenetics and Evolution 2010, 55, 1103–1110, doi:10.1016/j.ympev.2010.01.006.
- Lukashev, A.N.; Klimentov, A.S.; Smirnova, S.E.; Dzagurova, T.K.; Drexler, J.F.; Gmyl, A.P. Phylogeography of Crimean Congo Hemorrhagic Fever Virus. PLOS ONE 2016, 11, e0166744, doi:10.1371/journal.pone.0166744.


## Nipah

- [Download Nipah Database](https://github.com/hivdb/GenBankRefs/releases/latest/download/Nipah.db)
- [Database Summary and Tables](/page/pgl-Nipah)

### Database Statistics

- **Number of GenBank Accessions**: 407
- **Number of GenBank Submission Sets**: 61
- **Non-Clinical Isolation Accessions**: 40
- **GenBank MetaData Gaps**:
  - Hosts: 193
  - Specimens: 1,049
  - Country: 182
  - Isolate Year: 221

- **Number of Publication from PubMed search**: 1515
- **Number of Publication included after Full Text Review**: 33

- **Number of Matched Submission Sets**: 30
- **Number of Matched Publications**: 30
- **Number of Submission Sets without Matched Publication**: 31
- **Number of Submission Sets supplemented by Publication Data**:
    - Host: 9 (Numseq 12)
    - Speciemens: 19 (Numseq 81)
    - Country: 5 (Numseq 4)
    - Isolate Year: 11 (Numseq 32)

### Related literatures


-  de Campos, G.M.; Cella, E.; Kashima, S.; Alcântara, L.C.J.; Sampaio, S.C.; Elias, M.C.; Giovanetti, M.; Slavov, S.N. Updated Insights into the Phylogenetics, Phylodynamics, and Genetic Diversity of Nipah Virus (NiV). Viruses 2024, 16, 171, doi:10.3390/v16020171.
-  Hauser, N.; Gushiken, A.C.; Narayanan, S.; Kottilil, S.; Chua, J.V. Evolution of Nipah Virus Infection: Past, Present, and Future Considerations. Tropical Medicine and Infectious Disease 2021, 6, 24, doi:10.3390/tropicalmed6010024.
-  Lo Presti, A.; Cella, E.; Giovanetti, M.; Lai, A.; Angeletti, S.; Zehender, G.; Ciccozzi, M. Origin and Evolution of Nipah Virus. Journal of Medical Virology 2016, 88, 380–388, doi:10.1002/jmv.24345.



## LASV

- [Download LASV Database](https://github.com/hivdb/GenBankRefs/releases/latest/download/Lassa.db)
- [Database Summary and Tables](/page/pgl-Lassa)

### Database Statistics

- **Number of GenBank Accessions**: 2,780
- **Number of GenBank Submission Sets**: 103
- **Non-Clinical Isolation Accessions**: 47
- **GenBank MetaData Gaps**:
  - Hosts: 57
  - Specimens: 135
  - Country: 47
  - Isolate Year: 77

- **Number of Publication from PubMed search**: 1680
- **Number of Publication included after Full Text Review**: 66

- **Number of Matched Submission Sets**: 64
- **Number of Matched Publications**: 61
- **Number of Submission Sets without Matched Publication**: 39
- **Number of Submission Sets supplemented by Publication Data**:
    - Host: 16 (Numseq 126)
    - Speciemens: 18 (Numseq 833)
    - Country: 15 (Numseq 87)
    - Isolate Year: 15 (Numseq 132)

### Related literatures

-  Andersen, K.G.; Shapiro, B.J.; Matranga, C.B.; Sealfon, R.; Lin, A.E.; Moses, L.M.; Folarin, O.A.; Goba, A.; Odia, I.; Ehiane, P.E.; et al. Clinical Sequencing Uncovers Origins and Evolution of Lassa Virus. Cell 2015, 162, 738–750, doi:10.1016/j.cell.2015.07.020.
-  He, C.-Q.; Kong, C.; He, M.; Chen, G.-X.; Liu, S.-M.; Ding, N.-Z. Intrasegmental Recombination as an Evolutionary Force of Lassa Fever Virus. Front. Microbiol. 2024, 15, doi:10.3389/fmicb.2024.1411537.

