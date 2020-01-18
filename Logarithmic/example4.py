import unittest


# Логарифмическое время
# O( 1 + 1 + 1 + 1 + 1 + logN * 1 ) = O(6 + logN) = O(logN)
def is_element_in_list(element: int, lst: list):
    length = len(lst)                   # O(1)

    if length == 0:                     # O(1)
        return False

    if length == 1:                     # O(1)
        return element == lst[0]

    center = int(len(lst)/2)            # O(1)
    start = center
    if element == lst[center]:          # O(1)
        return True

    if element <= lst[center]:          # O(1)
        start = 0

    for i in range(start, center):      # O(logN)
        if element == lst[i]:           # O(1)
            return True

    return False


class Test(unittest.TestCase):
    def test_fun_is_element_in_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7]
        result = is_element_in_list(4, my_list)
        self.assertTrue(result)

    def test_fun_is_element_in_list_empty(self):
        my_list = []
        result = is_element_in_list(22, my_list)
        self.assertTrue(result == False)

    def test_fun_is_element_in_list_len_one(self):
        my_list = [2]
        result = is_element_in_list(2, my_list)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
