"""Модуль тестирования функции get_data_from_file."""

import unittest
import tempfile
import os

from main import get_data_from_file


def create_test_file(content) -> str:
    """Создает временный файл."""
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w")
    temp_file.write(content)
    temp_file.close()
    return temp_file.name


class TestGetData(unittest.TestCase):
    """Класс тестирования функции get_data_from_file."""

    CONTENT = ('{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200,'
               ' "url": "/api/specializations/...",'
               ' "request_method": "GET", "response_time": 0.044, "http_user_agent": "..."}'
               '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200,'
               '"url": "/api/homeworks/...", "request_method": "GET",'
               '"response_time": 0.04, "http_user_agent": "..."}'
               '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200,'
               '"url": "/api/users/...", "request_method": "GET",'
               '"response_time": 0.072, "http_user_agent": "..."}'
               '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200,'
               '"url": "/api/challenges/...", "request_method": "GET",'
               '"response_time": 0.056, "http_user_agent": "..."}'
               '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200,'
               '"url": "/api/homeworks/...", "request_method": "GET",'
               '"response_time": 0.06, "http_user_agent": "..."}')


    def setUp(self):
        """Создание временного файла перед тестом."""
        self.test_file = create_test_file(self.CONTENT)

    def tearDown(self):
        """Удаление временного файла после теста."""
        os.unlink(self.test_file)

    def test_get_data_from_file(self):
        """Тестировние чтения данных из файла"""
        data = get_data_from_file(self.test_file)
        self.assertEqual(data, [self.CONTENT])



if __name__ == '__main__':
    unittest.main()
