"""Модуль тестирования функции create_report_average."""

import unittest
from collections import defaultdict


from main import create_report_average


class TestReportAverage(unittest.TestCase):
    """Класс тестирования функции get_data_from_filecreate_report_average."""

    DATA:list = ['{"@timestamp": "2025-06-21T13:57:34+00:00", "status": 200,'
               ' "url": "/api/specializations/...",'
               ' "request_method": "GET", "response_time": 0.044, "http_user_agent": "..."}',
               '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200,'
               ' "url": "/api/homeworks/...", "request_method": "GET",'
               ' "response_time": 0.04, "http_user_agent": "..."}',
               '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200,'
               ' "url": "/api/users/...", "request_method": "GET",'
               ' "response_time": 0.072, "http_user_agent": "..."}',
               '{"@timestamp": "2025-06-23T13:57:34+00:00", "status": 200,'
               ' "url": "/api/challenges/...", "request_method": "GET",'
               ' "response_time": 0.056, "http_user_agent": "..."}',
               '{"@timestamp": "2025-06-23T13:57:34+00:00", "status": 200,'
               '"url": "/api/homeworks/...", "request_method": "GET",'
               ' "response_time": 0.06, "http_user_agent": "..."}']

    REPORT:dict = dict(
        {'/api/specializations/...': {'total': 1, 'avg_response_time': 0.044},
         '/api/homeworks/...': {'total': 2, 'avg_response_time': 0.1},
         '/api/users/...': {'total': 1, 'avg_response_time': 0.072},
         '/api/challenges/...': {'total': 1, 'avg_response_time': 0.056}
         })

    REPORT_FROM_DATE:dict = dict(
        {'/api/homeworks/...': {'total': 1, 'avg_response_time': 0.06},
         '/api/challenges/...': {'total': 1, 'avg_response_time': 0.056}
         })


    def test_create_report_average(self):
        """Тестировние составления defaultdict отчета average"""
        report: defaultdict = defaultdict(lambda: {"total": 0, "avg_response_time": 0.0})
        report = create_report_average(data=self.DATA, report=report)
        for handler in report:
            self.assertEqual(report[handler], self.REPORT[handler])



    def test_create_report_average_from_time(self):
        """Тестировние составления defaultdict отчета average
            учетом метки времени
        """
        report: defaultdict = defaultdict(lambda: {"total": 0, "avg_response_time": 0.0})
        report = create_report_average(data=self.DATA, report=report, timestamp="2025-06-23")
        for handler in report:
            self.assertEqual(report[handler], self.REPORT_FROM_DATE[handler])




if __name__ == '__main__':
    unittest.main()