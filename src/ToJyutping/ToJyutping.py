from os import path
from typing import List, Literal, Optional, Tuple, Union, overload
from operator import attrgetter
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

_get_syllables = attrgetter("syllables")
_get_ipa = attrgetter("ipa")

def get_jyutping_list(s: str) -> List[Tuple[str, Optional[str]]]:
	return [(k, v and v.syllables) for k, v in t.get(s)]

def get_jyutping(s: str) -> str:
	l = ''
	for k, v in get_jyutping_list(s):
		l += k + (f'({v})' if v else '')
	return l

def get_jyutping_text(s: str) -> str:
	return utils.format_romanization_text(s, get_jyutping_list)

def get_jyutping_candidates(s: str) -> List[Tuple[str, List[str]]]:
	return [(k, list(map(_get_syllables, v))) for k, v in t.get_all(s)]

def get_ipa_list(s: str) -> List[Tuple[str, Optional[str]]]:
	return [(k, v and v.ipa) for k, v in t.get(s)]

def get_ipa(s: str) -> str:
	l = ''
	for k, v in get_ipa_list(s):
		l += k + (f'[{v}]' if v else '')
	return l

def get_ipa_text(s: str) -> str:
	return utils.format_ipa_text(s, get_ipa_list)

def get_ipa_candidates(s: str) -> List[Tuple[str, List[str]]]:
	return [(k, list(map(_get_ipa, v))) for k, v in t.get_all(s)]

@overload
def g2p(s: str, offset: int = 0, *, minimal: Literal[False] = False) -> List[Tuple[int, int, int]]: ...

@overload
def g2p(s: str, offset: int = 0, *, minimal: Literal[True]) -> List[Tuple[int, int, int, int]]: ...

def g2p(s: str, offset=0, minimal=False) -> Union[List[Tuple[int, int, int]], List[Tuple[int, int, int, int]]]:
	return [p.g2p(offset=offset, minimal=minimal) for k, v in t.get(s) for p in v or ()]

def jyutping2ipa(s: str) -> str:
	return '.'.join(Jyutping.Jyutping(t).ipa for t in re.split('\\W+', s.lower()))
