import inspect
import sys
import this
from datetime import datetime, date
from typing import Any
from unittest import TestCase
import os


class UnitTestReport(TestCase):
    test_report_started = False

    def __init__(self):
        """

        :rtype: object
        """
        # file_path = os.path.realpath(__file__)
        # project_path = os.path.dirname(os.path.abspath(file_path))
        project_path = self.get_project_path()
        print(project_path)
        self.unit_test_report_file = rf"{project_path}\unit_test_report.md"
        if not UnitTestReport.test_report_started:
            UnitTestReport.test_report_started = True
            self.reset_unit_test_report_log()
        super().__init__()

    def get_project_path(self) -> str:
        project_path = ""
        for item in inspect.stack():
            calling_file = item.filename
            path_parts = calling_file.split("\\")
            try:
                test_pos = path_parts.index("test")
                project_path = "/".join(path_parts[:test_pos])
                break
            except ValueError:
                pass
        return project_path

    def assertTrue(self, expr: Any, msg: Any = ...) -> None:
        message = ""
        if msg == Ellipsis:
            msg = ""
        if expr:
            message = f"* :green_circle: {msg}"
        else:
            message = f"* :red_circle: {msg}"
        for item in inspect.stack():
            calling_file = item.filename
            calling_function = item.function
            calling_line = item.lineno
            path_parts = calling_file.split("\\")
            unit_test_path = ""
            try:
                test_pos = path_parts.index("test")
                project_path = "/".join(path_parts[test_pos+1:])
                unit_test_path = f"[{project_path}](test/{project_path}]: {calling_function}(line {calling_line})"
                break
            except ValueError:
                pass
        print(unit_test_path)
        message += unit_test_path
        with open(self.unit_test_report_file, 'a') as f:
            f.writelines(message + "\n")
        super().assertTrue(expr, message)

    def reset_unit_test_report_log(self):
        report_header ="""
UNIT TEST REPORT
================
        """
        today = datetime.combine(date.today(), datetime.now().time())
        report_header += f"\n generation: {today}\n\n\n-------\n"
        with open(self.unit_test_report_file, 'w') as f:
            f.writelines(report_header)
