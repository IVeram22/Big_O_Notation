import unittest


# Линейно-логарифмическое время
#
def merge_sort(unsorted_list: list):
    pass


# O(N^2)
def is_list_sorted(sorted_list: list):
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                return False

    return True


class Test(unittest.TestCase):
    def test_fun_merge_sort_not_empty(self):
        my_list = [1, 2, 3, 4, 66, 7, 2, 1, 8, 99, 3]
        print("Unsorted List: {}".format(my_list))
        merge_sort(my_list)
        print("Sorted List: {}".format(my_list))
        self.assertTrue(is_list_sorted(my_list))

    def test_fun_merge_sort_empty(self):
        my_list = []
        print("Unsorted List: {}".format(my_list))
        merge_sort(my_list)
        print("Sorted List: {}".format(my_list))
        self.assertTrue(is_list_sorted(my_list))


if __name__ == "__main__":
    unittest.main()
