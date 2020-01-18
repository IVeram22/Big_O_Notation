import unittest


# Линейное время
# O( 1 + 1 + 1 + 1 + N * 2 ) = O(4 + 2N) = O(2N) = O(N)
def get_max_element(lst: list):
    length = len(lst)               # O(1)

    if length == 0:                 # O(1)
        return

    if length == 1:                 # O(1)
        return lst[0]

    max_value = lst[0]              # O(1)
    for i in range(len(lst)):       # O(N)
        if max_value < lst[i]:      # O(1)
            max_value = lst[i]

    return max_value


class Test(unittest.TestCase):
    def test_fun_get_max_element_not_empty(self):
        my_list = [1, 2, 3, 4, 66, 7, 2, 1, 8, 99, 3]
        print("List: {}".format(my_list))
        result = get_max_element(my_list)
        print("Result: {}".format(result))
        self.assertTrue(result == 99)

    def test_fun_get_max_element_empty(self):
        my_list = []
        print("List: {}".format(my_list))
        result = get_max_element(my_list)
        print("Result: {}".format(result))
        self.assertTrue(result is None)

    def test_fun_get_max_element_len_one(self):
        my_list = [2]
        print("List: {}".format(my_list))
        result = get_max_element(my_list)
        print("Result: {}".format(result))
        self.assertTrue(result == 2)


if __name__ == "__main__":
    unittest.main()
