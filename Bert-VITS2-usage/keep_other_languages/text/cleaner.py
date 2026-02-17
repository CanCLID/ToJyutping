import ToJyutping
import unicodedata

from text import chinese, japanese, english
from text.symbols import symbols, yue_offset

language_module_map = {"ZH": chinese, "JP": japanese, "EN": english}


def clean_text(text, language):
    text = unicodedata.normalize("NFC", text)
    if language == "YUE":
        # Already handles punctuation and maps to symbol IDs internally
        phonemes = ToJyutping.g2p(text, offset=(yue_offset, yue_offset, 1))
        norm_text = "".join(
            char if length > 1 else
            # Convert punctuation ID back to one of … . , ! ? - '
            symbols[phonemes.segmentals[sum(phonemes.lengths[:i])]] if length == 1 else ""
            for i, (char, length) in enumerate(zip(text, phonemes.lengths, strict=True))
        )
        lengths = [length for length in phonemes.lengths if length > 0]
        return norm_text, phonemes.segmentals, phonemes.tones, lengths
    language_module = language_module_map[language]
    norm_text = language_module.text_normalize(text)
    phones, tones, word2ph = language_module.g2p(norm_text)
    return norm_text, phones, tones, word2ph
