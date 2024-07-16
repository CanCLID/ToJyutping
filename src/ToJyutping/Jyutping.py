from typing import List, Literal, Tuple, Union, overload
from itertools import starmap
from dataclasses import dataclass
from functools import cached_property
from operator import attrgetter
import re
import warnings

def to_id(s: str) -> List[int]:
	it = iter(s)
	return starmap(lambda x, y: (ord(x) - 33) * 90 + (ord(y) - 33), zip(it, it))

onset = ['', 'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'ng', 'gw', 'kw', 'w', 'h', 'z', 'c', 's', 'j']
nucleus = ['aa', 'a', 'e', 'i', 'o', 'u']  
rhyme = ['oe', 'oen', 'oeng', 'oet', 'oek', 'eoi', 'eon', 'eot', 'yu', 'yun', 'yut', 'm', 'ng']
coda = ['', 'i', 'u', 'm', 'n', 'ng', 'p', 't', 'k']

regex = re.compile('^([gk]w?|ng|[bpmfdtnlhwzcsj]?)(?![1-6]?$)((aa?|oe?|eo?|y?u|i?)(ng|[iumnptk]?))([1-6]?)$')

onset_ipa = ['', 'p', 'pʰ', 'm', 'f', 't', 'tʰ', 'n', 'l', 'k', 'kʰ', 'ŋ', 'kʷ', 'kʷʰ', 'w', 'h', 't͡s', 't͡sʰ', 's', 'j']
nucleus_ipa = ['aː', 'ɐ', 'ɛː', 'iː', 'ɔː', 'uː', 'œː', 'ɵ', 'yː']
coda_ipa = ['', 'i̯', 'u̯', 'm', 'n', 'ŋ', 'p̚', 't̚', 'k̚']
tone_ipa = ['˥', '˧˥', '˧', '˨˩', '˩˧', '˨']

nucleus_map = dict(zip([*nucleus, 'oe', 'eo', 'yu'], nucleus_ipa))
coda_map = dict(zip(coda, coda_ipa))
rhyme_ipa = {
	**{ i: nucleus_map[r[:2]] + coda_map[r[2:]] for i, r in enumerate(rhyme[:-2], 54) },
	19: 'ei̯', 32: 'eŋ', 35: 'ek̚', 38: 'ou̯', 50: 'oŋ', 53: 'ok̚', 59: 'ɵy̑', 65: 'm̩', 66: 'ŋ̍'
}

_minimal_mapping_nucleus_map = { 'oe': 26, 'eo': 26, 'yu': 27 }
_minimal_mapping_nucleus_to_onset = { 3: 19, 5: 14 }
_minimal_mapping_coda_to_onset = [0, 19, 14, 3, 7, 11, 1, 5, 9]
_minimal_mapping_rhyme_to_nucleus = {
	**{ i: _minimal_mapping_nucleus_map[r[:2]] for i, r in enumerate(rhyme[:-2], 54) },
	19: 23, 32: 23, 35: 23, 38: 25, 50: 25, 53: 25, 65: 0, 66: 0
}
_minimal_mapping_rhyme_to_coda = {
	**{ i: _minimal_mapping_coda_to_onset[coda.index(r[2:])] for i, r in enumerate(rhyme[:-2], 54) },
	0: 20, 9: 21, 18: 22, 27: 19, 36: 24, 45: 14, 54: 26, 62: 27, 65: 3, 66: 11
}

@dataclass(frozen=True)
class Jyutping:
	id: int
	onset_id: int
	onset: str
	rhyme_id: int
	rhyme: str
	tone_id: int
	tone: str
	syllable: str

	def __init__(self, x: Union[str, int]):
		if type(x) == int:
			object.__setattr__(self, "id", x)
			object.__setattr__(self, "onset_id", x // 402)
			object.__setattr__(self, "onset", onset[self.onset_id])
			object.__setattr__(self, "rhyme_id", (x % 402) // 6)
			object.__setattr__(self, "rhyme", rhyme[self.rhyme_id - 54] if self.rhyme_id >= 54 else nucleus[self.rhyme_id // 9] + coda[self.rhyme_id % 9])
			object.__setattr__(self, "tone_id", x % 6)
			object.__setattr__(self, "tone", str(self.tone_id + 1))
			object.__setattr__(self, "syllable", self.onset + self.rhyme + self.tone)
		else:
			object.__setattr__(self, "syllable", x)
			_onset, _rhyme, _nucleus, _coda, _tone = re.match(regex, x).groups()
			object.__setattr__(self, "onset", _onset)
			object.__setattr__(self, "onset_id", onset.index(_onset))
			object.__setattr__(self, "rhyme", _rhyme)
			try:
				object.__setattr__(self, "rhyme_id", rhyme.index(_rhyme) + 54)
			except ValueError:
				object.__setattr__(self, "rhyme_id", coda.index(_coda) + nucleus.index(_nucleus) * 9)
			object.__setattr__(self, "tone", _tone)
			object.__setattr__(self, "tone_id", int(_tone) - 1)
			object.__setattr__(self, "id", self.tone_id + self.rhyme_id * 6 + self.onset_id * 402)

	def __str__(self):
		return self.syllable

	def __eq__(self, other):
		return isinstance(other, Jyutping) and self.id == other.id
	
	def __hash__(self):
		return hash(self.id)

	@cached_property
	def ipa(self) -> str:
		return (
			onset_ipa[self.onset_id] +
			rhyme_ipa.get(self.rhyme_id, nucleus_ipa[self.rhyme_id // 9] + coda_ipa[self.rhyme_id % 9]) +
			tone_ipa[self.tone_id]
		)

	@overload
	def g2p(self, offset: int = 0, *, minimal: Literal[False] = False) -> Tuple[int, int, int]: ...

	@overload
	def g2p(self, offset: int = 0, *, minimal: Literal[True]) -> Tuple[int, int, int, int]: ...

	def g2p(self, offset=0, *, minimal=False) -> Union[Tuple[int, int, int], Tuple[int, int, int, int]]:
		if minimal:
			warnings.warn('`minimal` is an experimental feature and is subject to changes or removal in the future.')
			return (
				self.onset_id + offset,
				_minimal_mapping_rhyme_to_nucleus.get(self.rhyme_id, _minimal_mapping_nucleus_to_onset.get(self.rhyme_id // 9, self.rhyme_id // 9 + 20)) + offset,
				_minimal_mapping_rhyme_to_coda.get(self.rhyme_id, _minimal_mapping_coda_to_onset[self.rhyme_id % 9]) + offset,
				self.tone_id + 28 + offset,
			)
		return (self.onset_id + offset, self.rhyme_id + 20 + offset, self.tone_id + 87 + offset)

class JyutpingList(List[Jyutping]):
	@property
	def syllables(self):
		return ' '.join(map(attrgetter('syllable'), self))

	@property
	def ipa(self):
		return '.'.join(map(attrgetter('ipa'), self))

	def __str__(self):
		return self.syllables

	def __hash__(self):
		return hash(tuple(self))

	def __getslice__(self, i, j):
		return JyutpingList(list.__getslice__(self, i, j))

	def __add__(self, other):
		return JyutpingList(list.__add__(self, other))

	def __mul__(self, other):
		return JyutpingList(list.__mul__(self, other))
