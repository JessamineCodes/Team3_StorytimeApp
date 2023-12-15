from unittest import testcase, main
from  main import <function_being_tested>

class TestNameOfFunction(TestCase)

# template:
    def test_name_of_test(self):
        expected = 2 or 'blue' or True # whatever the function returns
        result = function_being_tested(1,1) # input(s) to give expected result
        self.assertEqual(expected,result) # assertEqual assertNotEqual but there are many options


# example:

# If x is odd, return 'Red'
    def test_odd_numbers(self):
        expected = 'Red'
        result = red_or_blue(num=3)
        self.assertEqual(expected, result)


# If x is even and in the inclusive range of 2 to 5, return 'Blue'
    def test_even_greater_than_twenty(self):
        expected = 'Blue'
        result = red_or_blue(num=54)
        self.assertEqual(expected, result)

# If x is even and in the inclusive range of 6 to 20, return 'Red'
    def test_range_6_to_20(self):
        expected = 'Red'
        result = red_or_blue(num=12)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()



























# MOCKING
# read a file line by line and check the number of the last line.
# Extract that number, increment by 1 and return the new number
# def get_file_content(file_name):
#     with open(file_name, 'r') as file:
#         return file.readlines()
#
# def increment_line_number(file_name):
#     content = get_file_content(file_name)
#     num = int(content.pop().split('.')[0])
#     return num + 1
#
# from unittest import TestCase, mock, main # MOCK
# from main import increment_line_number
#
# class TestIncrementLineNumber(TestCase):
#
    @mock.patch('main.get_file_content') # main file.function to get file content
    def test_mock_file_read_function(self, mock_get_file_content):
        content = [
            '1. Hello',
            '2. Hi',
            '3. Good morning',
        ]
        mock_get_file_content.return_value = content # do not call fn, its return value is content
        self.assertEqual(increment_line_number('some_file'),4)
#

# if __name__ == '__main__':
#     main()

