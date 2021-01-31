import calculation
import pytest


# def test_add_num_and_double():
#     cal = calculation.Cal()
#     assert cal.add_num_and_double(1, 1) == 4


class TestCal(object):
    @classmethod
    def setup_class(cls):
        print("start")
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        print("end")
        del cls.cal

    def setup_method(self, method):
        print(f"method={method.__name__}")

    def teardown_method(self, method):
        print(f"method={method.__name__}")

    def test_add_num_and_double(self):
        # cal = calculation.Cal()
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            # cal = calculation.Cal()
            self.cal.add_num_and_double("1", "1")
            # cal.add_num_and_double(1, 1)


if __name__ == "__main__":

    pytest.main()
