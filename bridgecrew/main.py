#!/usr/bin/env python

from checkov.main import run as checkov_run
# Add BaseResourceCheck to support extending checks
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

from bridgecrew.banner import banner


def run():
    checkov_run(banner)


if __name__ == '__main__':
    run()
