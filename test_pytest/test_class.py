import pytest


class TestClass:

    @pytest.mark.one
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


# class test_attr():
#
#       name = "xiaohua"
#
#       def run(self):
#
#         return "HelloWord"
#
#
# def test_003():
#
#
#     t = test_attr()
#
#     result = hasattr(t,"age")
#
#     if result == False:
#
#         setattr(t, "age", 50)
#
#     print(getattr(t, "age"))
