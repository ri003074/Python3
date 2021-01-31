import calculation
import pytest


# def test_add_num_and_double():
#     cal = calculation.Cal()
#     assert cal.add_num_and_double(1, 1) == 4


class TestCal(object):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = calculation.Cal()
            cal.add_num_and_double("1", "1")
            # cal.add_num_and_double(1, 1)


if __name__ == "__main__":

    pytest.main()
