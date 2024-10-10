# nf-core pipeline configuration

The structure for nf-core configuration files is as follows:

- Files in the `nf-core` directory should define profiles.
- Each directory in the `nf-core` directory (apart from the `assets` directory) should have the name of an nf-core pipeline. These directories should contain:
    - A `<pipeline>.config` file which is a Nextflow config file containing any process directives, or parameters that need to access parameter variables and/or environment variables.
    - An optional `params.yaml` file which contains parameters that do *not* need access to variables and/or environment variables.

The file `<pipeline.config>` must exist, and it should at the very least pull in the relevant profile config from the `nf-core` diretory. See [`raredisease/raredisease.config`](raredisease/raredisease.config) for an example.

In most cases, any parameters defined in `params.yaml` could go into the `<pipeline>.config` files, but there are exceptions. For example, if the pipeline defines a parameter that then is used as a part of other parameters, defining this in `<pipeline>.config` might yield unexpected results. One example of this is `igenomes_base` which is used by some nf-core pipelines. Defining this in `<pipeline>.config` will override it, but the paths defined using the original value will not. Therefore this has to be defined in `params.yaml`.

The `assets` directory should contain small reference files that could possibly be shared between pipelines. The sizes of these files should be suitable for a git repository. If a file is larger than half a megabyte, then consider having this in a reference repository on the system and refer to this path instead.
