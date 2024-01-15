import os
import json


def iter_references(fp, genotypes):
    rows = json.load(fp)
    for row in rows:
        idxname = row.pop('genotypeName')
        if 'year' not in row:
            row['year'] = None
        yield (
            '>{accession}|{genotypeName}|HXB2{firstNA}-{lastNA}'
            '|year:{year}|country:{country}|author:{authorYear}\n'
            '{sequence}\n'
            .format(
                genotypeName=genotypes[idxname]['displayName'],
                **row
            )
        )


def build_genotype_reference_fasta(resource_dir, download_dir, **kw):
    infile = os.path.join(
        resource_dir, 'hivfacts-data',
        'genotypes', 'genotype-references_hiv1.json')
    typefile = os.path.join(
        resource_dir, 'hivfacts-data', 'genotypes', 'genotypes_hiv1.json')
    outfile = os.path.join(
        download_dir, 'hiv-genotyper', 'genotype-references.fasta')
    with open(infile) as infp, \
            open(typefile) as typefp, \
            open(outfile, 'w') as outfp:
        for one in iter_references(infp, json.load(typefp)):
            outfp.write(one)
