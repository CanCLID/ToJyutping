from os import path
from typing import List, Optional, Tuple
import re
if __package__:
	from . import utils
	from . import Trie
else:
	import utils
	import Trie

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'trie.txt'), encoding='utf-8') as f:
	t = Trie.Trie(f.read())

def get_jyutping_list(s: str) -> List[Tuple[str, Optional[str]]]:
	return t.get(s)

def get_jyutping(s: str) -> str:
	l = ''
	for k, v in get_jyutping_list(s):
		l += k + (f'({v})' if v else '')
	return l

def get_jyutping_text(s: str) -> str:
	return utils.format_romanization_text(s, get_jyutping_list)

def get_jyutping_candidates(s: str) -> List[Tuple[str, List[str]]]:
	return t.get_all(s)

def get_ipa_list(s: str) -> List[Tuple[str, Optional[str]]]:
	return [(k, v and jyutping2ipa(v)) for k, v in get_jyutping_list(s)]

def get_ipa(s: str) -> str:
	l = ''
	for k, v in get_jyutping_list(s):
		l += k + (f'[{jyutping2ipa(v)}]' if v else '')
	return l

def get_ipa_text(s: str) -> str:
	return utils.format_ipa_text(s, get_ipa_list)

def get_ipa_candidates(s: str) -> List[Tuple[str, List[str]]]:
	return [(k, list(map(jyutping2ipa, v))) for k, v in t.get_all(s)]

onset = { 'b': 'p', 'p': 'pʰ', 'm': 'm', 'f': 'f', 'd': 't', 't': 'tʰ', 'n': 'n', 'l': 'l', 'g': 'k', 'k': 'kʰ',
		  'ng': 'ŋ', 'gw': 'kʷ', 'kw': 'kʷʰ', 'w': 'w', 'h': 'h', 'z': 't͡s', 'c': 't͡sʰ', 's': 's', 'j': 'j' }
nucleus = { 'aa': 'aː', 'a': 'ɐ', 'e': 'ɛː', 'i': 'iː', 'o': 'ɔː', 'u': 'uː', 'oe': 'œː', 'eo': 'ɵ', 'yu': 'yː' }
rhyme = { 'ei': 'ei̯', 'ing': 'eŋ', 'ik': 'ek̚', 'ou': 'ou̯', 'ung': 'oŋ', 'uk': 'ok̚', 'eoi': 'ɵy̑', 'm': 'm̩', 'ng': 'ŋ̍' }
coda = { 'i': 'i̯', 'u': 'u̯', 'm': 'm', 'n': 'n', 'ng': 'ŋ', 'p': 'p̚', 't': 't̚', 'k': 'k̚' }
tone = { '1': '˥', '2': '˧˥', '3': '˧', '4': '˨˩', '5': '˩˧', '6': '˨' }

regex = re.compile('^([gk]w?|ng|[bpmfdtnlhwzcsj]?)(?![1-6]$)((aa?|oe?|eo?|y?u|i?)(ng|[iumnptk]?))([1-6])$')

def jyutping2ipa(s: str) -> str:
	return '.'.join([
		(lambda initial, final, vowel, terminal, number: (
			(initial and onset[initial]) +
			rhyme.get(final, (vowel and nucleus[vowel]) + (terminal and coda[terminal])) +
			(number and tone[number])
		))(*re.match(regex, t).groups()) for t in re.split('\\W+', s.lower())
	])
