# Small configuration files for GMC Norr

Inspired by [Clinical-Genomics/reference-files](https://github.com/Clinical-Genomics/reference-files).

## nf-core/raredisease

To run the raredisease pipeline in a clinical setting on our cluster, run the following commands:

```bash
nextflow run nf-core/raredisease \
    -c $NFCORE_CONFIG_HOME/raredisease/raredisease.config \
    --params-file $NFCORE_CONFIG_HOME/raredisease/params.yaml \
    -profile rv,clinical \
    --analysis_type wgs
```

`$NFCORE_CONFIG_FILES` is the path to the `nf-core` directory in a clone of this repo. The `rv` (Region Västerbotten) profile is the general cluster config for nf-core and should be used for all nf-core pipelines. For this config there are also two additional profiles: `clinical` and `research`. These are also general, and will decide what priority the jobs will get on the cluster.

There are three types of analyses that can be run: `wgs` (whole genome), `wes` (whole exome) and `mito` (mitochondrial), and this is set with `--analysis_type`. This will partly decide what software to use and what resources they will need. The default value for this is `wgs`.

A parameter that can be useful in case of failed or otherwise interrupted runs is the `-resume` flag. This will attempt to resume the execution and make use of alredy generated results.

The samplesheet used for the input data is *not* an Illumina samplesheet. See the [nf-core/raredisease documentation](https://nf-co.re/raredisease/2.2.0/docs/usage#samplesheet) for details.

## Environment variables

These are environment variables that are recommended (and in some cases required):

- `GMCNORR_CONFIG_HOME`: should point to a clone of this repo.
- `NFCORE_CONFIG_HOME`: should point to the `nf-core` directory in this repo.
- `HYDRA_CONFIG_HOME`: should point to the `hydra-genetics` directory in this repo.
