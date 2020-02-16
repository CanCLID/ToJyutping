# -*- coding: utf-8 -*-

import opencc2
from os import path
import pygtrie
import urllib.request

here = path.abspath(path.dirname(__file__))

class ToJyutping:
	def __init__(self):
		self.cc_s = opencc2.Converter(from_variant='cn', to_variant='t', fast=True, with_phrases=False)  # TODO: Cannot handle 沈
		self.cc_hk = opencc2.Converter(from_variant='cn', to_variant='t', fast=True, with_phrases=False)

		def freq_str_to_float(s):
			'''Convert frequency data in the dictionary file to float.
			>>> freq_str_to_float('2')
			2.0
			>>> freq_str_to_float('2%')
			0.02
			'''
			if s[-1] == '%':
				return float(s[:-1]) * 0.01
			else:
				return float(s)

		def build_dict():
			'''Create a dictionary of all the words with jyutping data.
			If there are multiple possibilities, the one with higher frequency is used.
			'''
			d = {}
			with open(path.join(here, 'jyut6ping3.dict.yaml')) as f:
				for line in f:
					if line == '...\n':
						break
				next(f)
				for line in f:
					if line and line[0] != '#':
						parts = line.rstrip().rstrip('\t').split('\t')
						if len(parts) == 2:
							ch, jyut = parts
							if len(ch) == 1 or len(ch) == jyut.count(' ') + 1:
								original = d.get(ch)
								if not original:
									d[ch] = (jyut,)
								else:
									original_jyut = original[0]
									if original_jyut[-1] != '2' and jyut[-1] == '2':
										d[ch] = (jyut,)
						elif len(parts) == 3:
							ch, jyut, freq = parts
							if len(ch) == 1 or len(ch) == jyut.count(' ') + 1:
								original = d.get(ch)
								if not original:
										current_freq = freq_str_to_float(freq)
										d[ch] = (jyut, current_freq)
								else:
									if len(original) == 1:
										current_freq = freq_str_to_float(freq)
										d[ch] = (jyut, current_freq)
									else:
										original_freq = original[1]
										current_freq = freq_str_to_float(freq)
										if current_freq > original_freq:
											d[ch] = (jyut, current_freq)
			return d

		d = build_dict()

		# Build a trie from a dict
		t = pygtrie.CharTrie()
		for k, v in d.items():
			t[k] = v[0]
		self.DICT = t

	def run(self, s):
		def replace_words_plain(s, t):
			s_t = self.cc_hk.convert(self.cc_s.convert(s))
			l = []  # list of coverted words
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
