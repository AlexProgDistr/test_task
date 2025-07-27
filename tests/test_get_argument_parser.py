"""Модуль тестирования функции get_argument_parser."""

import unittest
from unittest.mock import patch
from main import get_argument_parser


class TestArgParse(unittest.TestCase):
    """Класс тестирования функции get_argument_parser."""

    def test_get_argument_parser(self):
        """Тест get_argument_parser без указания даты."""
        test_args = ["--file", "examlpe1.log", "example2.log", "--report", "average"]
        with patch("sys.argv", ["main.py"] + test_args):
            args = get_argument_parser().parse_args()
            self.assertEqual(args.file, ["examlpe1.log", "example2.log"])
            self.assertEqual(args.report, "average")

    def test_get_argument_parser_from_date(self):
        """Тест get_argument_parser с указания даты."""
        test_args = ["--file", "examlpe1.log", "--report", "average", "--date", "2025-23-06"]
        with patch("sys.argv", ["main.py"] + test_args):
            args = get_argument_parser().parse_args()
            self.assertEqual(args.file, ["examlpe1.log"])
            self.assertEqual(args.report, "average")
            self.assertEqual(args.date, "2025-23-06")


if __name__ == '__main__':
    unittest.main()
