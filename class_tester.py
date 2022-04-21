'''
DO NOT EDIT ANYTHING IN THIS FILE

This is a class used for testing class state/behavior implementation

author: Kamron Cole kjc8084@rit.edu
'''
import re

from copy import deepcopy

RESULT_LEN = 75

class ClassTester:
    __slots__ = ['__objects', '__class_t', '__const_args', '__expected_state',
                 '__expected_behavior', '__expected_sorted', '__const_test_passed']

    def __init__(self, type, const_args: list[list], expected_state: list[str],
                 expected_methods: dict[str, dict[tuple, list]], expected_get: dict[str, list],
                 expected_set: dict[str, list], expected_sorted: str):
        '''
        Params:
            type:
                - The Class to test
            const_args:
                - List of 4 lists, each tuple being the arguments to create one object
                - The tuples at index 0 and 1 should be the same to test __eq__ implementation
            expected_state:
                - List of strings that are the Class's expected variable names
            expected_methods:
                - Dictionary mapping a string of the method name to another dictionary mapping tuple of method arguments to list of expected results
                - Each element in the list corresponds to the object created with const_args
            expected_get:
                - Same format as expected_methods
                - Specifically for getter methods
            expected_set:
                - Dictionary mapping method name string to a sequence with 2 elements
                - First element being the variable that is supposed to be set
                - Second element being the new value of that variable
            expected_sorted:
                - Repr string of the sorted list of objects after they are added to a set
                - If testing __eq__ there should only be 3 values in the string list (because of the set)
        '''
        obj1 = None
        obj2 = None
        obj3 = None
        obj4 = None

        self.__objects = [obj1, obj2, obj3, obj4]

        if len(const_args) != 4:
            raise ValueError(f'expected length of const_args to be 3, got {len(const_args)}')

        self.__class_t = type
        self.__const_args = const_args
        self.__expected_state = expected_state

        self.__expected_behavior = {
            'get': expected_get,
            'set': expected_set,
            'methods': expected_methods
        }

        self.__expected_sorted = expected_sorted

        self.__const_test_passed = False


    def const_test_check(self) -> bool:
        if not self.__const_test_passed:
            print('Constructor test not passed yet.')
            return False
        return True


    def run_constructor_tests(self):
        print('Constructor Tests:'.ljust(RESULT_LEN), end='')
        try:
            for i in range(len(self.__objects)):
                args = self.__const_args[i]
                if len(args) == 0:
                    self.__objects[i] = self.__class_t()
                else:
                    self.__objects[i] = self.__class_t(*args)
            print('passed')
            self.__const_test_passed = True
        except Exception as e:
            raise e
            print(f'failed [runtime error: {e}]', sep='')


    def run_getter_tests(self):
        print('Getter Tests:'.ljust(RESULT_LEN), end='')
        if not self.const_test_check():
            return

        try:
            object_index = 0
            for method_name, expected_result in self.__expected_behavior['get'].items():
                actual_result = getattr(self.__objects[object_index], method_name)()
                if actual_result != expected_result[object_index]:
                    print(f'failed [expected: {expected_result[object_index]}, actual: {actual_result}]', sep='')
                    return
                object_index += 1
            print('passed')
        except Exception as e:
            print(f'failed [runtime error: {e}]', sep='')


    def run_setter_tests(self):
        print('Setter Tests:'.ljust(RESULT_LEN), end='')
        if not self.const_test_check():
            return

        try:
            for method_name, variable_value_seq in self.__expected_behavior['set'].items():
                expected_value = variable_value_seq[1]
                for obj in self.__objects:
                    variable_name = f'_{type(obj).__name__}{variable_value_seq[0]}'
                    obj_copy = deepcopy(obj)
                    getattr(obj_copy, method_name)(expected_value)
                    actual_value = getattr(obj_copy, variable_name)
                    if actual_value != expected_value:
                        print(f'failed [expected: {variable_name}={expected_value}, actual: {variable_name}={actual_value}]', sep='')
                        return
            print('passed')
        except Exception as e:
            print(f'failed [runtime error: {e}]', sep='')


    def run_method_tests(self):
        print('Method Tests:'.ljust(RESULT_LEN), end='')
        if not self.const_test_check():
            return

        try:
            object_index = 0
            for method_name, args_result_dict in self.__expected_behavior['methods'].items():
                if method_name == '__str__' or method_name == '__repr':
                    continue

                args, expected_result = list(args_result_dict.items())[0]

                actual_result = None
                if args is None:
                    actual_result = getattr(self.__objects[object_index], method_name)()
                else:
                    actual_result = getattr(self.__objects[object_index], method_name)(*args)

                if actual_result != expected_result[object_index]:
                    print(f'failed [expected: {expected_result[object_index]}, actual: {actual_result}]', sep='')
                    return
                object_index += 1
            print('passed')
        except Exception as e:
            print(f'failed [runtime error: {e}]', sep='')


    def run_repr_tests(self):
        print('Repr Tests:'.ljust(RESULT_LEN), end='')
        if not self.const_test_check():
            return

        try:
            for i in range(len(self.__objects)):
                obj = self.__objects[i]
                expected_result = list(self.__expected_behavior['methods']['__repr__'].items())[0][1][i]
                actual_result = obj.__repr__()
                if actual_result != expected_result:
                    print(f'failed [expected: {expected_result}, actual: {actual_result}]', sep='')
                    return
            print('passed')
        except Exception as e:
            print(f'failed [runtime error: {e}]', sep='')


    def run_str_tests(self):
        print('Str Tests:'.ljust(RESULT_LEN), end='')
        if not self.const_test_check():
            return

        try:
            for i in range(len(self.__objects)):
                obj = self.__objects[i]
                _, expected_result = list(self.__expected_behavior['methods']['__str__'].items())[0][1][i]
                actual_result = obj.__str__()
                if actual_result != expected_result:
                    print('failed!')
                    return
            print('passed')
        except Exception as e:
            print(f'failed [runtime error: {e}]', sep='')


    def run_eq_tests(self):
        obj1 = self.__objects[0]
        obj2 = self.__objects[1]
        obj3 = self.__objects[2]
        obj4 = self.__objects[3]
        print('Equality Tests:'.ljust(RESULT_LEN), end='')
        if not self.const_test_check():
            return

        try:
            assert(obj1 == obj2)
            assert(obj1 != obj3)
            assert(obj1 != obj4)
            assert(obj2 != obj3)
            assert(obj3 != obj4)
            print('passed')
        except Exception:
            print('failed!')


    def run_set_sort_tests(self):
        obj1 = self.__objects[0]
        obj2 = self.__objects[1]
        obj3 = self.__objects[2]
        obj4 = self.__objects[3]
        print('Set & Sort Tests:'.ljust(RESULT_LEN), end='')
        if not self.const_test_check():
            return

        try:
            obj_set = set()
            obj_set.add(obj1)
            obj_set.add(obj2)
            obj_set.add(obj3)
            obj_set.add(obj4)
            obj_list = list(obj_set)
            assert(sorted(obj_list).__repr__() == self.__expected_sorted)
            print('passed')
        except Exception:
            print(f'failed [expected: {self.__expected_sorted}, actual: {sorted(obj_list).__repr__()}]')


    def run_attr_tests(self):
        print('Attributes Tests:'.ljust(RESULT_LEN), end='')
        if not self.const_test_check():
            return

        try:
            for object in self.__objects:
                for attr in self.__expected_state:
                    assert f'_{type(object).__name__}{attr}' in dir(object)
            print('passed')
        except Exception:
            print('failed!')


    def run_all_tests(self):
        self.run_constructor_tests()
        if self.__expected_behavior['get']:
            self.run_getter_tests()
        if self.__expected_behavior['set']:
            self.run_setter_tests()
        if '__str__' in self.__expected_behavior['methods']:
            self.run_str_tests()
        if '__repr__' in self.__expected_behavior['methods']:
            self.run_repr_tests()
        if self.__expected_behavior['set']:
            self.run_method_tests()
        if '__eq__' in dir(self.__objects[0]):
            self.run_eq_tests()
        if '__hash__' in dir(self.__objects[0]) and self.__expected_sorted:
            self.run_set_sort_tests()
        if self.__expected_state:
            self.run_attr_tests()
        print()


