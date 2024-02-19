import os
import json


def build_consensus_fasta(resource_dir: str, download_dir: str, **kw) -> None:
    infile = os.path.join(
        resource_dir, 'hivfacts-data', 'genes_hiv1.json')
    outdir = os.path.join(
        download_dir, 'hiv1-consensus')
    os.makedirs(outdir, exist_ok=True)
    with open(infile) as fp:
        data = json.load(fp)
    for gene in ('HIV1PR', 'HIV1RT', 'HIV1IN', 'HIV1CA'):
        outfile = os.path.join(outdir, gene + '.fas')
        genedata = [one for one in data if one['name'] == gene][0]
        with open(outfile, 'w') as outfp:
            outfp.write(
                '>ConsensusB|{name}\n{refSequence}\n'.format(**genedata))
