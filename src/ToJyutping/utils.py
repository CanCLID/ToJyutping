from typing import DefaultDict, List, TypeVar
import re

punct_dict = dict(
	zip(
		'''!"'(),-./:;?[]{}~·‐‑‒–—―‘’“”…⋮⋯⸱⸳⸺⸻、。〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟・︐︑︒︓︔︕︖︗︘︙︱︲︵︶︷︸︹︺︻︼︽︾︿﹀﹁﹂﹃﹄﹇﹈﹐﹑﹒﹔﹕﹖﹗﹘﹙﹚﹛﹜﹝﹞﹣！＂＇（），－．／：；？［］｛｝～｟｠｡｢｣､･''',
		'''!"'(),-./:;?[]{}~·------‘’“”………··--,.‘’“”“”‘’[][][][][]~“””·,,.:;!?[]…--(){}[][]“”‘’“”‘’[],,.;:?!-(){}[]-!"'(),-./:;?[]{}~().“”,·'''
	)
)

left_bracket = '([{‘“'
right_bracket = ')]}’”'
left_bracket_to_right = dict(zip(left_bracket, right_bracket))
left_bracket = {*left_bracket}
right_bracket = {*right_bracket}
left_punct = {*left_bracket}
right_punct = {*'!,.:;?…', *right_bracket}
other_punct = {*'''"'·-~'''}
left_or_other_punct = {' ', *left_punct, *other_punct}
right_or_other_punct = {*right_punct, *other_punct}

minus_signs = {*'-﹣－'}  # U+2212 is unnecessary
decimal_seps = {*'''',.·⸱⸳﹒＇．'''}
digits = {*'0０𝟎𝟘𝟢𝟬𝟶🯰1１𝟏𝟙𝟣𝟭𝟷🯱2２𝟐𝟚𝟤𝟮𝟸🯲3３𝟑𝟛𝟥𝟯𝟹🯳4４𝟒𝟜𝟦𝟰𝟺🯴5５𝟓𝟝𝟧𝟱𝟻🯵6６𝟔𝟞𝟨𝟲𝟼🯶7７𝟕𝟟𝟩𝟳𝟽🯷8８𝟖𝟠𝟪𝟴𝟾🯸9９𝟗𝟡𝟫𝟵𝟿🯹'}
unknown_or_hyphen = {'', '-'}

def format_romanization_text(s, conv):
	def inner(m):
		t = [None]
		d = [None]
		for k, v in conv(m[0]):
			if v:
				t += [v]
				d += [None]
			elif not k.isspace():
				t += [punct_dict.get(k, '')]
				d += [k]
		t += [None]
		d += [None]
		l = ''
		b = ''
		for i, (p, c, n) in enumerate(zip(t, t[1:], t[2:]), 1):
			def between():
				nonlocal t, i
				j = i - 1
				while j and t[j] in right_bracket:
					j -= 1
				f = j and t[j] and len(t[j]) > 1
				j = i + 1
				while j < len(t) - 1 and t[j] in left_bracket:
					j += 1
				g = j and t[j] and len(t[j]) > 1
				return f and g

			def lspace():
				nonlocal l
				if l and l[-1] not in left_or_other_punct:
					l += ' '

			def rspace():
				nonlocal n, l
				if i < len(d) - 2 and d[i + 2] in digits if d[i + 1] in minus_signs else n not in right_or_other_punct:
					l += ' '

			if len(c) > 1:
				lspace()
				l += c
				rspace()
			elif not c or d[i] in minus_signs and d[i + 1] in digits and p not in unknown_or_hyphen:
				if not l.endswith('[…]'):
					l += '[…]'
			elif d[i] in decimal_seps and d[i + 1] in digits and d[i - 1] in digits:
				continue
			elif c in left_punct:
				lspace()
				l += c
				b += left_bracket_to_right[c]
			elif c in right_punct:
				l += c
				rspace()
				try:
					b = b[:b.rindex(c)]
				except ValueError:
					pass
			elif c == '-':
				if p == '-':
					continue
				if n == '-' or between():
					l += ' – '
				else:
					l += c
			elif c == '~':
				if p == '~' and n != '~' or between():
					l += '~ '
				else:
					l += c
			elif c == '·':
				l += c
			else:
				j = len(b) - 1
				y = False
				while j >= 0 and b[j] not in right_bracket:
					if b[j] == c:
						y = True
						break
					j -= 1
				if y:
					b = b[:j]
					l += c
					rspace()
				else:
					lspace()
					l += c
					b += c
		return ' '.join(l.split())

	return re.sub(r'[^\0-\x1f\x80-\x9f]+', inner, s)

major_break = {*'.!?…'}
minor_break = {*',/:;-~()[]{}'}

def format_ipa_text(s, conv):
	def inner(m):
		t = []
		d = []
		for k, v in conv(m[0]):
			if v:
				t += [v]
				d += [None]
			elif not k.isspace():
				t += [punct_dict.get(k, '')]
				d += [k]
		d += [None]
		l = []
		for i, c in enumerate(t):
			if len(c) > 1:
				l += [c]
			elif not c or d[i] in minus_signs and d[i + 1] in digits and i and t[i - 1] not in unknown_or_hyphen:
				if not l or l[-1] != '⸨…⸩':
					l += ['⸨…⸩']
			elif l:
				if d[i] in decimal_seps and d[i + 1] in digits and i and d[i - 1] in digits:
					continue
				if c in major_break:
					if len(l[-1]) > 1:
						l += ['‖']
					else:
						l[-1] = '‖'
				elif c in minor_break and len(l[-1]) > 1:
						l += ['|']
		if len(l[-1]) == 1:
			l.pop()
		s = ''
		for i, c in enumerate(l):
			s += c
			if i < len(l) - 1:
				n = l[i + 1]
				if c != '⸨…⸩' and len(c) > 1 and n != '⸨…⸩' and len(n) > 1:
					s += '.'
				else:
					s += ' '
		return s

	return re.sub(r'[^\0-\x1f\x80-\x9f]+', inner, s)

def flat_dedupe(s):
	seen = set()
	seen_add = seen.add
	return [x for t in s for x in t if not (x in seen or seen_add(x))]

def is_iterable(o):
	try:
		iter(o)
	except TypeError:
		return False
	return True

T = TypeVar('T')

class EdgeLengthToItems(DefaultDict[int, List[T]]):
	def __init__(self):
		super().__init__(list)
		self.max = 0

	def __missing__(self, index: int):
		result = super().__missing__(index)
		self[index] = result
		if index > self.max: self.max = index
		return result

	def __iter__(self):
		return map(super().__getitem__, range(self.max, -1, -1))
