# -*- coding: utf-8 -*-

from opencc import OpenCC
from os import path
import pygtrie
import re
import urllib.request

here = path.abspath(path.dirname(__file__))

# Initialize

cc_s = OpenCC('s2t.json')  # TODO: Cannot handle 沈
#cc_hk = OpenCC('hk2t.json')  # Wait for https://github.com/BYVoid/OpenCC/issues/406

t = pygtrie.CharTrie()
with open(path.join(here, 'jyut6ping3.simple.dict.yaml')) as f:
	for line in f:
		k, v = line.rstrip().split('\t')
		t[k] = v
DICT = t

def get_jyutping_list(s):
	def replace_words_plain(s, t):
		#s_t = cc_hk.convert(cc_s.convert(s))
		s_t = cc_s.convert(s)
		l = []  # list of converted words
		while s:
			longest_prefix = t.longest_prefix(s_t)  # match the longest prefix
			if not longest_prefix:  # if the prefix does not exist
				l.append((s[0], None))  # append (the first character, no result)
				s = s[1:]  # remove the first character from the string
				s_t = s_t[1:]
			else:  # if exists
				word, jyut = longest_prefix.key, longest_prefix.value
				if len(word) == 1:
					l.append((s[0], jyut))
					s = s[1:]  # remove the word from the string
					s_t = s_t[1:]
				else:
					for k, v in zip(s[:len(word)], jyut.split(' ')):
						l.append((k, v))
					s = s[len(word):]  # remove the word from the string
					s_t = s_t[len(word):]  # remove the word from the string
		return l  # A list of chars and jyutping

	return replace_words_plain(s, DICT)

def get_jyutping(s):
	l = []
	for k, v in get_jyutping_list(s):
		if v is None:
			l.append(k)
		else:
			l.append(k + '(' + v + ')')
	return ''.join(l)

def get_ipa(s):
	l = []
	for k, v in get_jyutping_list(s):
		if v is None:
			l.append(k)
		else:
			l.append(k + '(' + jyutping2ipa(v) + ')')
	return ''.join(l)

