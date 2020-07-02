# ToJyutping

Install:

```sh
$ pip install ToJyutping
```

Usage:

```python
>>> import ToJyutping
>>> ToJyutping.get_jyutping_list('一瓩係乜嘢嚟㗎？')
[('一', 'jat1'), ('瓩', 'cin1 ngaa5'), ('係', 'hai6'), ('乜', 'mat1'), ('嘢', 'je5'), ('嚟', 'lai4'), ('㗎', 'gaa3'), ('？', None)]
>>> ToJyutping.get_jyutping('一瓩係乜嘢嚟㗎？')
'一(jat1)瓩(cin1 ngaa5)係(hai6)乜(mat1)嘢(je5)嚟(lai4)㗎(gaa3)？'
>>> ToJyutping.get_ipa('一瓩係乜嘢嚟㗎？')
'一(jɐt˥)瓩(t͡sʰiːn˥ ŋaː˨˧)係(hɐi˨)乜(mɐt˥)嘢(jɛː˨˧)嚟(lɐi˨˩)㗎(kaː˧)？'
```

Helper:

```python
>>> ToJyutping.jyutping2ipa('jat1')
'jɐt˥'
```

# License

This repository is distributed under MIT license.

Dictionary data is taken from [rime/rime-cantonese](https://github.com/rime/rime-cantonese), which is licensed under a Creative Commons Attribution 4.0 International License.
