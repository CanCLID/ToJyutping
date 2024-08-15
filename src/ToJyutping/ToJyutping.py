from os import path
from typing import Dict, List, Literal, Optional, Tuple, Union, overload
import re
if __package__:
	from .utils import format_romanization_text, format_ipa_text, g2p_with_puncts
	from .Trie import Trie
	from .Jyutping import Jyutping
	from .PhonemesList import PhonemesList
else:
	from utils import format_romanization_text, format_ipa_text, g2p_with_puncts
	from Trie import Trie
	from Jyutping import Jyutping
	from PhonemesList import PhonemesList

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'trie.txt'), encoding='utf-8') as f:
	t = Trie(f.read())

def get_jyutping_list(s: str) -> List[Tuple[str, Optional[str]]]:
	return t.get(s, 'jyutping')

def get_jyutping(s: str) -> str:
	return ''.join(k + (f'({v})' if v else '') for k, v in get_jyutping_list(s))

def get_jyutping_text(s: str) -> str:
	return format_romanization_text(s, get_jyutping_list)

def get_jyutping_candidates(s: str) -> List[Tuple[str, List[str]]]:
	return t.get_all(s, 'jyutping')

def get_ipa_list(s: str) -> List[Tuple[str, Optional[str]]]:
	return t.get(s, 'ipa')

def get_ipa(s: str) -> str:
	return ''.join(k + (f'[{v}]' if v else '') for k, v in get_ipa_list(s))

def get_ipa_text(s: str) -> str:
	return format_ipa_text(s, get_ipa_list)

def get_ipa_candidates(s: str) -> List[Tuple[str, List[str]]]:
	return t.get_all(s, 'ipa')

@overload
def g2p(s: str, offset: Optional[Union[int, Tuple[int, int, int]]] = None, puncts_offset: Optional[int] = None, *, tone_same_seq = False, minimal: Literal[False] = False, extra_puncts: Optional[Dict[str, int]] = None, puncts_map: Optional[Dict[str, int]] = None, unknown_id: Optional[int] = None, decimal_check = True) -> PhonemesList[Tuple[int, int, int]]: ...

@overload
def g2p(s: str, offset: Optional[Union[int, Tuple[int, int, int, int]]] = None, puncts_offset: Optional[int] = None, *, tone_same_seq = False, minimal: Literal[True], extra_puncts: Optional[Dict[str, int]] = None, puncts_map: Optional[Dict[str, int]] = None, unknown_id: Optional[int] = None, decimal_check = True) -> PhonemesList[Tuple[int, int, int, int]]: ...

def g2p(s: str, offset: Optional[Union[int, Tuple[int, int, int], Tuple[int, int, int, int]]] = None, puncts_offset: Optional[int] = None, *, tone_same_seq = False, minimal = False, extra_puncts: Optional[Dict[str, int]] = None, puncts_map: Optional[Dict[str, int]] = None, unknown_id: Optional[int] = None, decimal_check = True) -> Union[PhonemesList[Tuple[int, int, int]], PhonemesList[Tuple[int, int, int, int]]]:
	if extra_puncts is not None and puncts_map is not None:
		raise ValueError("'extra_puncts' and 'puncts_map' must not be specified simultaneously")
	if puncts_map is not None and unknown_id is None:
		raise ValueError("'unknown_id' must be provided if 'puncts_map' is specified")
	if unknown_id is not None and puncts_map is None:
		raise ValueError("'unknown_id' cannot be changed if 'puncts_map' is not specified")
	return g2p_with_puncts(t.get(s), offset=offset, puncts_offset=puncts_offset, tone_same_seq=tone_same_seq, minimal=minimal, extra_puncts=extra_puncts, puncts_map=puncts_map, unknown_id=unknown_id, decimal_check=decimal_check)

def jyutping2ipa(s: str) -> str:
	return '.'.join(Jyutping(t).ipa for t in re.split('\\W+', s.lower()))
