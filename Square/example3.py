import unittest


# Квадратичное время
# O( N * (N * 1)) = O(N*N) = O(N^2)
def bubble_sort(unsorted_list: list):
    for i in range(len(unsorted_list)):                 # O(N)
        for j in range(len(unsorted_list)):             # O(N)
            if unsorted_list[i] < unsorted_list[j]:     # O(1)
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]


# O(N^2)
def is_list_sorted(sorted_list: list):
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                return False

    return True


class Test(unittest.TestCase):
    def test_fun_bubble_sort_not_empty(self):
        my_list = [1, 2, 3, 4, 66, 7, 2, 1, 8, 99, 3]
        print("Unsorted List: {}".format(my_list))
        bubble_sort(my_list)
        print("Sorted List: {}".format(my_list))
        self.assertTrue(is_list_sorted(my_list))

    def test_fun_bubble_sort_empty(self):
        my_list = []
        print("Unsorted List: {}".format(my_list))
        bubble_sort(my_list)
        print("Sorted List: {}".format(my_list))
        self.assertTrue(is_list_sorted(my_list))


if __name__ == "__main__":
    unittest.main()
