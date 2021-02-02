import json
from checkov.common.output.report import Report
from checkov.common.runners.runner_registry import RunnerRegistry, OUTPUT_CHOICES

from bridgecrew.output.sarif import SarifReport


class CustomRunnerRegistry(RunnerRegistry):
    def __init__(self, banner, runner_filter, *runners):
        super().__init__(banner, runner_filter, *runners)
        OUTPUT_CHOICES.append("sarif")

    def print_reports(self, scan_reports, args, url = None):
        if args.output not in OUTPUT_CHOICES:
            print(f"{self.banner}\n")
        exit_codes = []
        report_jsons = []
        merged_reports = self.merge_reports(scan_reports)
        if args.output == 'sarif':
            report = self.report2sarif_report(merged_reports, args)
            report.print_sarif()
            if url:
                print("More details: {}".format(url))
        else:
            for report in scan_reports:
                if not report.is_empty():
                    if args.output == "json":
                        report_jsons.append(report.get_dict())
                    elif args.output == "junitxml":
                        report.print_junit_xml()
                    elif args.output == 'github_failed_only':
                        report.print_failed_github_md()
                    elif args.output == 'sarif':
                        report = self.report2sarif_report(report, args)
                        report.print_sarif()
                        if url:
                            print("More details: {}".format(url))
                    else:
                        report.print_console(is_quiet=args.quiet)
                        if url:
                            print("More details: {}".format(url))
                exit_codes.append(report.get_exit_code(args.soft_fail))
        if args.output == "json":
            if len(report_jsons) == 1:
                print(json.dumps(report_jsons[0], indent=4))
            else:
                print(json.dumps(report_jsons, indent=4))
        exit_code = 1 if 1 in exit_codes else 0
        exit(exit_code)

    @staticmethod
    def merge_reports(reports):
        merged_report = Report("merged")
        for r in reports:
            merged_report.skipped_checks.extend(r.skipped_checks)
            merged_report.parsing_errors.extend(r.parsing_errors)
            merged_report.passed_checks.extend(r.passed_checks)
            merged_report.failed_checks.extend(r.failed_checks)
        return merged_report

    @staticmethod
    def report2sarif_report(report, args):
        sarif_report = SarifReport(report.check_type)
        sarif_report.passed_checks = report.passed_checks
        sarif_report.skipped_checks = report.skipped_checks
        sarif_report.failed_checks = report.failed_checks
        sarif_report.parsing_errors = report.parsing_errors
        sarif_report.repo_uri = "https://github.com/{}/".format(args.repo_id)
        sarif_report.branch = args.branch
        sarif_report.directory = args.directory
        return sarif_report
