# Getting Started with nf-core/rnaseq on Katana

RNA sequencing analysis pipeline using STAR, RSEM, HISAT2 or Salmon with gene/isoform counts and extensive quality control.

## Using Nextflow on Katana

Nextflow is a workflow manager that can be configured to submit jobs to a cluster, in this case OpenPBS. By default, we use the latest Ensembl reference/annotation. For guidance on modifying [nf-params.json](nf-params.json) including the genome, see [the official documentation](https://nf-co.re/rnaseq/usage), which includes an interface to generate new params files.

> [!NOTE] 
> The default resource allocations for nf-core are extremely generous and these instructions typically create hundreds of jobs.
> This may impact your Katana priority. Consider using [nf-optimizer](https://github.com/WalshKieran/nf-optimizer).
> I am mentioning this at the start because it would require exporting an additonal environment variable in run.pbs.

1. Create a new project folder (if you have sufficient lab scratch or are a non-BABS user, use that instead):
```bash
mkdir -p "/srv/scratch/seqflow/$USER/<your-project-name>" && cd "$_"
git clone https://github.com/WalshKieran/katana-rnaseq-start.git .
```
2. Download your data (optional):
if you have a curl command from Ramaciotti, call it here and note the folder name for the next step.

3. Create your samplesheet: The only required inputs for nf-core/rnaseq are a samplesheet of fastq files, a genome, and an annotation. Creating the samplesheet automatically via script is simple since Ramaciotti outputs usually follow the [illumina naming convention](https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/NamingConvention_FASTQ-files-swBS.htm), but you can also manually define file endings using e.g. '-r1 _1.fastq.gz -r2 _2.fastq.gz'. Strandedness can be determined automatically, set it manually using e.g. '-st reverse'.
```bash
wget https://raw.githubusercontent.com/nf-core/rnaseq/master/bin/fastq_dir_to_samplesheet.py
python3 fastq_dir_to_samplesheet.py --recursive "</srv/scratch/your/data>" ./samplesheet.csv
```

4. Submit batch job to Katana (and note the returned number):
```bash
qsub run.pbs
```
To check on a running Katana workflow, use `qstat -u $USER` and `cat .nextflow.log`. To stop it and all associated jobs, run `qdel <number returned by qsub>`. Results will be in ./results and resume is enabled by default.

5. Move your results out of temporary folder. Consider deleting your temporary project folder if you are done.
```bash
mv "/srv/scratch/seqflow/$USER/<your-project-name>/results/* /srv/scratch/$USER/<your-project-name>"
#rm -r "/srv/scratch/seqflow/$USER/<your-project-name>"
```

> [!WARNING] 
> Anything stored in the temporary directory /srv/scratch/seqflow may be cleared after 3 days. Nextflow can generate over 300GB of ./work files, this directory gives you the option to fix parameters and resume. If your lab has access to more storage, feel free to use that instead.

- [x] Downloaded iGenomes subset
- [x] Test with various datasets
- [ ] Integrate with default [Katana](https://docs.restech.unsw.edu.au) modules
- [ ] Push finalized Katana config to [nf-core](https://github.com/nf-core/configs)