# Reference: https://github.com/rime/rime-cantonese/blob/de0d5b594d03a534cb8b4de891b4ef1059da349b/jyut6ping3_ipa.schema.yaml#L115-L188
def jyutping2ipa(str):
	str = re.sub(r"(^|[ '])(m)(qq?|xx?|vv?)?($|[ '])", r"\1\2̩\3\4", str)
	str = re.sub(r"(^|[ '])(ng)(qq?|xx?|vv?)?($|[ '])", r"\1\2̍\3\4", str)
	str = re.sub(r"([ptk])qq", r"\1˨", str)
	str = re.sub(r"([ptk])q", r"\1˧", str)
	str = re.sub(r"([ptk])v", r"\1˥", str)
	str = re.sub(r"vv", r"˨˩", str)
	str = re.sub(r"v", r"˥", str)
	str = re.sub(r"xx", r"˩˧", str)
	str = re.sub(r"x", r"˧˥", str)
	str = re.sub(r"qq", r"˨", str)
	str = re.sub(r"(^|[ '])q", r"\1ʔ", str)
	str = re.sub(r"q", r"˧", str)
	str = re.sub(r"([PTK])$", r"\1]", str)  # Originally \2, which is wrong
	str = re.sub(r"(^|[ '])([jy])u(ng)", r"\1jʊŋ", str)
	str = re.sub(r"(^|[ '])(jy|[jy])u([t])", r"\1jYː\3]", str)
	str = re.sub(r"([dtlgkhzcsj])yu([t])", r"\1Yː\2]", str)
	str = re.sub(r"(^|[ '])([jy])u([k])", r"\1jʊ\3]", str)
	str = re.sub(r"(^|[ '])(jy)u", r"\1jYː", str)
	str = re.sub(r"yu", r"Yː", str)
	str = re.sub(r"y([aeior])", r"j\1", str)
	str = re.sub(r"(aa|r)([iu])", lambda pat: r"Aː" + pat.group(2).upper(), str)
	str = re.sub(r"a([iu])", lambda pat: r"ɐ" + pat.group(1).upper(), str)
	str = re.sub(r"(aa|r)([ptk])", lambda pat: r"Aː" + pat.group(2).upper() + "]", str)
	str = re.sub(r"a([ptk])", lambda pat: r"ɐ" + pat.group(1).upper() + "]", str)
	str = re.sub(r"(aa|r)", r"Aː", str)
	str = re.sub(r"b", r"P", str)
	str = re.sub(r"c", r"T͡sH", str)
	str = re.sub(r"d", r"T", str)
	str = re.sub(r"eu", r"ɛːU", str)
	str = re.sub(r"eoi", r"ɵY", str)
	str = re.sub(r"oei", r"ɵY", str)
	str = re.sub(r"oe([pk])", r"œː\1]", str)
	str = re.sub(r"oe(ng)", r"œː\1", str)
	str = re.sub(r"(.)oe([t])", r"\1ɵ\2]", str)
	str = re.sub(r"^oet", r"œːt]", str)
	str = re.sub(r"oe([n])", r"ɵ\1", str)
	str = re.sub(r"oe", r"œː", str)
	str = re.sub(r"oi", r"ɔːI", str)
	str = re.sub(r"eo(ng)", r"œːŋ", str)
	str = re.sub(r"eo([k])", r"œː\1]", str)
	str = re.sub(r"eo([t])", r"ɵ\1]", str)
	str = re.sub(r"eon", r"ɵn", str)
	str = re.sub(r"ou", r"OU", str)
	str = re.sub(r"u([k])", r"ʊ\1]", str)
	str = re.sub(r"ui", r"UːI", str)
	str = re.sub(r"iu", r"IːU", str)
	str = re.sub(r"i(ng)", r"ɪN", str)
	str = re.sub(r"ik", r"ɪK]", str)
	str = re.sub(r"i([pt])", r"Iː\1]", str)
	str = re.sub(r"eo", r"ɵ", str)
	str = re.sub(r"a", r"ɐ", str)
	str = re.sub(r"ei", r"EI", str)
	str = re.sub(r"i", r"Iː", str)
	str = re.sub(r"e([ptk])", r"ɛː\1]", str)
	str = re.sub(r"e", r"ɛː", str)
	str = re.sub(r"o([ptk])", r"ɔː\1]", str)
	str = re.sub(r"u([pt])", r"Uː\1]", str)
	str = re.sub(r"u(ng)", r"ʊN", str)
	str = re.sub(r"o", r"ɔː", str)
	str = re.sub(r"u", r"Uː", str)
	str = re.sub(r"ng", r"N", str)
	str = re.sub(r"n", r"n", str)
	str = re.sub(r"kw", r"KWH", str)
	str = re.sub(r"gw", r"KW", str)
	str = re.sub(r"g", r"K", str)
	str = re.sub(r"(^|[ '])([ptk])", r"\1\2H", str)
	str = re.sub(r"w", r"w", str)
	str = re.sub(r"j", r"j", str)
	str = re.sub(r"m", r"m", str)
	str = re.sub(r"l", r"l", str)
	str = re.sub(r"s", r"s", str)
	str = re.sub(r"z", r"T͡s", str)
	trans = str.maketrans("PmfTnNlKhHsʃjwWɐAEɛIɪɔOœɵUʊYː]", "pmftnŋlkhʰsʃjwʷɐaeɛiɪɔoœɵuʊyː̚")
	str = str.translate(trans)
	str = str.replace(r"̚", "")
	str = str.replace("4", "˨˩")
	str = str.replace("1", "˥")
	str = str.replace("5", "˨˧")
	str = str.replace("2", "˧˥")
	str = str.replace("6", "˨")
	str = str.replace("3", "˧")
	str = str.replace("ɪŋ", "eŋ")  # patch -ing
	str = str.replace("ɪk", "ek")  # patch -ik
	return str
