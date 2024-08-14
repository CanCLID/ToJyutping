from os import path
from typing import List, Literal, Optional, Tuple, Union, overload
import re
if __package__:
	from . import utils
	from . import Trie
	from . import Jyutping
else:
	import utils
	import Trie
	import Jyutping

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'trie.txt'), encoding='utf-8') as f:
	t = Trie.Trie(f.read())

def get_jyutping_list(s: str) -> List[Tuple[str, Optional[str]]]:
	return t.get(s, 'jyutping')

def get_jyutping(s: str) -> str:
	return ''.join(k + (f'({v})' if v else '') for k, v in get_jyutping_list(s))

def get_jyutping_text(s: str) -> str:
	return utils.format_romanization_text(s, get_jyutping_list)

def get_jyutping_candidates(s: str) -> List[Tuple[str, List[str]]]:
	return t.get_all(s, 'jyutping')

def get_ipa_list(s: str) -> List[Tuple[str, Optional[str]]]:
	return t.get(s, 'ipa')

def get_ipa(s: str) -> str:
	return ''.join(k + (f'[{v}]' if v else '') for k, v in get_ipa_list(s))

def get_ipa_text(s: str) -> str:
	return utils.format_ipa_text(s, get_ipa_list)

def get_ipa_candidates(s: str) -> List[Tuple[str, List[str]]]:
	return t.get_all(s, 'ipa')

@overload
def g2p(s: str, offset: Union[int, Tuple[int, int, int]] = 0, *, tone_same_seq = False, minimal: Literal[False] = False) -> List[Tuple[int, int, int]]: ...

@overload
def g2p(s: str, offset: Union[int, Tuple[int, int, int, int]] = 0, *, tone_same_seq = False, minimal: Literal[True]) -> List[Tuple[int, int, int, int]]: ...

def g2p(s: str, offset: Union[int, Tuple[int, int, int], Tuple[int, int, int, int]] = 0, *, tone_same_seq = False, minimal = False) -> Union[List[Tuple[int, int, int]], List[Tuple[int, int, int, int]]]:
	return [p.g2p(offset=offset, tone_same_seq=tone_same_seq, minimal=minimal) for k, v in t.get(s) for p in (v if isinstance(v, list) else v and (v,) or ())]

def jyutping2ipa(s: str) -> str:
	return '.'.join(Jyutping.Jyutping(t).ipa for t in re.split('\\W+', s.lower()))
