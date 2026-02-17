# Using ToJyutping in [Bert-VITS2](https://github.com/fishaudio/Bert-VITS2)

We have prepared a set of files for **drop-in replacements**:

- **Download** the files in the [`keep_other_languages` folder](keep_other_languages/text) if you plan to **keep** languages other than Cantonese.
- **Download** the files in the [`remove_other_languages` folder](remove_other_languages/text) if you plan to **remove** languages other than Cantonese.

Then, simply **drag-and-drop/`mv -f`** them to replace the files with identical names in the `text` folder of the original Bert-VITS2 repo, execute `pip install ToJyutping`, and you’re done!

However, if you prefer hands-on work, you may also amend the files manually according to the following diffs:

<details>
<summary>

## Manual Modification

</summary>

### `text/cleaner.py`

```diff
+import ToJyutping
+import unicodedata
+
 from text import chinese, japanese, english, cleaned_text_to_sequence
+from text.symbols import symbols, yue_offset
 
 language_module_map = {"ZH": chinese, "JP": japanese, "EN": english}
 
 
 def clean_text(text, language):
+    text = unicodedata.normalize("NFC", text)
+    if language == "YUE":
+        # Already handles punctuation and maps to symbol IDs internally
+        phonemes = ToJyutping.g2p(text, offset=(yue_offset, yue_offset, 1))
+        norm_text = "".join(
+            char if length > 1 else
+            # Convert punctuation ID back to one of … . , ! ? - '
+            symbols[phonemes.segmentals[sum(phonemes.lengths[:i])]] if length == 1 else ""
+            for i, (char, length) in enumerate(zip(text, phonemes.lengths, strict=True))
+        )
+        lengths = [length for length in phonemes.lengths if length > 0]
+        return norm_text, phonemes.segmentals, phonemes.tones, lengths
     language_module = language_module_map[language]
     norm_text = language_module.text_normalize(text)
     phones, tones, word2ph = language_module.g2p(norm_text)
     return norm_text, phones, tones, word2ph
 
 # ...
```

You may remove the `clean_text_bert` and `text_to_sequence` methods because they are not used anywhere. Bert models are handled in the `get_bert` method in `text/__init__.py`.

### `text/__init__.py`

```diff
 # ...
 
 def cleaned_text_to_sequence(cleaned_text, tones, language):
     """Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
     Args:
       text: string to convert to a sequence
     Returns:
       List of integers corresponding to the symbols in the text
     """
-    phones = [_symbol_to_id[symbol] for symbol in cleaned_text]
+    # For Cantonese, ToJyutping.g2p already mapped the text into symbol IDs
+    phones = cleaned_text if language == "YUE" else [_symbol_to_id[symbol] for symbol in cleaned_text]
     tone_start = language_tone_start_map[language]
     tones = [i + tone_start for i in tones]
     lang_id = language_id_map[language]
     lang_ids = [lang_id for i in phones]
     return phones, tones, lang_ids

 def get_bert(norm_text, word2ph, language, device, style_text=None, style_weight=0.7):
     from .chinese_bert import get_bert_feature as zh_bert
     from .english_bert_mock import get_bert_feature as en_bert
     from .japanese_bert import get_bert_feature as jp_bert
 
-    lang_bert_func_map = {"ZH": zh_bert, "EN": en_bert, "JP": jp_bert}
+    # Import your Cantonese Bert model here, or reuse the Chinese Bert model:
+    lang_bert_func_map = {"ZH": zh_bert, "EN": en_bert, "JP": jp_bert, "YUE": zh_bert}
     bert = lang_bert_func_map[language](
         norm_text, word2ph, device, style_text, style_weight
     )
     return bert
 
 # ...
```

### `text/symbols.py`

```diff
-punctuation = ["!", "?", "…", ",", ".", "'", "-"]
+# Follows the order in ToJyutping.g2p
+punctuation = ["…", ".", ",", "!", "?", "-", "'"]
 pu_symbols = punctuation + ["SP", "UNK"]
 pad = "_"
 
 # ...
 
+# Cantonese: Symbols are already mapped internally in ToJyutping.g2p
+# Generates identity mappings for `len(symbols)` to work correctly
+yue_symbols = list(range(87))
+num_yue_tones = 6
 
 # combine all symbols
 normal_symbols = sorted(set(zh_symbols + ja_symbols + en_symbols))
-symbols = [pad] + normal_symbols + pu_symbols
+# Following ToJyutping.g2p, punctuation must come before other symbols
+symbols = [pad] + pu_symbols + normal_symbols
+yue_offset = len(symbols)  # For use by ToJyutping.g2p in cleaner.py
+symbols += yue_symbols
 sil_phonemes_ids = [symbols.index(i) for i in pu_symbols]
 
 # combine all tones
-num_tones = num_zh_tones + num_ja_tones + num_en_tones
+num_tones = num_zh_tones + num_ja_tones + num_en_tones + num_yue_tones
 
 # language maps
-language_id_map = {"ZH": 0, "JP": 1, "EN": 2}
+language_id_map = {"ZH": 0, "JP": 1, "EN": 2, "YUE": 3}
 num_languages = len(language_id_map.keys())
 
 language_tone_start_map = {
     "ZH": 0,
     "JP": num_zh_tones,
     "EN": num_zh_tones + num_ja_tones,
+    "YUE": num_zh_tones + num_ja_tones + num_en_tones,
 }
 
 # ...
```

Or if you plan to remove other languages:

```diff
-punctuation = ["!", "?", "…", ",", ".", "'", "-"]
+# Follows the order in ToJyutping.g2p
+punctuation = ["…", ".", ",", "!", "?", "-", "'"]
 pu_symbols = punctuation + ["SP", "UNK"]
 pad = "_"
 
-# chinese
-zh_symbols = [
-# ...
-]
-num_en_tones = 4
 
+# Cantonese: Symbols are already mapped internally in ToJyutping.g2p
+# Generates identity mappings for `len(symbols)` to work correctly
+yue_symbols = list(range(87))
+num_yue_tones = 6
 
 # combine all symbols
-normal_symbols = sorted(set(zh_symbols + ja_symbols + en_symbols))
-symbols = [pad] + normal_symbols + pu_symbols
+symbols = [pad] + pu_symbols
+yue_offset = len(symbols)  # For use by ToJyutping.g2p in cleaner.py
+symbols += yue_symbols
 sil_phonemes_ids = [symbols.index(i) for i in pu_symbols]
 
 # combine all tones
-num_tones = num_zh_tones + num_ja_tones + num_en_tones
+num_tones = num_yue_tones
 
 # language maps
-language_id_map = {"ZH": 0, "JP": 1, "EN": 2}
+language_id_map = {"YUE": 0}
 num_languages = len(language_id_map.keys())
 
 language_tone_start_map = {
-    "ZH": 0,
-    "JP": num_zh_tones,
-    "EN": num_zh_tones + num_ja_tones,
+    "YUE": 0,
 }
 
-if __name__ == "__main__":
-    a = set(zh_symbols)
-    b = set(en_symbols)
-    print(sorted(a & b))
```

</details>
