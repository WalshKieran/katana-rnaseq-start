#!/usr/bin/env python3

import sys, os

#Given an illumina directory, parses into a nf-core csv samplesheet printed to stdout

if len(sys.argv) < 2:
    print("Usage: ramac_to_samplesheet path/to/root", file=sys.stderr)
    exit(1)

print('sample,fastq_1,fastq_2,strandedness')

for root, dirs, files in os.walk(sys.argv[1]):
    dirs.sort()
    for file in sorted(files):
        if file.endswith("_R1_001.fastq.gz"):
            r1 = os.path.join(root, file)
            r2 = os.path.join(root, r1.replace("_R1_", "_R2_"))

            sampleName = r1.rsplit('_', 4)[0].rsplit('/', 1)[-1]

            if not os.path.exists(r2): r2 = ""
            print(f'{sampleName},{r1},{r2},reverse')
