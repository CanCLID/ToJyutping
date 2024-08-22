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

For the 8 basic functions, examples are worth a thousand words:

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

For `get_jyutping_candidates` and `get_ipa_candidates`, pronunciations are sorted according to how likely they are to be correct in a sentence, with the first being the most likely.

Methods may also be imported individually:

```python
>>> from ToJyutping import get_jyutping_text
>>> get_jyutping_text('咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。')
'gam3 ngaam1 lou5 sai3 jiu1 kau4 keoi5 dang2 zan6 jiu3 hoi1 wui2, zing6 dai1 ge3 je5 ngo5 wui5 gaau2 dim6 gaa3 laa3.'
```

In rare cases, the pronunciation of a single character can contain more than one syllable:

```python
>>> ToJyutping.get_jyutping_list('一瓩')
[('一', 'jat1'), ('瓩', 'cin1 ngaa5')]
>>> ToJyutping.get_ipa_list('一瓩')
[('一', 'jɐt̚˥'), ('瓩', 't͡sʰiːn˥.ŋaː˩˧')]
```

They are mostly dated ligature characters (合字) coined to represent units with SI prefixes. 

## Custom Entries & Existing Entries Overriding or Exclusion

With an accuracy rate of 99%, the possibility of needing an adjustment is rare. However, Cantonese, like other varieties of Chinese, is mostly written in logographs, which means that homographs (同形詞) that are indistinguishable out of context can occur. Consider the following sentence:

> 上堂終於講到分數

In the above sentence, there are multiple possible pronunciations of 上, 到 and 分, and their meanings are different depending on how they are actually pronounced:

| Pronunciation | Meaning |
| --- | --- |
| soeng**5** tong4 zung1 jyu1 gong2 dou**3** fan**1** sou3 | Attending the lesson, it finally came to talk about scores.<br>_(Perhaps the scores weren’t available until today.)_ |
| soeng**5** tong4 zung1 jyu1 gong2 dou**3** fan**6** sou3 | Attending the lesson, it finally came to talk about fractions.<br>_(Perhaps the progress of the math class was slow.)_ |
| soeng**5** tong4 zung1 jyu1 gong2 dou**2** fan**1** sou3 | Attending the lesson, eventually it was able to talk about scores.<br>_(Perhaps the teacher wasn’t allowed to reveal the scores until today.)_ |
| soeng**5** tong4 zung1 jyu1 gong2 dou**2** fan**6** sou3 | Attending the lesson, eventually it was able to talk about fractions.<br>_(Perhaps the introduction to fractions requires some other concepts to be taught.)_ |
| soeng**6** tong4 zung1 jyu1 gong2 dou**3** fan**1** sou3 | The previous lesson finally came to talk about scores.<br>_(Perhaps the teacher just made the scores available right before the previous lesson.)_ |
| soeng**6** tong4 zung1 jyu1 gong2 dou**3** fan**6** sou3 | The previous lesson finally came to talk about fractions.<br>_(Perhaps the students just managed to catch up the progress in the math class.)_ |
| soeng**6** tong4 zung1 jyu1 gong2 dou**2** fan**1** sou3 | Eventually, it was able to talk about scores in the previous lesson.<br>_(Perhaps the teacher was finally allowed to reveal the scores in the previous lesson.)_ |
| soeng**6** tong4 zung1 jyu1 gong2 dou**2** fan**6** sou3 | Eventually, it was able to talk about fractions in the previous lesson.<br>_(Perhaps the teacher just finished teaching the other concepts required for learning fractions.)_ |

Thus, the library offers the ability to include custom entries and override or exclude built-in entries:

```python
>>> ToJyutping.get_jyutping_text('上堂終於講到分數')
'soeng5 tong4 zung1 jyu1 gong2 dou3 fan1 sou3'

>>> converter_lesson = ToJyutping.customize({'上堂': None, '分數': 'fan6 sou3'})
>>> converter_lesson.get_jyutping_text('上堂終於講到分數')
'soeng6 tong4 zung1 jyu1 gong2 dou3 fan6 sou3'
```

In the above example:

