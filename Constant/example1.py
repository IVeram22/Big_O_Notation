import unittest


# Константное время
# O( 1 + 1 + 1 ) = O(3) = O(1)
def get_central_element(lst: list):
    if len(lst) == 0:           # O(1)
        return

    center = int(len(lst) / 2)  # O(1)
    return lst[center]          # O(1)


class Test(unittest.TestCase):
    def test_fun_get_central_element_not_empty(self):
        my_list = [1, 2, 8, 4, 5]
        print("List: {}".format(my_list))
        result = get_central_element(my_list)
        print("Result: {}".format(result))
        self.assertTrue(result == 8)

    def test_fun_get_central_element_empty(self):
        my_list = []
        print("List: {}".format(my_list))
        result = get_central_element(my_list)
        print("Result: {}".format(result))
        self.assertTrue(result is None)

    def test_fun_get_central_element_len_one(self):
        my_list = [2]
        print("List: {}".format(my_list))
        result = get_central_element(my_list)
        print("Result: {}".format(result))
        self.assertTrue(result == 2)


if __name__ == "__main__":
    unittest.main()