'''
EXAMPLE IMPLEMENTATION
'''

class PhoneNumber:
    __slots__ = ['__number', '__sumVal', '__productVal']

    def __init__(self, phone_number: str):
        self.__number = re.sub('[^0-9]', '', phone_number)
        self.__sumVal = 0
        self.__productVal = 1

        for value in self.__number:
            value = int(value)
            self.__sumVal += value
            self.__productVal *= value


    def __repr__(self) -> str:
        return self.__number + ':' + str(self.__sumVal) + ':' + str(self.__productVal)


    def __eq__(self, other) -> bool:
        if type(other) != type(self):
            return False
        return self.__number == other.get_number()


    def __hash__(self) -> int:
        return hash(self.__number * (self.__sumVal + self.__productVal))


    def __lt__(self, other) -> bool:
        if type(other) != type(self):
            return False
        return self.__productVal < other.get_productVal()


    def params_plus_last_digit(self, param1, param2):
        return int(self.__number[-1]) + param1 + param2


    def get_number(self) -> str:
        return self.__number


    def get_sumVal(self) -> int:
        return self.__sumVal


    def get_productVal(self) -> int:
        return self.__productVal


    def set_number(self, newNum):
        self.__number = newNum


def main():
    # Note: element 1 and 2 need to make 'equal' classes if you are expecting __eq__ implementation
    const_args = [['(585) 555-1212'],
                  ['585-555-1212'],
                  ['585-555-1111'],
                  ['585-555-2222']]
    expected_state = ['__number', '__sumVal', '__productVal'] # Expected Variables
    expected_normal = {'__repr__': {None: ['5855551212:39:100000', '5855551212:39:100000', '5855551111:37:25000', '5855552222:41:400000']},
                       'params_plus_last_digit': {(1, 2): [5, 5, 4, 5]}}
    expected_get = {
        'get_number': ['5855551212', '5855551212', '5855551111', '5855552222'],
        'get_sumVal': [39, 39, 37, 41],
        'get_productVal': [100000, 100000, 25000, 400000]
    }
    expected_set = {'set_number': ['__number', '5851111111']} # Dictionary of any setter methods and their expected results
    expected_sorted = '[5855551111:37:25000, 5855551212:39:100000, 5855552222:41:400000]'
    ct = ClassTester(PhoneNumber, const_args, expected_state, expected_normal, expected_get, expected_set, expected_sorted)

    print('*** PhoneNumber tests:')
    ct.run_all_tests()


if __name__ == '__main__':
    main()
