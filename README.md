# ToJyutping ![](https://github.com/CanCLID/ToJyutping/workflows/Python%20Package/badge.svg)

Install:

```sh
$ pip install ToJyutping
```

Usage:

```python
>>> import ToJyutping
>>> ToJyutping.get_jyutping_list('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
[('咁', 'gam3'), ('啱', 'ngaam1'), ('老', 'lou5'), ('世', 'sai3'), ('要', 'jiu1'), ('求', 'kau4'), ('佢', 'keoi5'), ('等', 'dang2'), ('陣', 'zan6'), ('要', 'jiu3'), ('開', 'hoi1'), ('會', 'wui2'), ('，', None), ('剩', 'zing6'), ('低', 'dai1'), ('嘅', 'ge2'), ('嘢', 'je5'), ('我', 'ngo5'), ('會', 'wui5'), ('搞', 'gaau2'), ('掂', 'dim6'), ('㗎', 'ga3'), ('喇', 'laa3'), ('。', None)]
>>> ToJyutping.get_jyutping('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
'咁(gam3)啱(ngaam1)老(lou5)世(sai3)要(jiu1)求(kau4)佢(keoi5)等(dang2)陣(zan6)要(jiu3)開(hoi1)會(wui2)，剩(zing6)低(dai1)嘅(ge2)嘢(je5)我(ngo5)會(wui5)搞(gaau2)掂(dim6)㗎(ga3)喇(laa3)。'
>>> ToJyutping.get_jyutping_text('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
'gam3 ngaam1 lou5 sai3 jiu1 kau4 keoi5 dang2 zan6 jiu3 hoi1 wui2, zing6 dai1 ge2 je5 ngo5 wui5 gaau2 dim6 ga3 laa3.'
>>> ToJyutping.get_ipa_list('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
[('咁', 'kɐm˧'), ('啱', 'ŋaːm˥'), ('老', 'lou̯˩˧'), ('世', 'sɐi̯˧'), ('要', 'jiːu̯˥'), ('求', 'kʰɐu̯˨˩'), ('佢', 'kʰɵy̑˩˧'), ('等', 'tɐŋ˧˥'), ('陣', 't͡sɐn˨'), ('要', 'jiːu̯˧'), ('開', 'hɔːi̯˥'), ('會', 'wuːi̯˧˥'), ('，', None), ('剩', 't͡seŋ˨'), ('低', 'tɐi̯˥'), ('嘅', 'kɛː˧˥'), ('嘢', 'jɛː˩˧'), ('我', 'ŋɔː˩˧'), ('會', 'wuːi̯˩˧'), ('搞', 'kaːu̯˧˥'), ('掂', 'tiːm˨'), ('㗎', 'kɐ˧'), ('喇', 'laː˧'), ('。', None)]
>>> ToJyutping.get_ipa('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
'咁[kɐm˧]啱[ŋaːm˥]老[lou̯˩˧]世[sɐi̯˧]要[jiːu̯˥]求[kʰɐu̯˨˩]佢[kʰɵy̑˩˧]等[tɐŋ˧˥]陣[t͡sɐn˨]要[jiːu̯˧]開[hɔːi̯˥]會[wuːi̯˧˥]，剩[t͡seŋ˨]低[tɐi̯˥]嘅[kɛː˧˥]嘢[jɛː˩˧]我[ŋɔː˩˧]會[wuːi̯˩˧]搞[kaːu̯˧˥]掂[tiːm˨]㗎[kɐ˧]喇[laː˧]。'
>>> ToJyutping.get_ipa_text('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
'kɐm˧.ŋaːm˥.lou̯˩˧.sɐi̯˧.jiːu̯˥.kʰɐu̯˨˩.kʰɵy̑˩˧.tɐŋ˧˥.t͡sɐn˨.jiːu̯˧.hɔːi̯˥.wuːi̯˧˥ | t͡seŋ˨.tɐi̯˥.kɛː˧˥.jɛː˩˧.ŋɔː˩˧.wuːi̯˩˧.kaːu̯˧˥.tiːm˨.kɐ˧.laː˧'
```

In rare cases, the pronunciation of a single character can contain more than one syllable:

```python
>>> ToJyutping.get_jyutping_list('一瓩')
[('一', 'jat1'), ('瓩', 'cin1 ngaa5')]
>>> ToJyutping.get_ipa_list('一瓩')
[('一', 'jɐt̚˥'), ('瓩', 't͡sʰiːn˥.ŋaː˩˧')]
```

Helper:

```python
>>> ToJyutping.jyutping2ipa('jat1')
'jɐt̚˥'
>>> ToJyutping.jyutping2ipa('cin1 ngaa5')
't͡sʰiːn˥.ŋaː˩˧'
```

Note that autocorrection is intentionally not included in this helper, and an error is thrown if strings like `jyt6` are passed into the function.
Punctuation is ignored in the helper.
