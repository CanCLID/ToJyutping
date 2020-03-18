# -*- coding: utf-8 -*-

from os import path
from urllib import request

here = path.abspath(path.dirname(__file__))

def download_file_if_not_exist():
	'''Download the dictionary file to the current folder if not exists.'''
	DICT_URL = 'https://raw.githubusercontent.com/rime/rime-cantonese/master/jyut6ping3.dict.yaml'
	if not path.exists(path.join(here, 'jyut6ping3.dict.yaml')):
		request.urlretrieve(DICT_URL, path.join(here, 'jyut6ping3.dict.yaml'))

download_file_if_not_exist()

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
	return {k: v[0] for k, v in d.items()}

def write_dict(d):
	with open(path.join(here, 'src/ToJyutping/jyut6ping3.simple.dict.yaml'), 'w') as f:
		for k, v in d.items():
			print(k + '\t' + v, file=f)

write_dict(build_dict())
