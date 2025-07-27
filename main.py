"""Скрипт обработки log файла."""

import json
import logging
import os.path
from argparse import ArgumentParser
from collections import defaultdict
from tabulate import tabulate


def get_argument_parser() -> ArgumentParser:
    """Возвращает парсер аргументов команды запуска скрипта."""
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", nargs="*", help="Имена файлов логов")
    parser.add_argument("-r", "--report", choices=["average"], help="Тип отчета")
    parser.add_argument("-d", "--date", default=None)
    return parser


def get_data_from_file(file_name: str) -> list:
    """Возвращает не обработанные данные из log файла."""
    data: list = []
    full_name: str = os.path.join(".", "logs", file_name)
    try:
        with open(full_name, "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        logging.error(f"Файл {file_name} не найден")
    return data


def create_report_average(data: list, report: defaultdict, timestamp: str = None) -> defaultdict:
    """Формирует отчет average для одного файла."""
    for line in data:
        frame = json.loads(line)
        if (not timestamp) or (timestamp and timestamp in frame["@timestamp"]):
            handler = frame["url"]
            resp_time = frame["response_time"]
            report[handler]["total"] += 1
            report[handler]["avg_response_time"] += resp_time
    return report


def print_report_average(report: defaultdict) -> None:
    """Вывод в консоль отчета типа average."""
    table_data = [[handler, stats["total"], stats["avg_response_time"]] for handler, stats in report.items()]
    print(tabulate(table_data, headers=["handler", "total", "avg_response_time"]))


def main() -> None:
    """Функция запуска скрипта."""
    parser = get_argument_parser()
    args = parser.parse_args()
    if args.report == "average":
        report: defaultdict = defaultdict(lambda: {"total": 0, "avg_response_time": 0.0})
        for file in args.file:
            data = get_data_from_file(file_name=file)
            report = create_report_average(data=data, report=report, timestamp=args.date)
        # Вычисление среднего времени
        for handler in report:
            report[handler]["avg_response_time"] = round(
                report[handler]["avg_response_time"] / report[handler]["total"],
                3
            )
        print_report_average(report)


if __name__ == '__main__':
    main()
