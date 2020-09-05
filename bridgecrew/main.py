#!/usr/bin/env python
from checkov import main
from checkov.main import run as checkov_run
# Add BaseResourceCheck to support extending checks
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories
from bridgecrew.output.custom_runner_registry import CustomRunnerRegistry
from bridgecrew.banner import banner
from checkov.arm.runner import Runner as arm_runner
from checkov.cloudformation.runner import Runner as cfn_runner

from checkov.kubernetes.runner import Runner as k8_runner
from checkov.serverless.runner import Runner as sls_runner
from checkov.terraform.runner import Runner as tf_runner

def run():
    main.outer_registry = CustomRunnerRegistry(banner,None, tf_runner(), cfn_runner(), k8_runner(), sls_runner(),
                                                arm_runner())
    main.run(banner)


if __name__ == '__main__':
    run()
