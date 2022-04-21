"""
- Read these and the question instructions very carefully.
- You may only use Python language constructs, features, and functions covered in this class or specified below.
- Push to github frequently.  You will only receive credit for what is in github at the end of the exam.
- Remember to submit your quiz in MyCourses by the end of the exam time period.
- Recall the Academic Honesty Policy.
"""

from typing import Any


"""
Question 1 (XX pts): 

Description:

Example:

"""
def question_1(parameter: Any) -> Any:
    pass # replace with your soluton


"""
Question 2 (XX pts): 

Description:

Example:

"""
def question_2(parameter: Any) -> Any:
    pass # replace with your soluton


"""
Question 3 (XX pts): 

Description:

Example:

"""
def question_3(parameter: Any) -> Any:
    pass # replace with your soluton


"""
Question 4 (XX pts): 

Description:

Example:

"""
def question_4(parameter: Any) -> Any:
    pass # replace with your soluton


"""
Question 5 (XX pts): 

Description:

Example:

"""
def question_5(parameter: Any) -> Any:
    pass # replace with your soluton


# *********************************************************************
# **************  DO NOT MODIFY ANYTHING BELOW THIS LINE **************
# *********************************************************************
"""
Helper function to print the function name and arguments
    func_name - name of function
    args - arguments to function under test  (this must come last since there are a variable number of arguments)
"""
RESULT_LEN = 75 # Change to fit function/args print length

def print_func_and_args(func_name, args):
    # str([arg for arg in args])[1:-1] returns list of args as string w/o '[' or ']'
    # .ljust(40) ensures all strings are of size RESULT_LEN with the string body left justified and padded w/ spaces
    print(f'{func_name}({str([arg for arg in args])[1:-1]}) ... '.ljust(RESULT_LEN), end = '')


def print_method_and_args(object_name, func_name, args):
    # str([arg for arg in args])[1:-1] returns list of args as string w/o '[' or ']'
    # .ljust(40) ensures all strings are of size RESULT_LEN with the string body left justified and padded w/ spaces
    print(f'{object_name}.{func_name}({str([arg for arg in args])[1:-1]}) ... '.ljust(RESULT_LEN), end = '')


"""
Helper function to run a test and print result
    func - function being tested
    expected_result - expected result
    args - arguments to function under test  (this must come last since there are a variable number of arguments)
"""
def run_test(func,expected_result, *args):
    try:
        print_func_and_args(func.__name__, args)
        actual_result = func(*args)
        if actual_result == expected_result:
            print('passed')
        else:
            print(f'failed [expected: {expected_result}, actual: {actual_result}]', sep = '')
    except Exception as e:
        print(f'failed [runtime error: {e}]', sep = '')


def main():
    ###########################################################################
    # run_test arguments: function to test, expected result, function arguments
    ###########################################################################
    # Question 1 tests
    print('*** question_1 tests:')
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    print()

    # Question 2 tests
    print('*** question_2 tests:')
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    print()

    # Question 3 tests
    print('*** question_3 tests:')
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    print()

    # Question 4 tests
    print('*** question_4 tests:')
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    print()

    # Question 5 tests
    print('*** question_5 tests:')
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    # run_test()
    print()
    
if __name__ == "__main__":
    main()
