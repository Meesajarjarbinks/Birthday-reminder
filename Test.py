import unittest
from main2.py import patch
from concrete_birthday_reminder import ConcreteBirthdayReminder
import datetime

try:
  from unittest.mock import patch
except ImportError:
  from mock import patch
class TestConcreteBirthdayReminder(unittest.TestCase):

    def setUp(self):
        self.reminder = ConcreteBirthdayReminder()

    def tearDown(self):
        # Clean up any resources used by the tests
        pass

    @patch('builtins.input', side_effect=['John', 'password'])
    def test_create_account(self, mock_input):
        self.assertTrue(self.reminder.create_account('John', 'password'))
        self.assertIn('John', self.reminder.users)

    @patch('builtins.input', side_effect=['John', 'password'])
    def test_login(self, mock_input):
        self.reminder.create_account('John', 'password')
        self.assertTrue(self.reminder.login('John', 'password'))

    @patch('builtins.input', side_effect=['John', 'password', 'David', '2024', '4', '19'])
    def test_add_birthday(self, mock_input):
        self.reminder.create_account('John', 'password')
        with patch('builtins.input', side_effect=['David', '2024', '4', '19']):
            self.reminder.add_birthday('John')
        with open('birthdays.txt') as file:
            lines = file.readlines()
            self.assertIn('John,David,2024,4,19\n', lines)

    @patch('builtins.input', side_effect=['John', 'David', '2024', '4', '19'])
    def test_check_birthday_today(self, mock_input):
        today = datetime.datetime.today()
        with open('birthdays.txt', 'a') as file:
            file.write(f"John,David,{today.year},{today.month},{today.day}\n")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.reminder.check_birthday_today('John')
            self.assertEqual(mock_stdout.getvalue().strip(), f"David's birthday is today!")

if __name__ == '__main__':
    unittest.main()
