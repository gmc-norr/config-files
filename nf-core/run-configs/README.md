# nf-core run configs

These are config files that should be loaded after the standard nf-core configs in order to be able to override certain defaults. This can be achieved in two ways:

1. Symlink the appropriate config to `nextflow.config` in the launch directory.
    ```
    # in the launch directory
    ln -s $CONFIG_FILES/nf-core/run-configs/<pipeline>.config nextflow.config
    nextflow run nf-core/<pipeline> [args ...]
    ```
2. Specify the config path in the nextflow command with `-c`.
    ```
    # in the launch directory
    nextflow run nf-core/<pipeline> -c $CONFIG_FILES/nf-core/run-configs/<pipeline>.config [args ...]
    ```
