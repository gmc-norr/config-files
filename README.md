# Small configuration files for GMC Norr

Inspired by [Clinical-Genomics/reference-files](https://github.com/Clinical-Genomics/reference-files).

## nf-core/raredisease

To run the raredisease pipeline in a clinical setting on our cluster, run the following command:

```bash
nextflow \
    run \
    -c $NEXTFLOW_CONFIG_HOME/nf-core/raredisease/raredisease.config \
    -c $NEXTFLOW_CONFIG_HOME/nf-core/rv.config \
    -params-file $NEXTFLOW_CONFIG_HOME/nf-core/raredisease/params.yaml \
    -profile clinical \
    nf-core/raredisease
```

`$NEXTFLOW_CONFIG_HOME` is the path to the `nextflow` directory in a clone of this repo. The `rv` (Region Västerbotten) profile is the general cluster config for nf-core and should be used for all nf-core pipelines. For this config there are also two additional profiles: `clinical` and `research`. These are also general, and will decide what priority the jobs will get on the cluster.

There are three types of analyses that can be run: `wgs` (whole genome), `wes` (whole exome) and `mito` (mitochondrial), and this is set with `--analysis_type`. This will partly decide what software to use and what resources they will need. The default value for this is `wgs`.

A parameter that can be useful in case of failed or otherwise interrupted runs is the `-resume` flag. This will attempt to resume the execution and make use of alredy generated results.

The samplesheet used for the input data is *not* an Illumina samplesheet. See the [nf-core/raredisease documentation](https://nf-co.re/raredisease/2.2.0/docs/usage#samplesheet) for details.

## genomic-medicine-sweden/Twist_Solid

To run Twist Solid in a clinical setting, run the following command:

```bash
snakemake \
    -s $PLUMBER_PIPELINE_HOME/workflow/Snakefile \
    --profile $PLUMBER_PIPELINE_CONFIG/profiles/slurm \
    --configfiles $PLUMBER_PIPELINE_HOME/config/config.yaml \
        $PLUMBER_PIPELINE_HOME/config/config.data.hg19.yaml \
        $PLUMBER_CONFIG_HOME/configs/config.hg19.yaml \
        $PLUMBER_CONFIG_HOME/configs/resources.clinical.yaml \
    --config \
        PROJECT_DESIGN_DATA=$PLUMBER_REFERENCE_DATA \
        PROJECT_PON_DATA=$PLUMBER_REFERENCE_DATA \
        PROJECT_REF_DATA=$PLUMBER_REFERENCE_DATA \
        PLUMBER_PIPELINE_CONFIG=$PLUMBER_PIPELINE_CONFIG \
        PLUMBER_PIPELINE_HOME=$PLUMBER_PIPELINE_HOME
```

See below for the definition of the different environment variables used. This assumes that the required files `samples.tsv` and `units.tsv` have already been generated and exist in the working directory.

## Environment variables

These are environment variables that are recommended (and in some cases required):

- `GMCNORR_CONFIG_HOME`: should point to a clone of this repo.
- `NEXTFLOW_CONFIG_HOME`: should point to the `nextflow` directory in this repo.
- `HYDRA_CONFIG_HOME`: should point to the `hydra-genetics` directory in this repo.
- `PLUMBER_PIPELINE_HOME`: should point to local path of the pipeline repo (is set when using plumber).
- `PLUMBER_PIPELINE_CONFIG`: should point to the local path of the pipeline config (is set when using plumber). 
- `PLUMBER_REFERENCE_DATA`: should point to the directory containing all required reference files required for the pipeline.
- `PLUMBER_ASSETS_PATH`: should point to the assets directory of the local pipeline config.

## Plumber integration

This repo is configured to work with [plumber](https://github.com/gmc-norr/plumber).
In order to make a pipeline configuration available in plumber, it has to be added to the plumberfile `plumber.yaml`.
See the [plumberfile schema](https://github.com/gmc-norr/plumber/blob/main/schema/plumber-v1.schema.json) for more information.
It is also possible to use plumber to validate the plumberfile.

Due to plumber rearranging the config files to some extent, it needs to be able to control file paths in any config files that refer to files within this repo.
This can be seen in action in the [config for nf-core/raredisease](./nextflow/nf-core/raredisease/raredisease.config).
Since this approach has yet to be extensively tested, it might be subject to change.

To run the same example that is presented at the beginning of this document, run the command:

```bash
plumber nextflow run -p clinical nf-core/raredisease
```

Configs and assets will be downloaded automatically, and the appropriate environment variables will be set.
