from typing import DefaultDict, Dict, List, Literal, Optional, Tuple, Union, overload
from functools import reduce
from collections import defaultdict
from operator import itemgetter
if __package__:
	from . import utils
	from . import Jyutping
else:
	import utils
	import Jyutping

class Node(Dict[str, 'Node']):
	v: Optional[List[Union[Jyutping.Jyutping, Jyutping.JyutpingList]]] = None

class Trie:
	def __init__(self, s: str):
		self.t = Node()
		n = [self.t]
		i = 1
		while n:
			j = i
			while ord(s[j]) >= 256:
				j += 1
			f = reduce(lambda t, c: t.setdefault(c, Node()), s[i:j], n[-1])
			i = j
			while ord(s[j]) < 123 or s[j] == '|':
				j += 1
			if i != j:
				f.v = [Jyutping.Jyutping(next(Jyutping.to_id(x))) if len(x) == 2 else Jyutping.JyutpingList(Jyutping.Jyutping(s) for s in Jyutping.to_id(x)) for x in s[i:j].split('|')]
				i = j
			if s[i] == '{':
				i += 1
				n.append(f)
			elif s[i] == '}':
				i += 1
				n.pop()

	@overload
	def get(self, s: str, attr: Literal['jyutping', 'ipa']) -> List[Tuple[str, Optional[str]]]: ...

	@overload
	def get(self, s: str, attr: None = None) -> List[Tuple[str, Optional[Union[Jyutping.Jyutping, Jyutping.JyutpingList]]]]: ...

	def get(self, s: str, attr: Optional[Literal['jyutping', 'ipa']] = None):
		r: List[Tuple[str, Optional[Union[str, Jyutping.Jyutping, Jyutping.JyutpingList]]]] = []
		i = 0
		while i < len(s):
			t = self.t
			c = None
			k = i
			for j in range(i, len(s)):
				u = t.get(s[j])
				if u is None:
					break
				t = u
				if t.v:
					c = t.v[0]
					k = j
			if k == i:
				r.append((s[i], getattr(c, attr, None) if attr else c))
				i += 1
			elif c:
				n = i
				while i <= k:
					r.append((s[i], getattr(c[i - n], attr, None) if attr else c[i - n]))
					i += 1
		return r

	@overload
	def get_all(self, s: str, attr: Literal['jyutping', 'ipa']) -> List[Tuple[str, List[str]]]: ...

	@overload
	def get_all(self, s: str, attr: None = None) -> List[Tuple[str, List[Union[Jyutping.Jyutping, Jyutping.JyutpingList]]]]: ...

	def get_all(self, s: str, attr: Optional[Literal['jyutping', 'ipa']] = None) -> List[Tuple[str, List[Union[str, Jyutping.Jyutping, Jyutping.JyutpingList]]]]:
		t = self.t
		def initialize(c: str):
			d = defaultdict(list)
			u = t.get(c)
			if u is not None and u.v:
				d[0] = [getattr(p, attr, None) for p in u.v] if attr else u.v
			return d
		r: List[Tuple[str, DefaultDict[int, List[Union[str, Jyutping.Jyutping, Jyutping.JyutpingList]]]]] = [(c, initialize(c)) for c in s]
		for i in range(len(r)):
			u = t.get(r[i][0])
			if u is None:
				continue
			for j in range(i + 1, len(r)):
				u = u.get(r[j][0])
				if u is None:
					break
				if u.v:
					l = j - i
					for p in u.v:
						for k in range(i, j + 1):
							r[k][1][l].append(getattr(p[k - i], attr, None) if attr else p[k - i])
		return [(c, utils.flat_dedupe(map(itemgetter(1), sorted(s.items(), key=itemgetter(0), reverse=True)))) for c, s in r]
