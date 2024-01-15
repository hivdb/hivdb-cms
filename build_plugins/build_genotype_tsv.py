import os
import csv
import json

from collections import OrderedDict


def iter_genotype_row(fp):
    rows = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(fp.read())
    for row in rows.values():
        cleaned = {
            'name': row['displayName'],
            'parentSubtype': ' + '.join(
                rows[n]['displayName']
                for n in (row['parentGenotypes'] or '').split('|')
                if n) or '-',
            'distanceUpperLimit':
            '{:.1f}%'.format(row['distanceUpperLimit'] * 100),
            'isSimpleCRF': row['isSimpleCRF'],
            'classificationLevel': row['classificationLevel']
        }

        if row['regions']:
            regions = ['{start}-{end}:{displayName}'
                       .format(displayName=rows
                               .get(r['genotypeName'], {})
                               .get('displayName', r['genotypeName']), **r)
                       for r in row['regions']]
            cleaned['breakPoints'] = '; '.join(regions)
        else:
            cleaned['breakPoints'] = '-'
        yield cleaned


def build_genotype_tsv(resource_dir, download_dir, **kw):
    infile = os.path.join(
        resource_dir, 'hivfacts-data', 'genotypes', 'genotypes_hiv1.json')
    outfile = os.path.join(
        download_dir, 'hiv-genotyper', 'genotype-properties.tsv')
    with open(infile) as infp, open(outfile, 'w') as outfp:
        writer = csv.DictWriter(
            outfp, ['name', 'parentSubtype', 'distanceUpperLimit',
                    'isSimpleCRF', 'classificationLevel', 'breakPoints'],
            delimiter='\t')
        writer.writeheader()
        for row in iter_genotype_row(infp):
            writer.writerow(row)