- By default, the library special-cases the pronunciation of 上堂 to “soeng5 tong4”. Setting `上堂` to `None` removes the special case and both 上 and 堂 now fallback to the their default pronunciations, which are “soeng6” and “tong4” respectively.
- By default, the library does not special-case 分數. Thus, the pronunciations of each individual characters, which in this case are “fan1” and “sou3”, are used. By including the entry `分數` and setting it to `fan6 sou3`, the converter outputs `fan6 sou3` when `分數` is encountered.

In general, setting any built-in entry to `None` fallbacks it to shorter matches and ultimately individual character pronunciations if there isn’t a match:

```python
>>> ToJyutping.get_jyutping_text('好學生')
'hou2 hok6 saang1'

>>> converter_studious = ToJyutping.customize({'好學生': None})
>>> converter_studious.get_jyutping_text('好學生')
'hou3 hok6 saang1' # Using shorter matches 好學 and 生

>>> converter_good_student = converter_studious.customize({'好學': None})
>>> converter_good_student.get_jyutping_text('好學生')
'hou2 hok6 saang1' # Using individual character pronunciations as it can’t be decomposed further
```

Converters can be chained without affecting each other:

```python
>>> converter_dou2 = converter_lesson.customize({'到': 'dou2'})
>>> converter_None = converter_lesson.customize({'到': None})

>>> converter_dou2.get_jyutping_text('上堂終於講到分數')
'soeng6 tong4 zung1 jyu1 gong2 dou2 fan6 sou3'

>>> converter_None.get_jyutping_text('上堂終於講到分數')
'soeng6 tong4 zung1 jyu1 gong2 […] fan6 sou3'

>>> ToJyutping.get_jyutping_text('上堂終於講到分數')
'soeng5 tong4 zung1 jyu1 gong2 dou3 fan1 sou3' # Also not affected
```

> [!WARNING]
> - This library only offers basic customization functionality. If there are longer built-in word entries, they aren’t overridden:
>   ```python
>   >>> converter_dou2.get_jyutping_text('笑到轆地')
>   'siu3 dou3 luk1 dei2'
>   
>   >>> converter_None.get_jyutping_text('笑到轆地')
>   'siu3 dou3 luk1 dei2'
>   
>   >>> converter_another_lesson = ToJyutping.customize({'上': None, '分': 'fan6'})
>   >>> converter_another_lesson.get_jyutping_text('上堂終於講到分數')
>   'soeng5 tong4 zung1 jyu1 gong2 dou3 fan6 sou3'
>   ```
>   In the second example, their isn’t an entry for 分數, so 分 is patched successfully. However, this is not the case for 上 since the longer built-in entry 上堂 is prioritized.
> - The original pronunciations will be lost. If you are using `get_jyutping_candidates` or `get_ipa_candidates`, you will need to include the pronunciations manually:
>   ```python
>   >>> 到_original_pronunciations = ToJyutping.get_jyutping_candidates('到')
>   >>> 到_original_pronunciations
>   [('到', ['dou3', 'dou2'])]
>   >>> converter_dou2_dou3 = converter_lesson.customize({'到': ['dou2', *到_original_pronunciations[0][1]]})
>   >>> converter_dou2_dou3.get_jyutping_candidates('到')
>   [('到', ['dou2', 'dou3'])]
>   ```
>   Notice how the library automatically deduplicates the values for you.

## Grapheme-to-Phoneme Conversion Function

