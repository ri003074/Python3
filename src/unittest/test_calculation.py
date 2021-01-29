import unittest
import calculation

release_name = "lesson"


class CalTest(unittest.TestCase):
    def setUp(self):
        print("set up")
        self.cal = calculation.Cal()

    def tearDown(self):
        print("clean up")
        del self.cal

    # @unittest.skip("skip!")
    @unittest.skipIf(release_name == "lesson", "skip!!")
    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double("1", "1")


if __name__ == "__main__":
    unittest.main()
