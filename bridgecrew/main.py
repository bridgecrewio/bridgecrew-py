#!/usr/bin/env python

from checkov.main import run as checkov_run

from bridgecrew.banner import banner

def run():
    checkov_run(banner)


if __name__ == '__main__':
    run()
