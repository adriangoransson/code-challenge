import unittest
from flatten import flatten


class TestFlatten(unittest.TestCase):
    def test_flat_object(self):
        flat = {"a": 1, "b": True, "c": "c"}

        self.assertEqual(flat, flatten(flat))

    def test_included_data(self):
        data = {"a": 1, "b": True, "c": {"d": 3, "e": "test"}}
        expected = {"a": 1, "b": True, "c.d": 3, "c.e": "test"}

        self.assertEqual(expected, flatten(data))

    def test_nested(self):
        data = {
            "a": 1,
            "b": True,
            "c": {"d": 3, "e": "test", "f": {"g": 1, "h": False}},
        }

        expected = {
            "a": 1,
            "b": True,
            "c.d": 3,
            "c.e": "test",
            "c.f.g": 1,
            "c.f.h": False,
        }

        self.assertEqual(expected, flatten(data))


if __name__ == "__main__":
    unittest.main()