Intended for machine learning purposes (especially text-to-speech and automatic speech recognition), a `g2p` function is provided to minimize the possibility of conversion problems due to lack of linguistic knowledge. It takes a string and outputs tuples of 3 integers (ranged from 8 to 94 inclusive) representing the **onset** (聲母), **rhyme** (韻母) and **tone** (聲調) of a syllable. Punctuations are included as singletons (1-tuples) and range from 1 to 7. They are detailed in the _[Punctuations](#punctuations)_ section below.

> [!NOTE]
> In this section, the word _“punctuation”_ may be delibrately written in the plural form to avoid confusion.

> [!IMPORTANT]
> In this section, **punctuations** include the unknown character filler, described in the _Punctuations_ section.

```python
>>> ToJyutping.g2p('咩話……你話上個月上堂學法文文法用咗 $50,000！？')
PhonemesList(
    [(11, 46, 1), (22, 28, 2), (2,), (15, 47, 5), (22, 28, 6), (26, 84, 6), (17, 64, 3), (27, 92, 6), (26, 84, 5), (14, 69, 4), (23, 72, 6), (12, 35, 3), (11, 41, 2), (11, 41, 4), (12, 35, 3), (27, 78, 6), (24, 64, 2), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (4,), (5,)],
    segmentals=[11, 46, 22, 28, 2, 15, 47, 22, 28, 26, 84, 17, 64, 27, 92, 26, 84, 14, 69, 23, 72, 12, 35, 11, 41, 11, 41, 12, 35, 27, 78, 24, 64, 1, 1, 1, 1, 1, 1, 1, 4, 5],
    tones=[1, 1, 2, 2, 0, 5, 5, 6, 6, 6, 6, 3, 3, 6, 6, 5, 5, 4, 4, 6, 6, 3, 3, 2, 2, 4, 4, 3, 3, 6, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    lengths=[2, 2, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
)
```

(Formatted manually, not exactly the same as what `repr` produces)

`PhonemesList` is a `list` with convenient properties common to syllables handling (particularly in VITS2). `segmentals` is an ordinary `list` with onsets, rhymes and punctuations included, while each element of `tones` gives the tone corresponding to each onset or rhyme, or `0` if the corresponding element is a punctuation. `lengths` suggests how many elements of `segmentals` or `tones` is each character of the original input correspond to. It is guaranteed that:

- `lengths` always sum up to the number of elements of both `segmentals` and `tones`; and
- The length of the input is always the same as that of `lengths`, such that they can be zipped nicely.

Note that the number of elements of `lengths` does not necessary match that of the original `PhonemesList`, since the input may contain polysyllabic characters, consecutive punctuations of the same type, or whitespaces.

From the above example, you can see that the tone values are coincidently the same as some of the onsets, as it is a more common practice to separate tones into another sequence (this is what VITS2 expects, for example). If this is undesirable, pass `tone_same_seq=True` to output integers ranged from 8 up to 100:

(From now on, the properties are not shown. Try them out and reveal them yourselves! However, for the case setting `tone_same_seq` to `True`, you probably don’t need them and just need to flatten the list.)

```python
>>> ToJyutping.g2p('咩話……你話上個月上堂學法文文法用咗 $50,000！？', tone_same_seq=True)
PhonemesList([(11, 46, 95), (22, 28, 96), (2,), (15, 47, 99), (22, 28, 100), (26, 84, 100), (17, 64, 97), (27, 92, 100), (26, 84, 99), (14, 69, 98), (23, 72, 100), (12, 35, 97), (11, 41, 96), (11, 41, 98), (12, 35, 97), (27, 78, 100), (24, 64, 96), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (4,), (5,)])
```

Additionally, the second `offset` argument can be specified to shift the output values by a certain amount:

```python
>>> ToJyutping.g2p('咩話……你話上個月上堂學法文文法用咗 $50,000！？', offset=100)
PhonemesList([(103, 138, 101), (114, 120, 102), (2,), (107, 139, 105), (114, 120, 106), (118, 176, 106), (109, 156, 103), (119, 184, 106), (118, 176, 105), (106, 161, 104), (115, 164, 106), (104, 127, 103), (103, 133, 102), (103, 133, 104), (104, 127, 103), (119, 170, 106), (116, 156, 102), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (4,), (5,)])
```

You may pass a triplet as well for shifting each element by different amounts:

```python
>>> ToJyutping.g2p('咩話……你話上個月上堂學法文文法用咗 $50,000！？', offset=(100, 200, 300))
PhonemesList([(103, 238, 301), (114, 220, 302), (2,), (107, 239, 305), (114, 220, 306), (118, 276, 306), (109, 256, 303), (119, 284, 306), (118, 276, 305), (106, 261, 304), (115, 264, 306), (104, 227, 303), (103, 233, 302), (103, 233, 304), (104, 227, 303), (119, 270, 306), (116, 256, 302), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (4,), (5,)])
```

By default, `offset` shifts the onsets and rhymes by 8, which is one plus the number of elements in the default punctuation set described in the below section. The tones are **not** shifted unless `tone_same_seq` is set to `True`.

> [!WARNING]
> This is not the case if you specify `offset` as a single value. The onsets, rhymes and tones are **all shifted** by `offset` and both the `segmentals` and `tones` properties are affected if you provide a single integer. This may not be desirable unless `tone_same_seq` is set. To suppress shifting tones, pass `(amount, amount, 0)`. See below for an example.

### Punctuations

By default, ToJyutping classifies punctuations into 6 categories, `.`, `,`, `!`, `?`, `-` and `'`, and numbers them from 2 to 7. 1's (you may label it `…` for convenience) are used to mark unknown characters in the input string.

The reason for using a filler instead of raising an error is that we want to avoid data-driven errors. Strings in the dataset are known, but this is not the case for user input. If this is undesirable, you will need to look for `(1,)` in the output list and raise the error yourself.

Consecutive punctuations of the same type are collapsed into a single element. For example, both `……` and `......` become a single `(2,)`. However, this does not applies to the unknown character filler. This is because we want to maintain the length of the audio when there are multiple consecutive unknown characters.

You may supply `puncts_offset` to shift the punctuation IDs by a certain amount. For example, to swap the order of syllable IDs and punctuation IDs (i.e. make syllables range from 1 to 87 and punctuations range from 88 to 94):

```python
>>> ToJyutping.g2p('咩話……你話上個月上堂學法文文法用咗 $50,000！？', offset=(1, 1, 0), puncts_offset=88)
PhonemesList([(4, 39, 1), (15, 21, 2), (89,), (8, 40, 5), (15, 21, 6), (19, 77, 6), (10, 57, 3), (20, 85, 6), (19, 77, 5), (7, 62, 4), (16, 65, 6), (5, 28, 3), (4, 34, 2), (4, 34, 4), (5, 28, 3), (20, 71, 6), (17, 57, 2), (88,), (88,), (88,), (88,), (88,), (88,), (88,), (91,), (92,)])
```

The `puncts_offset` argument **defaults to 1**, since 0 is commonly used as the ID for padding. However, if `puncts_map` (detailed in the [Custom Punctuation Map](#custom-punctuation-map) section below) is provided, it’s defaulted to 0.

> [!WARNING]
> The `offset` and `puncts_offset` arguments do not affect each other. If you changed `puncts_offset`, be sure to modify `offset` as well, or the values will coincide. **Read the instructions in the above section** before doing so.

Although not recommended, to make the ID for padding and the unknown character filler the same:

```python
>>> ToJyutping.g2p('咩話……你話上個月上堂學法文文法用咗 $50,000！？', puncts_offset=0, offset=(7, 7, 0))
PhonemesList([(10, 45, 1), (21, 27, 2), (1,), (14, 46, 5), (21, 27, 6), (25, 83, 6), (16, 63, 3), (26, 91, 6), (25, 83, 5), (13, 68, 4), (22, 71, 6), (11, 34, 3), (10, 40, 2), (10, 40, 4), (11, 34, 3), (26, 77, 6), (23, 63, 2), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (3,), (4,)])
```

This causes all values to be decreased by 1 except for the tones.

#### Decimal Numbers Detection

From the very first example in the _[g2p Conversion Function](#grapheme-to-phoneme-conversion-function)_ section, you can see that the thousand separator `,` is converted to `(1,)` instead of `(3,)`. In fact, the library automatically checks if `,` and `.`, etc. are between digits, prevents them from being treated as commas and treats them as if they were part of the number. As the library does not (yet) convert Arabic decimal numbers to their pronunciations, they are converted to `(1,)`, the same as the result of converting any of the digits. In addition, the library detects negative signs by checking whether `-` etc. are preceding a digit and no `-` or unknown characters precede them and converts them to `(1,)` instead of `(6,)`.

If this is not desired, you may suppress this behavior by passing `decimal_check=False` (Note the `(3,)` between the `(1,)`s):

```python
>>> ToJyutping.g2p('咩話……你話上個月上堂學法文文法用咗 $50,000！？', decimal_check=False)
PhonemesList([(11, 46, 1), (22, 28, 2), (2,), (15, 47, 5), (22, 28, 6), (26, 84, 6), (17, 64, 3), (27, 92, 6), (26, 84, 5), (14, 69, 4), (23, 72, 6), (12, 35, 3), (11, 41, 2), (11, 41, 4), (12, 35, 3), (27, 78, 6), (24, 64, 2), (1,), (1,), (1,), (3,), (1,), (1,), (1,), (4,), (5,)])
```

#### Extra Punctuations & Custom Punctuation Map

The default punctuation mapping is comprehensive and should cover most of the use cases. However, you may add your own punctuations and symbols or override the built-in mapping by the `extra_puncts` option:

```python
>>> ToJyutping.g2p('咩話……你話上個月上堂學法文文法用咗 $50,000！？', extra_puncts={'$': 8, '！': 9})
PhonemesList([(13, 48, 1), (24, 30, 2), (2,), (17, 49, 5), (24, 30, 6), (28, 86, 6), (19, 66, 3), (29, 94, 6), (28, 86, 5), (16, 71, 4), (25, 74, 6), (14, 37, 3), (13, 43, 2), (13, 43, 4), (14, 37, 3), (29, 80, 6), (26, 66, 2), (8,), (1,), (1,), (1,), (1,), (1,), (1,), (9,), (5,)])
```

> [!IMPORTANT]
> - You cannot override pronunciations of Chinese characters by `extra_puncts`. Use `customize` for that purpose.
> - If you want to override a built-in punctuation, you will need to specify all “variants” of it by yourself. For example, `!`, `︕`, `﹗` and `！` should map to the same ID.

If any of the values in `extra_puncts` are greater than 7, the `offset` parameter is automatically adjusted to shift onsets and rhymes (and tones if `tone_same_seq`) by one plus the largest value, but you may modify it to suit your needs. **Read the instructions in the _[g2p Conversion Function](#grapheme-to-phoneme-conversion-function)_ section** before doing so.

If you would like to use your own mapping for some reason, you may specify the `puncts_map` option:

```python
>>> ToJyutping.g2p('咩話……你話上個月上堂學法文文法用咗 $50,000！？', puncts_map={'…': 2, '$': 3, '！': 4, '？': 5}, unknown_id=1)
PhonemesList([(9, 44, 1), (20, 26, 2), (2,), (13, 45, 5), (20, 26, 6), (24, 82, 6), (15, 62, 3), (25, 90, 6), (24, 82, 5), (12, 67, 4), (21, 70, 6), (10, 33, 3), (9, 39, 2), (9, 39, 4), (10, 33, 3), (25, 76, 6), (22, 62, 2), (3,), (1,), (1,), (1,), (1,), (1,), (1,), (4,), (5,)])
```

> [!IMPORTANT]
> - You **must** specify `unknown_id` if `puncts_map` is provided.
> - You cannot override pronunciations of Chinese characters by `puncts_map`. Use `customize` for that purpose.
> - You will need to specify all “variants” of a punctuation by yourself. For example, `!`, `︕`, `﹗` and `！` should map to the same ID.

The `offset` parameter is automatically calculated for you. By default, it shifts onsets and rhymes (and tones if `tone_same_seq`) by one plus the maximum of `unknown_id` and all the values in `puncts_map`. However, you may modify it to suit your needs. Again, be sure to **read the instructions in the _[g2p Conversion Function](#grapheme-to-phoneme-conversion-function)_ section** before doing so.

The `unknown_id` parameter may be used alone or with the `extra_puncts` option as well, but we generally do not recommend doing so. The `offset` parameter is computed similarly if it is greater than 7.

## Helper

```python
>>> ToJyutping.jyutping2ipa('jat1')
'jɐt̚˥'
>>> ToJyutping.jyutping2ipa('cin1 ngaa5')
't͡sʰiːn˥.ŋaː˩˧'
```

Note that autocorrection is intentionally not included in this helper, and an error is thrown if strings like `jyt6` are passed into the function.
Punctuation is ignored in the helper.
