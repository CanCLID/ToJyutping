from __future__ import annotations
from typing import Dict, List, Literal, Optional, Tuple, Union, overload
if __package__:
	from .utils import format_romanization_text, format_ipa_text, g2p_with_puncts, jyutping2ipa
	from .Trie import Trie, CustomizableTrie
	from .PhonemesList import PhonemesList
else:
	from utils import format_romanization_text, format_ipa_text, g2p_with_puncts, jyutping2ipa
	from Trie import Trie, CustomizableTrie
	from PhonemesList import PhonemesList

class JyutpingConverter:
	def __init__(self, t: Trie):
		self.__t = t

	def get_jyutping_list(self, s: str) -> List[Tuple[str, Optional[str]]]:
		return self.__t.get(s, 'jyutping')

	def get_jyutping(self, s: str) -> str:
		return ''.join(k + (f'({v})' if v else '') for k, v in self.get_jyutping_list(s))

	def get_jyutping_text(self, s: str) -> str:
		return format_romanization_text(s, self.get_jyutping_list)

	def get_jyutping_candidates(self, s: str) -> List[Tuple[str, List[str]]]:
		return self.__t.get_all(s, 'jyutping')

	def get_ipa_list(self, s: str) -> List[Tuple[str, Optional[str]]]:
		return self.__t.get(s, 'ipa')

	def get_ipa(self, s: str) -> str:
		return ''.join(k + (f'[{v}]' if v else '') for k, v in self.get_ipa_list(s))

	def get_ipa_text(self, s: str) -> str:
		return format_ipa_text(s, self.get_ipa_list)

	def get_ipa_candidates(self, s: str) -> List[Tuple[str, List[str]]]:
		return self.__t.get_all(s, 'ipa')

	def customize(self, entries: Dict[str, Optional[Union[List[str], str]]]) -> JyutpingConverter:
		t = CustomizableTrie(self.__t)
		converter = JyutpingConverter(t)
		for k, v in entries.items():
			if not k: raise ValueError(f"Error customizing value {v!r}: Empty key")
			t.customize(k, v)
		return converter

	@overload
	def g2p(self, s: str, offset: Optional[Union[int, Tuple[int, int, int]]] = None, puncts_offset: Optional[int] = None, *, tone_same_seq = False, minimal: Literal[False] = False, extra_puncts: Optional[Dict[str, int]] = None, puncts_map: Optional[Dict[str, int]] = None, unknown_id: Optional[int] = None, decimal_check = True) -> PhonemesList[Tuple[int, int, int]]: ...

	@overload
	def g2p(self, s: str, offset: Optional[Union[int, Tuple[int, int, int, int]]] = None, puncts_offset: Optional[int] = None, *, tone_same_seq = False, minimal: Literal[True], extra_puncts: Optional[Dict[str, int]] = None, puncts_map: Optional[Dict[str, int]] = None, unknown_id: Optional[int] = None, decimal_check = True) -> PhonemesList[Tuple[int, int, int, int]]: ...

	def g2p(self, s: str, offset: Optional[Union[int, Tuple[int, int, int], Tuple[int, int, int, int]]] = None, puncts_offset: Optional[int] = None, *, tone_same_seq = False, minimal = False, extra_puncts: Optional[Dict[str, int]] = None, puncts_map: Optional[Dict[str, int]] = None, unknown_id: Optional[int] = None, decimal_check = True) -> Union[PhonemesList[Tuple[int, int, int]], PhonemesList[Tuple[int, int, int, int]]]:
		if extra_puncts is not None and puncts_map is not None:
			raise ValueError("'extra_puncts' and 'puncts_map' must not be specified simultaneously")
		if puncts_map is not None and unknown_id is None:
			raise ValueError("'unknown_id' must be provided if 'puncts_map' is specified")
		return g2p_with_puncts(self.__t.get(s), offset=offset, puncts_offset=puncts_offset, tone_same_seq=tone_same_seq, minimal=minimal, extra_puncts=extra_puncts, puncts_map=puncts_map, unknown_id=unknown_id, decimal_check=decimal_check)

	# This method exists purely due to compatibility. It is the same across all `JyutpingConverter` instances.
	jyutping2ipa = jyutping2ipa

ToJyutping = JyutpingConverter(Trie())
