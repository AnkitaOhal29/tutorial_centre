import requests
from django.test import TestCase
from mockito import when, mock, unstub


# Create your tests here.

import unittest

class TestMockMethods(unittest.TestCase):

    def test_mock_with_dummy_data(self):
        # mock_response = when(requests).get('https://jsonplaceholder.typicode.com/todos/1').thenReturn(mock({'status': 501})) \
        #                .thenRaise(requests.Timeout("I'm flaky")) \
        #                .thenReturn(mock({'status': 200, 'text': 'Ok'}))

        response = mock({'status_code': 200, 'text': 'Ok'})
        when(requests).get('https://jsonplaceholder.typicode.com/todos/1').thenReturn(response)

        # Call request url 
        res = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        print(res.status_code,res.text)
        self.assertEqual(res.status_code, res.status_code)

        # clean up
        unstub()


if __name__ == '__main__':
    unittest.main()