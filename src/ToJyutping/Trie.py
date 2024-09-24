from __future__ import annotations
from os import path
from typing import Dict, List, Literal, Optional, Tuple, Union, overload # , override # requires Python 3.12
from weakref import WeakKeyDictionary
from functools import reduce
if __package__:
	from .utils import EdgeLengthToItems, dedupe, flat_dedupe, extract_alnum
	from .Jyutping import Jyutping, JyutpingList
else:
	from utils import EdgeLengthToItems, dedupe, flat_dedupe, extract_alnum
	from Jyutping import Jyutping, JyutpingList

here = path.abspath(path.dirname(__file__))

class Node(Dict[str, 'Node']):
	v: Optional[List[Union[Jyutping, JyutpingList]]] = None
	m: Optional[WeakKeyDictionary[Trie, Optional[List[Union[Jyutping, JyutpingList]]]]] = None

def set_default_node(n: Node, c: str):
	return n.setdefault(c, Node())

def parse_jyutping(k: str, x: str):
	if not x: raise ValueError('Empty value')
	l = extract_alnum(x)
	if not l: raise ValueError(f'There are no jyutping syllables in {x!r}')
	if len(k) not in {1, len(l)}: raise ValueError(f'Mismatched number of syllables: There must be {len(k)} syllables in {x!r}')
	return (next if len(l) == 1 else JyutpingList)(map(Jyutping, l))

with open(path.join(here, 'trie.txt'), encoding='utf-8') as f:
	s = f.read()
del f

root = Node()
n = [root]
l = [0]
i = 1
while n:
	p = n[-1]
	d = l[-1]
	while ord(s[i]) >= 256:
		p = set_default_node(p, s[i])
		i += 1
		d += 1
	v = []
	while ord(s[i]) < 123:
		c = 0
		w = JyutpingList()
		while c < d:
			w.append(Jyutping((ord(s[i]) - 33) * 90 + (ord(s[i + 1]) - 33)))
			i += 2
			if s[i] == '~': i += 1
			else: c += 1
		v.append(w[0] if len(w) == 1 else w)
	if v:
		p.v = v
	if s[i] == '{':
		i += 1
		n.append(p)
		l.append(d)
	elif s[i] == '}':
		i += 1
		n.pop()
		l.pop()
del n
del l
del s

class Trie:
	@overload
	def get(self, s: str, attr: Literal['jyutping', 'ipa']) -> List[Tuple[str, Optional[str]]]: ...

	@overload
	def get(self, s: str, attr: None = None) -> List[Tuple[str, Optional[Union[Jyutping, JyutpingList]]]]: ...

	def get(self, s: str, attr: Optional[Literal['jyutping', 'ipa']] = None):
		r: List[Tuple[str, Optional[Union[str, Jyutping, JyutpingList]]]] = []
		i = 0
		while i < len(s):
			t = root
			c = None
			k = i
			for j in range(i, len(s)):
				u = t.get(s[j])
				if u is None:
					break
				t = u
				v = self.get_value(t)
				if v:
					c = v[0]
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
	def get_all(self, s: str, attr: None = None) -> List[Tuple[str, List[Union[Jyutping, JyutpingList]]]]: ...

	def get_all(self, s: str, attr: Optional[Literal['jyutping', 'ipa']] = None) -> List[Tuple[str, List[Union[str, Jyutping, JyutpingList]]]]:
		t = root
		def initialize(c: str):
			d = EdgeLengthToItems()
			u = t.get(c)
			if u is not None:
				v = self.get_value(u)
				if v:
					d[0] = [getattr(p, attr, None) for p in v] if attr else v
			return d
		r: List[Tuple[str, EdgeLengthToItems[Union[str, Jyutping, JyutpingList]]]] = [(c, initialize(c)) for c in s]
		for i in range(len(r)):
			u = t.get(r[i][0])
			if u is None:
				continue
			for j in range(i + 1, len(r)):
				u = u.get(r[j][0])
				if u is None:
					break
				v = self.get_value(u)
				if v:
					l = j - i
					for p in v:
						for k in range(i, j + 1):
							r[k][1][l].append(getattr(p[k - i], attr, None) if attr else p[k - i])
		return [(c, flat_dedupe(s)) for c, s in r]

	def get_value(self, n: Node):
		return n.v

class CustomizableTrie(Trie):
	def __init__(self, parent: Trie):
		self.__parent = parent

	def customize(self, k: str, v: Optional[Union[List[str], str]]):
		n = reduce(set_default_node, k, root)
		if n.m is None:
			n.m = WeakKeyDictionary()
		try:
			n.m[self] = None if v is None or v == [] else [parse_jyutping(k, v)] if isinstance(v, str) else dedupe(parse_jyutping(k, x) for x in v)
		except Exception as err:
			raise ValueError(f'Error customizing key {k!r}: invalid value {v!r}') from err

	# @override
	def get_value(self, n: Node):
		# Fast path if `n.m` isn't defined
		return (n.m[self] if self in n.m else self.__parent.get_value(n)) if n.m else n.v
