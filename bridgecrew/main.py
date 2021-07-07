#!/usr/bin/env python
from checkov import main
from checkov.main import run as checkov_run
# Add BaseResourceCheck to support extending checks
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories
from bridgecrew.output.custom_runner_registry import CustomRunnerRegistry
from bridgecrew.banner import banner
from checkov.main import DEFAULT_RUNNERS


def run():
    main.outer_registry = CustomRunnerRegistry(banner,None, *DEFAULT_RUNNERS)
    exit_code = main.run(banner)
    if exit_code:
        exit(exit_code)


if __name__ == '__main__':
    run()
