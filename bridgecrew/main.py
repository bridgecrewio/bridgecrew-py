#!/usr/bin/env python
from bridgecrew.banner import banner, tool
from checkov.main import Checkov


def run():
    exit_code = Checkov().run(banner=banner, tool=tool)
    if exit_code:
        exit(exit_code)


if __name__ == "__main__":
    run()
