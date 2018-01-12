"""Tests for practice problems."""

import unittest

import practice_problems


class CountAppearancesTest(unittest.TestCase):
    def test_good_input_results_in_expected_counts(self):
	'''Check for good results in expected counts'''
        expected_counts = {1: 2, 3: 1, 2:1}
        self.assertDictEqual(practice_problems.count_appearances([1, 1, 3, 2]),
                             expected_counts)

if __name__ == '__main__':
    unittest.main()
