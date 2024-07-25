# ToJyutping

![pip](https://github.com/CanCLID/ToJyutping/workflows/Python%20Package/badge.svg)

粵語拼音自動標註工具 Cantonese Pronunciation Automatic Labeling Tool

## Installation

```sh
$ pip install ToJyutping
```

### In Other Languages

- [JavaScript/TypeScript (npm) Version](https://www.npmjs.com/package/to-jyutping) ([Repo](https://github.com/CanCLID/to-jyutping))

## Usage

```python
>>> import ToJyutping

>>> ToJyutping.get_jyutping_list('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
[('咁', 'gam3'), ('啱', 'ngaam1'), ('老', 'lou5'), ('世', 'sai3'), ('要', 'jiu1'), ('求', 'kau4'), ('佢', 'keoi5'), ('等', 'dang2'), ('陣', 'zan6'), ('要', 'jiu3'), ('開', 'hoi1'), ('會', 'wui2'), ('，', None), ('剩', 'zing6'), ('低', 'dai1'), ('嘅', 'ge3'), ('嘢', 'je5'), ('我', 'ngo5'), ('會', 'wui5'), ('搞', 'gaau2'), ('掂', 'dim6'), ('㗎', 'gaa3'), ('喇', 'laa3'), ('。', None)]

>>> ToJyutping.get_jyutping('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
'咁(gam3)啱(ngaam1)老(lou5)世(sai3)要(jiu1)求(kau4)佢(keoi5)等(dang2)陣(zan6)要(jiu3)開(hoi1)會(wui2)，剩(zing6)低(dai1)嘅(ge3)嘢(je5)我(ngo5)會(wui5)搞(gaau2)掂(dim6)㗎(gaa3)喇(laa3)。'

>>> ToJyutping.get_jyutping_text('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
'gam3 ngaam1 lou5 sai3 jiu1 kau4 keoi5 dang2 zan6 jiu3 hoi1 wui2, zing6 dai1 ge3 je5 ngo5 wui5 gaau2 dim6 gaa3 laa3.'

>>> ToJyutping.get_jyutping_candidates('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
[('咁', ['gam3', 'gam2', 'gam1', 'gam4']), ('啱', ['ngaam1', 'aam1', 'am1', 'ngam1']), ('老', ['lou5', 'lou2']), ('世', ['sai3', 'sai2']), ('要', ['jiu1', 'jiu3', 'jiu2']), ('求', ['kau4']), ('佢', ['keoi5', 'heoi5']), ('等', ['dang2']), ('陣', ['zan6', 'zan2']), ('要', ['jiu3', 'jiu2', 'jiu1']), ('開', ['hoi1']), ('會', ['wui2', 'wui5', 'wui6', 'wui3', 'kui2', 'kui3', 'kwui2']), ('，', []), ('剩', ['zing6', 'sing6']), ('低', ['dai1']), ('嘅', ['ge3', 'ge2', 'koi2', 'koi3']), ('嘢', ['je5', 'e5']), ('我', ['ngo5', 'o5']), ('會', ['wui5', 'wui6', 'wui2', 'wui3', 'kui2', 'kui3', 'kwui2']), ('搞', ['gaau2']), ('掂', ['dim6', 'dim3', 'dim1']), ('㗎', ['gaa3', 'ga3', 'gaa2', 'gaa1', 'gaa4']), ('喇', ['laa3', 'laa1', 'laak3', 'laa5', 'laat3']), ('。', [])]

>>> ToJyutping.get_ipa_list('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
[('咁', 'kɐm˧'), ('啱', 'ŋaːm˥'), ('老', 'lou̯˩˧'), ('世', 'sɐi̯˧'), ('要', 'jiːu̯˥'), ('求', 'kʰɐu̯˨˩'), ('佢', 'kʰɵy̑˩˧'), ('等', 'tɐŋ˧˥'), ('陣', 't͡sɐn˨'), ('要', 'jiːu̯˧'), ('開', 'hɔːi̯˥'), ('會', 'wuːi̯˧˥'), ('，', None), ('剩', 't͡seŋ˨'), ('低', 'tɐi̯˥'), ('嘅', 'kɛː˧'), ('嘢', 'jɛː˩˧'), ('我', 'ŋɔː˩˧'), ('會', 'wuːi̯˩˧'), ('搞', 'kaːu̯˧˥'), ('掂', 'tiːm˨'), ('㗎', 'kaː˧'), ('喇', 'laː˧'), ('。', None)]

>>> ToJyutping.get_ipa('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
'咁[kɐm˧]啱[ŋaːm˥]老[lou̯˩˧]世[sɐi̯˧]要[jiːu̯˥]求[kʰɐu̯˨˩]佢[kʰɵy̑˩˧]等[tɐŋ˧˥]陣[t͡sɐn˨]要[jiːu̯˧]開[hɔːi̯˥]會[wuːi̯˧˥]，剩[t͡seŋ˨]低[tɐi̯˥]嘅[kɛː˧]嘢[jɛː˩˧]我[ŋɔː˩˧]會[wuːi̯˩˧]搞[kaːu̯˧˥]掂[tiːm˨]㗎[kaː˧]喇[laː˧]。'

>>> ToJyutping.get_ipa_text('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
'kɐm˧.ŋaːm˥.lou̯˩˧.sɐi̯˧.jiːu̯˥.kʰɐu̯˨˩.kʰɵy̑˩˧.tɐŋ˧˥.t͡sɐn˨.jiːu̯˧.hɔːi̯˥.wuːi̯˧˥ | t͡seŋ˨.tɐi̯˥.kɛː˧.jɛː˩˧.ŋɔː˩˧.wuːi̯˩˧.kaːu̯˧˥.tiːm˨.kaː˧.laː˧'

>>> ToJyutping.get_ipa_candidates('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
[('咁', ['kɐm˧', 'kɐm˧˥', 'kɐm˥', 'kɐm˨˩']), ('啱', ['ŋaːm˥', 'aːm˥', 'ɐm˥', 'ŋɐm˥']), ('老', ['lou̯˩˧', 'lou̯˧˥']), ('世', ['sɐi̯˧', 'sɐi̯˧˥']), ('要', ['jiːu̯˥', 'jiːu̯˧', 'jiːu̯˧˥']), ('求', ['kʰɐu̯˨˩']), ('佢', ['kʰɵy̑˩˧', 'hɵy̑˩˧']), ('等', ['tɐŋ˧˥']), ('陣', ['t͡sɐn˨', 't͡sɐn˧˥']), ('要', ['jiːu̯˧', 'jiːu̯˧˥', 'jiːu̯˥']), ('開', ['hɔːi̯˥']), ('會', ['wuːi̯˧˥', 'wuːi̯˩˧', 'wuːi̯˨', 'wuːi̯˧', 'kʰuːi̯˧˥', 'kʰuːi̯˧', 'kʷʰuːi̯˧˥']), ('，', []), ('剩', ['t͡seŋ˨', 'seŋ˨']), ('低', ['tɐi̯˥']), ('嘅', ['kɛː˧', 'kɛː˧˥', 'kʰɔːi̯˧˥', 'kʰɔːi̯˧']), ('嘢', ['jɛː˩˧', 'ɛː˩˧']), ('我', ['ŋɔː˩˧', 'ɔː˩˧']), ('會', ['wuːi̯˩˧', 'wuːi̯˨', 'wuːi̯˧˥', 'wuːi̯˧', 'kʰuːi̯˧˥', 'kʰuːi̯˧', 'kʷʰuːi̯˧˥']), ('搞', ['kaːu̯˧˥']), ('掂', ['tiːm˨', 'tiːm˧', 'tiːm˥']), ('㗎', ['kaː˧', 'kɐ˧', 'kaː˧˥', 'kaː˥', 'kaː˨˩']), ('喇', ['laː˧', 'laː˥', 'laːk̚˧', 'laː˩˧', 'laːt̚˧']), ('。', [])]
```

In rare cases, the pronunciation of a single character can contain more than one syllable:

```python
>>> ToJyutping.get_jyutping_list('一瓩')
[('一', 'jat1'), ('瓩', 'cin1 ngaa5')]
>>> ToJyutping.get_ipa_list('一瓩')
[('一', 'jɐt̚˥'), ('瓩', 't͡sʰiːn˥.ŋaː˩˧')]
```

## Grapheme-to-Phoneme Conversion Function

Intended for machine learning purposes (especially text-to-speech and automatic speech recognition), a `g2p` function is provided to reduce conversion problems due to lack of linguistic knowledge. It takes a string and outputs a tuple of 3 integers (ranged from 0 to 86 inclusive) representing the **onset** (聲母), **rhyme** (韻母) and **tone** (聲調) of a syllable:

```python
>>> ToJyutping.g2p('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
[(9, 32, 3), (11, 23, 1), (8, 58, 5), (18, 30, 3), (19, 49, 1), (10, 31, 4), (10, 79, 5), (5, 34, 2), (16, 33, 6), (19, 49, 3), (15, 57, 1), (14, 66, 2), (16, 52, 6), (5, 30, 1), (9, 38, 3), (19, 38, 5), (11, 56, 5), (14, 66, 5), (9, 22, 2), (5, 50, 6), (9, 20, 3), (8, 20, 3)]
```

From the above example, you can see that the tone values are coincidently the same as some of the onsets, as separating tones into another sequence is a more common practice (for example, this is what VITS2 expects). If this is undesirable, pass `tone_same_seq=True` to output integers ranged from 0 up to 92:

```python
>>> ToJyutping.g2p('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。', tone_same_seq=True)
[(9, 32, 89), (11, 23, 87), (8, 58, 91), (18, 30, 89), (19, 49, 87), (10, 31, 90), (10, 79, 91), (5, 34, 88), (16, 33, 92), (19, 49, 89), (15, 57, 87), (14, 66, 88), (16, 52, 92), (5, 30, 87), (9, 38, 89), (19, 38, 91), (11, 56, 91), (14, 66, 91), (9, 22, 88), (5, 50, 92), (9, 20, 89), (8, 20, 89)]
```

Additionally, the second `offset` argument can be specified to shift the output values by a certain amount:

```python
>>> ToJyutping.g2p('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。', offset=100)
[(109, 132, 103), (111, 123, 101), (108, 158, 105), (118, 130, 103), (119, 149, 101), (110, 131, 104), (110, 179, 105), (105, 134, 102), (116, 133, 106), (119, 149, 103), (115, 157, 101), (114, 166, 102), (116, 152, 106), (105, 130, 101), (109, 138, 103), (119, 138, 105), (111, 156, 105), (114, 166, 105), (109, 122, 102), (105, 150, 106), (109, 120, 103), (108, 120, 103)]
```

This is useful if you wish to place custom symbols at the front.

You may pass a triplet as well for shifting each element by different amounts:

```python
>>> ToJyutping.g2p('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。', offset=(100, 200, 300))
[(109, 232, 303), (111, 223, 301), (108, 258, 305), (118, 230, 303), (119, 249, 301), (110, 231, 304), (110, 279, 305), (105, 234, 302), (116, 233, 306), (119, 249, 303), (115, 257, 301), (114, 266, 302), (116, 252, 306), (105, 230, 301), (109, 238, 303), (119, 238, 305), (111, 256, 305), (114, 266, 305), (109, 222, 302), (105, 250, 306), (109, 220, 303), (108, 220, 303)]
```

## Helper

```python
>>> ToJyutping.jyutping2ipa('jat1')
'jɐt̚˥'
>>> ToJyutping.jyutping2ipa('cin1 ngaa5')
't͡sʰiːn˥.ŋaː˩˧'
```

Note that autocorrection is intentionally not included in this helper, and an error is thrown if strings like `jyt6` are passed into the function.
Punctuation is ignored in the helper.
