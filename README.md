# ToJyutping ![](https://github.com/CanCLID/ToJyutping/workflows/Python%20Package/badge.svg)

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
>>> ToJyutping.get_jyutping_text('一瓩係乜嘢嚟㗎？')
'jat1 cin1 ngaa5 hai6 mat1 je5 lai4 gaa3'
>>> ToJyutping.get_ipa_list('一瓩係乜嘢嚟㗎？')
[('一', 'jɐt̚˥'), ('瓩', 't͡sʰiːn˥.ŋaː˩˧'), ('係', 'hɐi̯˨'), ('乜', 'mɐt̚˥'), ('嘢', 'jɛː˩˧'), ('嚟', 'lɐi̯˨˩'), ('㗎', 'kaː˧'), ('？', None)]
>>> ToJyutping.get_ipa('一瓩係乜嘢嚟㗎？')
'一[jɐt̚˥]瓩[t͡sʰiːn˥.ŋaː˩˧]係[hɐi̯˨]乜[mɐt̚˥]嘢[jɛː˩˧]嚟[lɐi̯˨˩]㗎[kaː˧]？'
>>> ToJyutping.get_ipa_text('一瓩係乜嘢嚟㗎？')
'jɐt̚˥.t͡sʰiːn˥.ŋaː˩˧.hɐi̯˨.mɐt̚˥.jɛː˩˧.lɐi̯˨˩.kaː˧'
```

Helper:

```python
>>> ToJyutping.jyutping2ipa('jat1')
'jɐt̚˥'
>>> ToJyutping.jyutping2ipa('cin1 ngaa5')
't͡sʰiːn˥.ŋaː˩˧'
```

Note that autocorrection is intentionally not included in this helper, and an error is thrown if strings like `jyt6` are passed into the function.
