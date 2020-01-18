import unittest


# Факториальное время
#
def fibonacci(number: int):
    if number in (1, 2):                                        # O(1)
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)    # O(2^N)


class Test(unittest.TestCase):
    def test_fun_get_max_element_not_empty(self):
        number = 10
        print("Number: {}".format(number))
        result = fibonacci(number)
        print("Result: {}".format(result))
        self.assertTrue(result == 55)


if __name__ == "__main__":
    unittest.main()

