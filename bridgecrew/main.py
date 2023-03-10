#!/usr/bin/env python
from checkov import main
# Add BaseResourceCheck to support extending checks
from bridgecrew.output.custom_runner_registry import BridgecrewRunnerRegistry
from bridgecrew.banner import banner
from checkov.main import DEFAULT_RUNNERS, Checkov


def run():
    main.outer_registry = BridgecrewRunnerRegistry(banner, None, *DEFAULT_RUNNERS)
    exit_code = Checkov().run(banner=banner)
    if exit_code:
        exit(exit_code)


if __name__ == '__main__':
    run()
