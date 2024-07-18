import unittest
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.join(here, '..'))

from src.ToJyutping import utils

def simple_conv(s):
    return [(c, "zi6" if c == "字" else None) for c in s]

class TestUtils(unittest.TestCase):
    def test_format_romanization_text(self):
        with open(os.path.join(here, "format_romanization_test_cases.tsv"), encoding="utf-8") as f:
            for line in f:
                line = line.rstrip()
                if line:
                    test_string, expected = line.split("\t")
                    with self.subTest(test_string=test_string):
                        self.assertEqual(utils.format_romanization_text(test_string, simple_conv), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
