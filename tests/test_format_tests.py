from format_tests import format_tests
import unittest


class EmptyHeadersTest(unittest.TestCase):
    def test_headers(self):
        format_test = format_tests.EmptyHeaders()
        format_test.test(["a", "b", "c"])
        self.assertTrue(format_test.passed)

        format_test = format_tests.EmptyHeaders()
        format_test.test(["a", "", "c"])
        self.assertFalse(format_test.passed)

        format_test = format_tests.EmptyHeaders()
        format_test.test(["", "", "c"])
        self.assertFalse(format_test.passed)