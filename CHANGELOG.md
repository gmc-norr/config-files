# Changelog

## [0.3.0](https://github.com/gmc-norr/config-files/compare/v0.2.0...v0.3.0) (2025-02-21)

### Supported pipelines

#### Nextflow:

- nf-core/raredisease 2.3.0

#### hydra-genetics:

- genomic-medicine-sweden/Twist_Solid 0.13.0, 0.14.0

### Features

* update nf-core/raredisease to 2.3.0 ([#23](https://github.com/gmc-norr/config-files/issues/23)) ([a2d3479](https://github.com/gmc-norr/config-files/commit/a2d34795fa7d6cef77f563f72a075933adc821ae))

## [0.2.0](https://github.com/gmc-norr/config-files/compare/v0.1.0...v0.2.0) (2025-02-17)


### Features

* add plumberfile ([#19](https://github.com/gmc-norr/config-files/issues/19)) ([90c6b0a](https://github.com/gmc-norr/config-files/commit/90c6b0adedd9331e6cd9c8dbfd39916a895baada))


### Bug Fixes

* **hydra-genetics:** don't specify nodelist, rely on partition instead ([#22](https://github.com/gmc-norr/config-files/issues/22)) ([45ca959](https://github.com/gmc-norr/config-files/commit/45ca9593d2eea446753a2b9885c57a86b23679e1))

## 0.1.0 (2024-10-11)

First release of config-files.

### Supported pipelines

**Nextflow:**
- nf-core/raredisease 2.2.0

**hydra-genetics:**
- genomic-medicine-sweden/Twist_Solid 0.13.0, 0.14.0

### Features

* add config and profile for Twist Solid v0.14.0 ([#10](https://github.com/gmc-norr/config-files/issues/10)) ([d38677f](https://github.com/gmc-norr/config-files/commit/d38677f1cf69c3494b908a86a98a4ce95ba7c1f2))
* add configuration files for nf-core/raredisease ([#9](https://github.com/gmc-norr/config-files/issues/9)) ([a9dd52a](https://github.com/gmc-norr/config-files/commit/a9dd52a0d04e8c76580a5ebea6e9a54a3237807e))
* add twist-solid-0.13.0 slurm profile ([#5](https://github.com/gmc-norr/config-files/issues/5)) ([fff0b9d](https://github.com/gmc-norr/config-files/commit/fff0b9dff22b935ebdd05fa6c343fa855981fc3a))
* add validation script for Snakemake profiles ([d9382b6](https://github.com/gmc-norr/config-files/commit/d9382b6ced85bb3833d0398bad95a510f5edd969))
* organisation support for Nextflow pipelines ([#15](https://github.com/gmc-norr/config-files/issues/15)) ([b7a8f67](https://github.com/gmc-norr/config-files/commit/b7a8f674f3bf07951270315adb51c23d2bd4d734))
* poppy dev config ([#1](https://github.com/gmc-norr/config-files/issues/1)) ([ce3f9d4](https://github.com/gmc-norr/config-files/commit/ce3f9d444a0c4073ff02a27c2f85e3a4700e4e23))
* remove Twist Solid config files for versions &lt;0.13.0 ([d9382b6](https://github.com/gmc-norr/config-files/commit/d9382b6ced85bb3833d0398bad95a510f5edd969))
* twist solid v0.9.0 config ([#2](https://github.com/gmc-norr/config-files/issues/2)) ([bb4295d](https://github.com/gmc-norr/config-files/commit/bb4295d07828a4a5377593b7291fcb4d7de689f4))
* update reports module in poppy ([#3](https://github.com/gmc-norr/config-files/issues/3)) ([d0b27c1](https://github.com/gmc-norr/config-files/commit/d0b27c1bcaffbe629864bd7bc7b704027d096205))
* update reports module in poppy ([#4](https://github.com/gmc-norr/config-files/issues/4)) ([f52cf21](https://github.com/gmc-norr/config-files/commit/f52cf21dd9938b0f69f6a891021b5d6a8b89d668))


### Bug Fixes

* increase research timelimit for fuseq_wes ([#12](https://github.com/gmc-norr/config-files/issues/12)) ([1a51429](https://github.com/gmc-norr/config-files/commit/1a5142955500d7bfdd5890f6691f9c835ca9889e))
* increase time limit for FuSeq_WES ([#7](https://github.com/gmc-norr/config-files/issues/7)) ([7926911](https://github.com/gmc-norr/config-files/commit/7926911115a9d0ff45ed58c344313aab6e8a261c))
* increase timelimit for fuseq_wes ([#11](https://github.com/gmc-norr/config-files/issues/11)) ([737e21b](https://github.com/gmc-norr/config-files/commit/737e21bebbaab56fb55ededb590daf439010e681))
* increse fuseq_wes timelimit even more ([#13](https://github.com/gmc-norr/config-files/issues/13)) ([654ed90](https://github.com/gmc-norr/config-files/commit/654ed90a8506cdb201cdca3ae6e5b5ced387f138))
* more defensive check of slurm status ([#8](https://github.com/gmc-norr/config-files/issues/8)) ([208abcf](https://github.com/gmc-norr/config-files/commit/208abcf01d254270c50b0b2a2f31c4b77c6b61e0))


### Miscellaneous Chores

* release 0.1.0 ([#18](https://github.com/gmc-norr/config-files/issues/18)) ([e888c7e](https://github.com/gmc-norr/config-files/commit/e888c7ebc181f5a459cf928076710666cd369ba4))
