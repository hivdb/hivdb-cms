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

### GenBank

- \# accessions: 4806
- \# Submission Sets: 217
    - % with matched publication: 86% (186)
    - \# Matched by algorithm: 78

### Publication

- \# Publications reporting sequences: 218
    - % with matched GenBank submission set: 86% (188)


## Nipah

- [Download Nipah Database](https://github.com/hivdb/GenBankRefs/releases/latest/download/Nipah.db)
- [Database Overview: Tables, Matches, and Phylogenetic Insights](/page/pgl-Nipah)


### GenBank

- \# accessions: 362
- \# Submission Sets: 40
    - % with matched publication: 85% (34)
    - \# Matched by algorithm: 14


### Publication

- \# Publications reporting sequences: 37
    - % with matched GenBank submission set: 92% (34)


## LASV

- [Download LASV Database](https://github.com/hivdb/GenBankRefs/releases/latest/download/Lassa.db)
- [Database Overview: Tables, Matches, and Phylogenetic Insights](/page/pgl-Lassa)

### GenBank

- \# accessions: 2676
- \# Submission Sets: 88
    - % with matched publication: 77% (68)
    - \# Matched by algorithm: 24

### Publication

- \# Publications reporting sequences: 72
    - % with matched GenBank submission set: 92% (66)
