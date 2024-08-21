# Small configuration files for GMC Norr

Inspired by [Clinical-Genomics/reference-files](https://github.com/Clinical-Genomics/reference-files).

## nf-core/raredisease

To run the raredisease pipeline in a clinical setting on our cluster, run the following commands:

```bash
ln -s ${GMCNORR_CONFIG_FILES}/nf-core/run-configs/raredisease.config nextflow.config
nextflow run nf-core/raredisease \
    --custom_config_base ${GMCNORR_CONFIG_FILES}/nf-core \
    -profile rv,clinical \
    --analysis_type wgs
```

`$GMCNORR_CONFIG_FILES` is the path to the clone of this repo. The `rv` (Region Västerbotten) profile is the general cluster config for nf-core and should be used for all nf-core pipelines. For this config there are also two additional profiles: `clinical` and `research`. These are also general, and will decide what priority the jobs will get on the cluster.

There are three types of analyses that can be run: `wgs` (whole genome), `wes` (whole exome) and `mito` (mitochondrial), and this is set with `--analysis_type`. This will partly decide what software to use and what resources they will need.

The samplesheet used for the input data is *not* an Illumina samplesheet. See the [nf-core/raredisease documentation](https://nf-co.re/raredisease/2.1.0/docs/usage#samplesheet) for details.
