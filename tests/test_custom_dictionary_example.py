import importlib.util
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT))

from src.ToJyutping import ToJyutping


EXAMPLE_PATH = REPOSITORY_ROOT / "examples" / "custom_dictionary.py"
SPEC = importlib.util.spec_from_file_location("custom_dictionary_example", EXAMPLE_PATH)
assert SPEC is not None and SPEC.loader is not None
EXAMPLE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXAMPLE)


class TestCustomDictionaryExample(unittest.TestCase):
    def test_loads_json_entries_without_changing_default_converter(self):
        converter = EXAMPLE.load_custom_dictionary(ToJyutping)

        self.assertEqual(
            converter.get_jyutping_text("上堂終於講到分數"),
            "soeng6 tong4 zung1 jyu1 gong2 dou2 fan6 sou3",
        )
        self.assertEqual(
            converter.get_jyutping_candidates("到"),
            [("到", ["dou2", "dou3"])],
        )
        self.assertEqual(
            ToJyutping.get_jyutping_text("上堂終於講到分數"),
            "soeng5 tong4 zung1 jyu1 gong2 dou3 fan1 sou3",
        )

    def test_rejects_non_object_json(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "invalid_custom_dictionary.json"
            path.write_text(json.dumps(["fan1"]), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "must be a JSON object"):
                EXAMPLE.load_custom_dictionary(ToJyutping, path)


if __name__ == "__main__":
    unittest.main()
