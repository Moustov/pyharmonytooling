import inspect
from datetime import datetime, date
from typing import Any
from unittest import TestCase


class UnitTestReport(TestCase):
    test_report_started = False
    project_path = ""
    green = 0
    red = 0

    def __init__(self):
        """
        """
        project_path = self.get_project_path()
        print(project_path)
        self.unit_test_report_file = rf"{project_path}\unit_test_report.md"
        if not UnitTestReport.test_report_started:
            UnitTestReport.test_report_started = True
            self.reset_unit_test_report_log()
        super().__init__()

    def get_project_path(self) -> str:
        """
        get the project path from stack
        => must be used only while running test cases under the folder "test"
        :return:
        """
        if UnitTestReport.project_path != "":
            return self.project_path
        project_path = ""
        for item in inspect.stack():
            calling_file = item.filename
            path_parts = calling_file.split("\\")
            try:
                test_pos = path_parts.index("test")
                project_path = "\\".join(path_parts[:test_pos])
                break
            except ValueError:
                pass
        self.project_path = project_path
        return project_path

    def assertTrue(self, expr: Any, msg: Any = ...) -> None:
        """
        intercept asserts to update the test report
        :param expr:
        :param msg:
        :return:
        """
        message = ""
        unit_test_path = ""
        if msg == Ellipsis:
            msg = ""
        if expr:
            message = f"* :green_circle:"
            UnitTestReport.green += 1
        else:
            message = f"* :red_circle: {msg}"
            UnitTestReport.red += 1
        for item in inspect.stack():
            calling_file = item.filename
            calling_function = item.function
            calling_line = item.lineno
            path_parts = calling_file.split("\\")
            unit_test_path = ""
            try:
                test_pos = path_parts.index("test")
                project_path = "/".join(path_parts[test_pos+1:])
                unit_test_path = f"[[{project_path}](test/{project_path}#L{calling_line})]: {calling_function}(line {calling_line}): {msg}"
                break
            except ValueError:
                pass
        print(unit_test_path)
        message += unit_test_path
        self.update_report(message)
        super().assertTrue(expr, message)

    def reset_unit_test_report_log(self):
        """
        initialize the test report
        :return:
        """
        report_header = """
UNIT TEST REPORT
================
        """
        today = datetime.combine(date.today(), datetime.now().time())
        report_header += f"\n generation: {today}\n\n\n-------\n"
        with open(self.unit_test_report_file, 'w') as f:
            f.writelines(report_header)

    def update_report(self, msg: str):
        """
        update the report with the message at the end
        :param msg:
        :return:
        """
        report_lines = []
        # https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/#read-and-write-a-file-with-r
        with open(self.unit_test_report_file, 'r') as f:
            report = f.read()
            report_lines = report.split("\n")
            report_lines[5] = f":red_circle:{UnitTestReport.red}"
            report_lines[6] = f":green_circle:{UnitTestReport.green}"
            report_lines.append(msg)
        report = "\n".join(report_lines)
        with open(self.unit_test_report_file, 'w') as f:
            f.writelines(report)

