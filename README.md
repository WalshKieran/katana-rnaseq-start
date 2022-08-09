# nf-core RNASeq Steps

> RNA sequencing analysis pipeline using STAR, RSEM, HISAT2 or Salmon with gene/isoform counts and extensive quality control.

## Using Nextflow on Katana

By default, we use Ensembl GRCh37. See [here](https://github.com/nf-core/rnaseq/blob/master/conf/igenomes.config) for alternatives, major human and mouse assemblies are installed on Katana. For guidance on modifying [nf-params.json](nf-params.json), see [the official documentation](https://nf-co.re/rnaseq/usage), which includes an interface to generate new params files.

1. Create a new project folder:
```bash
mkdir -p "/srv/scratch/genomicwf/$USER/<your-project-name>" && cd "$_"
git clone https://github.com/WalshKieran/rnaseq-run.git .
```
2. Download your data (optional):
if you have a curl command from Ramaciotti, call it here and note the folder name for the next step.

3. Create your samplesheet: a simple script is provided to convert any folder containing [illumina naming convention](https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/NamingConvention_FASTQ-files-swBS.htm) fastqs to a samplesheet, but it is [straightforward](https://nf-co.re/rnaseq/usage#samplesheet-input) to create one manually:
```bash
python3 ramac_to_samplesheet.py "<your/data/folder>" > samplesheet.csv
head samplesheet.csv # verify non-empty, update sample names
```

4. Submit batch job to Katana (and note the returned number):
```bash
qsub run.pbs
```
To check on a running Katana workflow, use `qstat -u $USER` and `cat .nextflow.log`. To stop it and all associated jobs, run `qdel <number returned by qsub>`. Results will be in ./results and resume is enabled by default.

5. Move your results out of temporary folder. Consider deleting your temporary project folder if you are done.
```bash
mv "/srv/scratch/genomicwf/$USER/<your-project-name>/results/* /srv/scratch/$USER/<your-project-name>"
#rm -r "/srv/scratch/genomicwf/$USER/<your-project-name>"
```

> **Note**
> The default resource allocations for nf-core are extremely generous and these instructions typically create hundreds of jobs.
> This may impact your Katana priority.

> **Warning**
> Anything stored in the temporary directory /srv/scratch/genomicwf may be cleared after 2 days. Nextflow can generate over 300GB of ./work files, this directory gives you the option to fix parameters and resume. If your lab has access to more storage, feel free to use that instead.

- [x] Downloaded iGenomes subset
- [x] Test with various datasets
- [ ] Push finalized Katana config to [nf-core](https://github.com/nf-core/configs)
- [ ] Push finalized documentation to unsw-restech.github.io
