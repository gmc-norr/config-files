#!/usr/bin/env python3

"""
This script performs a simple validation of a snakemake profile.
The following checks are performed:

- The profile path exists
- The profile config file exists
- The snakefile is specified
    - The snakefile exists on the system
- The configfiles are specified
    - The config files listed exist on the system
- Resources are specified
    - The resource config file exists
- Singularity args are set
- Singularity prefix is set
"""

import argparse
import os
import sys
from enum import Enum
from pathlib import Path
from typing import Union

import yaml


class ValidationStatus(Enum):
    OK = "success"
    WARNING = "warning"
    ERROR = "error"


def validate_singularity_args(
    singularity_args: str,
) -> list[tuple[ValidationStatus, str]]:
    if not singularity_args:
        return [(ValidationStatus.ERROR, "singularity args not specified")]

    validations = []

    if "--cleanenv" not in singularity_args:
        validations.append(
            (ValidationStatus.ERROR, "singularity args must include --cleanenv")
        )

    p = argparse.ArgumentParser()
    p.add_argument("-B", "--bind", action="append")
    p.add_argument("-e", "--cleanenv", action="store_true")
    args = p.parse_args(singularity_args.split())

    # check binds
    for b in args.bind:
        binds = b.split(",")
        for bind in binds:
            bind_path = Path(os.path.expandvars(bind.split(":")[0]))
            if not bind_path.exists():
                validations.append(
                    (ValidationStatus.WARNING, f"apptainer bind path does not exist: {bind_path}")
                )
            if not bind_path.is_absolute():
                validations.append(
                    (ValidationStatus.ERROR, f"apptainer bind path must be absolute: {bind_path}")
                )

    return validations


def validate_profile_config(
    profile_config: Union[str, Path]
) -> list[tuple[ValidationStatus, str]]:
    profile_config = Path(profile_config)

    if not profile_config.exists():
        return [
            (ValidationStatus.ERROR, f"config file does not exist: {profile_config}")
        ]

    cfg = yaml.safe_load(profile_config.read_text())

    validations = []

    if "snakefile" not in cfg:
        validations.append(
            (ValidationStatus.ERROR, "snakefile not found in config file")
        )
    elif not Path(cfg["snakefile"]).exists():
        validations.append(
            (ValidationStatus.ERROR, f"snakefile does not exist: {cfg['snakefile']}")
        )

    if "configfiles" not in cfg:
        validations.append(
            (ValidationStatus.ERROR, "configfiles not found in config file")
        )
    elif not type(cfg["configfiles"]) is list:
        validations.append((ValidationStatus.ERROR, "configfiles is not an array"))

    for configfile in cfg["configfiles"]:
        configfile = Path(configfile)
        if not configfile.exists():
            validations.append(
                (ValidationStatus.ERROR, f"configfile does not exist: {configfile}")
            )

    found_resources = False
    if "config" not in cfg:
        validations.append((ValidationStatus.ERROR, "config not found in config file"))
    elif not type(cfg["config"]) is list:
        validations.append((ValidationStatus.ERROR, "config is not an array"))
    else:
        for config in cfg["config"]:
            name, value = config.split("=")
            if name == "resources":
                found_resources = True
                if not Path(value).exists():
                    validations.append(
                        (
                            ValidationStatus.ERROR,
                            f"resource config does not exist: {value}",
                        )
                    )

    if not found_resources:
        validations.append(
            (ValidationStatus.WARNING, "resources not found under config")
        )

    if "singularity-args" not in cfg:
        validations.append(
            (ValidationStatus.ERROR, "singularity-args not found in config file")
        )
    else:
        arg_validations = validate_singularity_args(cfg["singularity-args"])
        validations.extend(arg_validations)

    if "singularity-prefix" not in cfg:
        validations.append(
            (ValidationStatus.ERROR, "singularity-prefix not found in config file")
        )
    else:
        if not Path(cfg["singularity-prefix"]).exists():
            validations.append(
                (
                    ValidationStatus.ERROR,
                    f"singularity cache dir does not exist: {cfg['singularity-prefix']}",
                )
            )

    return validations


def validate_profile(
    profile_path: Union[str, Path]
) -> list[tuple[ValidationStatus, str]]:
    profile_path = Path(profile_path)

    if not profile_path.exists():
        return [(ValidationStatus.ERROR, f"profile path not found: {profile_path}")]

    profile_config = profile_path / "config.yaml"
    return validate_profile_config(profile_config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Validates a Snakemake profile.
        The validation is very much directed towards our use at GMC Norr, and
        not a general purpose tool for validating Snakemake profiles."""
    )
    parser.add_argument("profile", help="path to the profile to validate")
    args = parser.parse_args()

    any_error = False
    any_warning = False
    for status, message in validate_profile(args.profile):
        if status == ValidationStatus.ERROR:
            any_error = True
        if status == ValidationStatus.WARNING:
            any_warning = True
        print(f"{status.value}: {message}")

    if any_error:
        print("Profile validation failed")
        sys.exit(1)
    elif any_warning:
        print("Profile validation succeeded with warnings")
    else:
        print("Profile validation succeeded")
