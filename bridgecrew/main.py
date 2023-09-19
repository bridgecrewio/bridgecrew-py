#!/usr/bin/env python
from bridgecrew.banner import banner, tool
from checkov.main import Checkov


def run():
    exit_code = Checkov().run(banner=banner, tool=tool)
    if exit_code:
        exit(exit_code)


if __name__ == "__main__":
    print("DEPRECATED: This project is no longer supported and will be archived end of 2023.")
    print("            Please use checkov instead, pip install checkov")
    run()
