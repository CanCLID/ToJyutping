"""Load persistent custom ToJyutping entries from a JSON file."""

import json
from pathlib import Path
from typing import Any


DEFAULT_DICTIONARY_PATH = Path(__file__).with_suffix(".json")


def load_custom_dictionary(converter: Any, path: Path = DEFAULT_DICTIONARY_PATH) -> Any:
    """Return a converter customized with entries loaded from *path*."""
    with path.open(encoding="utf-8") as file:
        entries = json.load(file)

    if not isinstance(entries, dict):
        raise ValueError("The custom dictionary must be a JSON object")

    return converter.customize(entries)


def main() -> None:
    import ToJyutping

    converter = load_custom_dictionary(ToJyutping)
    print(converter.get_jyutping_text("上堂終於講到分數"))


if __name__ == "__main__":
    main()
