from typing import DefaultDict, Dict, List, Optional, Tuple
from functools import reduce
from itertools import starmap
from collections import defaultdict
from operator import itemgetter

class Node(Dict[str, 'Node']):
	v: Optional[List[str]] = None

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
				f.v = list(map(decode_jyutping, s[i:j].split('|')))
				i = j
			if s[i] == '{':
				i += 1
				n.append(f)
			elif s[i] == '}':
				i += 1
				n.pop()

	def get(self, s: str):
		r: List[Tuple[str, Optional[str]]] = []
		i = 0
		while i < len(s):
			t = self.t
			c = ''
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
				r.append((s[i], c or None))
				i += 1
			else:
				d = c.split(' ')
				n = i
				while i <= k:
					r.append((s[i], d[i - n]))
					i += 1
		return r

	def get_all(self, s: str) -> List[Tuple[str, List[str]]]:
		t = self.t
		def initialize(c: str):
			d = defaultdict(list)
			u = t.get(c)
			if u is not None and u.v:
				d[0] = u.v
			return d
		r: List[Tuple[str, DefaultDict[int, List[str]]]] = [(c, initialize(c)) for c in s]
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
						d = p.split(' ')
						for k in range(i, j + 1):
							r[k][1][l].append(d[k - i])
		return [(c, dedupe(map(itemgetter(1), sorted(s.items(), key=itemgetter(0), reverse=True)))) for c, s in r]

def dedupe(s):
	seen = set()
	seen_add = seen.add
	return [x for t in s for x in t if not (x in seen or seen_add(x))]

onset = ['', 'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'ng', 'gw', 'kw', 'w', 'h', 'z', 'c', 's', 'j']
nucleus = ['aa', 'a', 'e', 'i', 'o', 'u']
rhyme = ['oe', 'oen', 'oeng', 'oet', 'oek', 'eoi', 'eon', 'eot', 'yu', 'yun', 'yut', 'm', 'ng']
coda = ['', 'i', 'u', 'm', 'n', 'ng', 'p', 't', 'k']

def decode_jyutping(s: str) -> str:
	it = iter(s)
	def inner(x, y):
		order = (ord(x) - 33) * 90 + (ord(y) - 33)
		final = (order % 402) // 6
		return (
			onset[order // 402] +
			(rhyme[final - 54] if final >= 54 else nucleus[final // 9] + coda[final % 9]) +
			str((order % 6) + 1)
		)
	return ' '.join(starmap(inner, zip(it, it)))
