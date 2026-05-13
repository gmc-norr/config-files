# Changelog

## [0.6.1](https://github.com/gmc-norr/config-files/compare/v0.6.0...v0.6.1) (2026-05-13)


### Bug Fixes

* bump resources for fuseq_wes and add_mosdepth_coverage_to_gvcf  ([#53](https://github.com/gmc-norr/config-files/issues/53)) ([e3e805f](https://github.com/gmc-norr/config-files/commit/e3e805fa2c700c2cb87af0f3b8b64d3d5bb7ef1c))
* bump resources for fuseq_wes and add_mosdepth_coverage_to_gvcf for the gms-solid pipeline ([e3e805f](https://github.com/gmc-norr/config-files/commit/e3e805fa2c700c2cb87af0f3b8b64d3d5bb7ef1c))

## [0.6.0](https://github.com/gmc-norr/config-files/compare/v0.5.1...v0.6.0) (2026-04-30)


### ⚠ BREAKING CHANGES

* **scout-annotation:** add new scout-annotation config ([#48](https://github.com/gmc-norr/config-files/issues/48))

### Features

* add test profile configs for rare-disease ([#38](https://github.com/gmc-norr/config-files/issues/38)) ([1f3111d](https://github.com/gmc-norr/config-files/commit/1f3111ded901229761cb7d34568a1b978858c565))
* **nf-core/raredisease:** add SV support ([#49](https://github.com/gmc-norr/config-files/issues/49)) ([fa3b6f7](https://github.com/gmc-norr/config-files/commit/fa3b6f710d49f1412c1245ab45f794d6473d2b3e))
* **scout-annotation:** add new scout-annotation config ([#48](https://github.com/gmc-norr/config-files/issues/48)) ([3bd2b4a](https://github.com/gmc-norr/config-files/commit/3bd2b4a8d4311b835d4272fc94ffe778f4e5e9e7))


### Bug Fixes

* bind /seqdata in twist solid profile ([#44](https://github.com/gmc-norr/config-files/issues/44)) ([f179555](https://github.com/gmc-norr/config-files/commit/f179555e6e5927eab3d7947aeff725fbb94b4eea))
* don't attempt to restart failed jobs ([dc1788c](https://github.com/gmc-norr/config-files/commit/dc1788c6cbbc83e62040c334c41a292e59fbe36f))
* increase memory allocation for juli ([#42](https://github.com/gmc-norr/config-files/issues/42)) ([ec483fe](https://github.com/gmc-norr/config-files/commit/ec483fef582488040472a2459b48c1d06897cdf8))
* increase memory allocation for juli_call ([d729142](https://github.com/gmc-norr/config-files/commit/d7291429691ee8b7f22c2d250d7735d0efd04aa0))
* increase time and memory allocation for optitype ([ede2348](https://github.com/gmc-norr/config-files/commit/ede2348f570aca014afaec1bc3093c79d01db527))
* set correct version for scout-annotation in paths ([#50](https://github.com/gmc-norr/config-files/issues/50)) ([e6a5a89](https://github.com/gmc-norr/config-files/commit/e6a5a89b3ab47ee71fd4381a56cfbd5d7efd9523))
* **twist-solid:** bump resources ([#51](https://github.com/gmc-norr/config-files/issues/51)) ([133c68d](https://github.com/gmc-norr/config-files/commit/133c68d798ef7f2b2bc06b5b83e08e1a3d793f10))

## [0.5.1](https://github.com/gmc-norr/config-files/compare/v0.5.0...v0.5.1) (2025-10-30)


### Bug Fixes

* **Twist Solid:** adjust resources to avoid OOM kills ([#31](https://github.com/gmc-norr/config-files/issues/31)) ([fbf8120](https://github.com/gmc-norr/config-files/commit/fbf81203b37c4ba231b5c87e4d414dca284eacf5))

## [0.5.0](https://github.com/gmc-norr/config-files/compare/v0.4.0...v0.5.0) (2025-09-30)


### Features

* add config for Twist Solid v0.23.0 ([#28](https://github.com/gmc-norr/config-files/issues/28)) ([cb20282](https://github.com/gmc-norr/config-files/commit/cb202821b382d9dc773a504d7cef0c95980a78d6))

## [0.4.0](https://github.com/gmc-norr/config-files/compare/v0.3.0...v0.4.0) (2025-02-27)

### Supported pipelines

#### Nextflow:

- nf-core/raredisease 2.4.0

#### hydra-genetics:

- genomic-medicine-sweden/Twist_Solid 0.13.0, 0.14.0

### Features

* update nf-core/raredisease to 2.4.0 ([#25](https://github.com/gmc-norr/config-files/issues/25)) ([4d6874a](https://github.com/gmc-norr/config-files/commit/4d6874ab3b255efdbc94e4e1e4ef16cf928399dd))

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
