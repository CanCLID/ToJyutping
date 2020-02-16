# -*- coding: utf-8 -*-

from os import path
import pygtrie
import urllib.request

here = path.abspath(path.dirname(__file__))

class ToJyutping:
	def __init__(self):
		def download_file_if_not_exist():
			if not path.exists('jyut6ping3.dict.yaml'):
				urllib.request.urlretrieve('https://raw.githubusercontent.com/rime/rime-cantonese/master/jyut6ping3.dict.yaml', path.join(here, 'jyut6ping3.dict.yaml'))

		def freq_str_to_float(s):
			if s[-1] == '%':
				return float(s[:-1]) * 0.01
			else:
				return float(s)

		def build_dict():
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
			return {k: v[0] for k, v in d.items()}

		def build_trie(d):  # build a trie
			t = pygtrie.CharTrie()
			for k, v in d.items():
				t[k] = v
			return t

		download_file_if_not_exist()
		d = build_dict()
		self.DICT = build_trie(d)

	def run(self, s):
		def replace_words_plain(s, t):
			l = []  # list of coverted words
			while s:
				longest_prefix = t.longest_prefix(s)  # match the longest prefix
				if not longest_prefix:  # if the prefix does not exist
					l.append(s[0])  # append the first character
					s = s[1:]  # remove the first character from the string
				else:  # if exists
					word, jyut = longest_prefix.key, longest_prefix.value
					if len(word) == 1:
						l.append(word + '(' + jyut + ')')
						s = s[1:]  # remove the word from the string
					else:
						for k, v in zip(word, jyut.split(' ')):
							l.append(k + '(' + v + ')')
						s = s[len(word):]  # remove the word from the string
			return ''.join(l)

		return replace_words_plain(s, self.DICT)
