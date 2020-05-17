# -*- coding: utf-8 -*-

from opencc import OpenCC
from os import path
import pygtrie
import urllib.request

here = path.abspath(path.dirname(__file__))

class ToJyutping:
	def __init__(self):
		self.cc_s = OpenCC('s2t.json')  # TODO: Cannot handle 沈
		#self.cc_hk = OpenCC('hk2t.json')  # Wait for https://github.com/BYVoid/OpenCC/issues/406

		t = pygtrie.CharTrie()
		with open(path.join(here, 'jyut6ping3.simple.dict.yaml')) as f:
			for line in f:
				k, v = line.rstrip().split('\t')
				t[k] = v
		self.DICT = t

	def run(self, s):
		def replace_words_plain(s, t):
			#s_t = self.cc_hk.convert(self.cc_s.convert(s))
			s_t = self.cc_s.convert(s)
			l = []  # list of converted words
			while s:
				longest_prefix = t.longest_prefix(s_t)  # match the longest prefix
				if not longest_prefix:  # if the prefix does not exist
					l.append(s[0])  # append the first character
					s = s[1:]  # remove the first character from the string
					s_t = s_t[1:]
				else:  # if exists
					word, jyut = longest_prefix.key, longest_prefix.value
					if len(word) == 1:
						l.append(s[0] + '(' + jyut + ')')
						s = s[1:]  # remove the word from the string
						s_t = s_t[1:]
					else:
						for k, v in zip(s[:len(word)], jyut.split(' ')):
							l.append(k + '(' + v + ')')
						s = s[len(word):]  # remove the word from the string
						s_t = s_t[len(word):]  # remove the word from the string
			return ''.join(l)

		return replace_words_plain(s, self.DICT)
