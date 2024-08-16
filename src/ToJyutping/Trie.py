from __future__ import annotations
from os import path
from typing import Dict, List, Literal, Optional, Tuple, Union, overload # , override # requires Python 3.12
from weakref import WeakKeyDictionary
from functools import reduce
if __package__:
	from .utils import EdgeLengthToItems, dedupe, flat_dedupe, extract_alnum
	from .Jyutping import Jyutping, JyutpingList, to_id
else:
	from utils import EdgeLengthToItems, dedupe, flat_dedupe, extract_alnum
	from Jyutping import Jyutping, JyutpingList, to_id

here = path.abspath(path.dirname(__file__))

class Node(Dict[str, 'Node']):
	v: Optional[List[Union[Jyutping, JyutpingList]]] = None
	m: Optional[WeakKeyDictionary[Trie, Optional[List[Union[Jyutping, JyutpingList]]]]] = None

def set_default_node(t: Trie, c: str):
	return t.setdefault(c, Node())

def parse_jyutping(k: str, x: str):
	assert x, 'String must not be empty'
	l = extract_alnum(x)
	assert l, f'There are no alphanumeric characters in the string {x!r}'
	assert len(k) in {1, len(l)}, f'Mismatched number of syllables: {l!r} must be of length {len(k)}'
	return (next if len(l) == 1 else JyutpingList)(map(Jyutping, l))

with open(path.join(here, 'trie.txt'), encoding='utf-8') as f:
	s = f.read()

root = Node()
n = [root]
i = 1
while n:
	j = i
	while ord(s[j]) >= 256:
		j += 1
	f = reduce(set_default_node, s[i:j], n[-1])
	i = j
	while ord(s[j]) < 123 or s[j] == '|':
		j += 1
	if i != j:
		f.v = [Jyutping(next(to_id(x))) if len(x) == 2 else JyutpingList(Jyutping(s) for s in to_id(x)) for x in s[i:j].split('|')]
		i = j
	if s[i] == '{':
		i += 1
		n.append(f)
	elif s[i] == '}':
		i += 1
		n.pop()

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
	
	def customize(self, k: str, v: Optional[List[str]]):
		n = reduce(set_default_node, k, root)
		if n.m is None:
			n.m = WeakKeyDictionary()
		n.m[self] = v and dedupe(parse_jyutping(k, x) for x in v)

	# @override
	def get_value(self, n: Node):
		# Fast path if `n.m` isn't defined
		return (n.m[self] if self in n.m else self.__parent.get_value(n)) if n.m else n.v
