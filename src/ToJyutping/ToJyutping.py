from os import path
import pygtrie
import re

here = path.abspath(path.dirname(__file__))

t = pygtrie.CharTrie()
with open(path.join(here, 'jyut6ping3.simple.dict.yaml')) as f:
	for line in f:
		k, v = line.rstrip().split('\t')
		t[k] = v

def get_jyutping_list(s):
	l = []
	while s:
		p = t.longest_prefix(s)
		if not p:
			l += [(s[0], None)]
			s = s[1:]
		else:
			n = len(p.key)
			l += zip(s[:n], p.value.split(' ', n - 1))
			s = s[n:]
	return l

def get_jyutping(s):
	l = ''
	for k, v in get_jyutping_list(s):
		l += k + ('(%s)' % v if v else '')
	return l

def get_jyutping_text(s):
	l = []
	for k, v in get_jyutping_list(s):
		if v:
			l += [v]
	return ' '.join(l)

def get_ipa_list(s):
	l = []
	for k, v in get_jyutping_list(s):
		l += [(k, v and jyutping2ipa(v))]
	return l

def get_ipa(s):
	l = ''
	for k, v in get_jyutping_list(s):
		l += k + ('[%s]' % jyutping2ipa(v) if v else '')
	return l

def get_ipa_text(s):
	l = []
	for k, v in get_jyutping_list(s):
		if v:
			l += [jyutping2ipa(v)]
	return '.'.join(l)

initial = { 'b': 'p', 'p': 'pʰ', 'm': 'm', 'f': 'f', 'd': 't', 't': 'tʰ', 'n': 'n', 'l': 'l', 'g': 'k', 'k': 'kʰ',
			'ng': 'ŋ', 'gw': 'kʷ', 'kw': 'kʷʰ', 'w': 'w', 'h': 'h', 'z': 't͡s', 'c': 't͡sʰ', 's': 's', 'j': 'j' }
nucleus = { 'aa': 'aː', 'a': 'ɐ', 'e': 'ɛː', 'i': 'iː', 'o': 'ɔː', 'u': 'uː', 'oe': 'œː', 'eo': 'ɵ', 'yu': 'yː' }
unit = { 'ei': 'ei̯', 'ing': 'eŋ', 'ik': 'ek̚', 'ou': 'ou̯', 'ung': 'oŋ', 'uk': 'ok̚', 'eoi': 'ɵy̑', 'm': 'm̩', 'ng': 'ŋ̍' }
terminal = { 'i': 'i̯', 'u': 'u̯', 'm': 'm', 'n': 'n', 'ng': 'ŋ', 'p': 'p̚', 't': 't̚', 'k': 'k̚' }
tone = { '1': '˥', '2': '˧˥', '3': '˧', '4': '˨˩', '5': '˩˧', '6': '˨' }

def jyutping2ipa(s):
	l = []
	for t in re.split("[\s'.]+", s):
		match = re.match('^((?:[gk]w?|ng|[bpmfdtnlhwzcsj])?)((?:aa?|oe|eo|yu|[eiou])?)((?:ng|[iumnptk])?)((?:[1-6])?)$', t)
		lead, vowel, final, number = match.groups()
		group = vowel + final
		l += [(lead and initial[lead])
			+ (unit[group] if group in unit else (vowel and nucleus[vowel]) + (final and terminal[final]))
			+ (tone and tone[number])
		]
	return '.'.join(l)
