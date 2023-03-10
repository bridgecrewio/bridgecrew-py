from __future__ import annotations

from checkov.common.runners.runner_registry import RunnerRegistry

from bridgecrew.banner import tool

class BridgecrewRunnerRegistry(RunnerRegistry):
    def __init__(self, banner, runner_filter, *runners):
        super().__init__(banner, runner_filter, *runners)
        self.tool = tool
