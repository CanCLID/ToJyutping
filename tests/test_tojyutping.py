import unittest
import sys
import os
import timeit
import importlib
import statistics

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ToJyutping import ToJyutping, Trie

class TestToJyutping(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.test_string = "咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。"

    def test_get_jyutping_list(self):
        result = ToJyutping.get_jyutping_list(self.test_string)
        expected = [('咁', 'gam3'), ('啱', 'ngaam1'), ('老', 'lou5'), ('世', 'sai3'), ('要', 'jiu1'), ('求', 'kau4'), ('佢', 'keoi5'), ('等', 'dang2'), ('陣', 'zan6'), ('要', 'jiu3'), ('開', 'hoi1'), ('會', 'wui2'), ('，', None), ('剩', 'zing6'), ('低', 'dai1'), ('嘅', 'ge3'), ('嘢', 'je5'), ('我', 'ngo5'), ('會', 'wui5'), ('搞', 'gaau2'), ('掂', 'dim6'), ('㗎', 'gaa3'), ('喇', 'laa3'), ('。', None)]
        self.assertEqual(result, expected)

    def test_get_jyutping(self):
        result = ToJyutping.get_jyutping(self.test_string)
        expected = "咁(gam3)啱(ngaam1)老(lou5)世(sai3)要(jiu1)求(kau4)佢(keoi5)等(dang2)陣(zan6)要(jiu3)開(hoi1)會(wui2)，剩(zing6)低(dai1)嘅(ge3)嘢(je5)我(ngo5)會(wui5)搞(gaau2)掂(dim6)㗎(gaa3)喇(laa3)。"
        self.assertEqual(result, expected)

    def test_get_jyutping_text(self):
        result = ToJyutping.get_jyutping_text(self.test_string)
        expected = "gam3 ngaam1 lou5 sai3 jiu1 kau4 keoi5 dang2 zan6 jiu3 hoi1 wui2, zing6 dai1 ge3 je5 ngo5 wui5 gaau2 dim6 gaa3 laa3."
        self.assertEqual(result, expected)

    def test_get_jyutping_candidates(self):
        result = ToJyutping.get_jyutping_candidates(self.test_string)
        expected = [('咁', ['gam3', 'gam2', 'gam1', 'gam4']), ('啱', ['ngaam1', 'aam1', 'am1', 'ngam1']), ('老', ['lou5', 'lou2']), ('世', ['sai3', 'sai2']), ('要', ['jiu1', 'jiu3', 'jiu2']), ('求', ['kau4']), ('佢', ['keoi5', 'heoi5']), ('等', ['dang2']), ('陣', ['zan6', 'zan2']), ('要', ['jiu3', 'jiu2', 'jiu1']), ('開', ['hoi1']), ('會', ['wui2', 'wui5', 'wui6', 'wui3', 'kui2', 'kui3', 'kwui2']), ('，', []), ('剩', ['zing6', 'sing6']), ('低', ['dai1']), ('嘅', ['ge3', 'ge2', 'koi2', 'koi3']), ('嘢', ['je5', 'e5']), ('我', ['ngo5', 'o5']), ('會', ['wui5', 'wui6', 'wui2', 'wui3', 'kui2', 'kui3', 'kwui2']), ('搞', ['gaau2']), ('掂', ['dim6', 'dim3', 'dim1']), ('㗎', ['gaa3', 'ga3', 'gaa2', 'gaa1', 'gaa4']), ('喇', ['laa3', 'laa1', 'laak3', 'laa5', 'laat3']), ('。', [])]
        self.assertEqual(result, expected)

    def test_get_ipa_list(self):
        result = ToJyutping.get_ipa_list(self.test_string)
        expected = [('咁', 'kɐm˧'), ('啱', 'ŋaːm˥'), ('老', 'lou̯˩˧'), ('世', 'sɐi̯˧'), ('要', 'jiːu̯˥'), ('求', 'kʰɐu̯˨˩'), ('佢', 'kʰɵy̑˩˧'), ('等', 'tɐŋ˧˥'), ('陣', 't͡sɐn˨'), ('要', 'jiːu̯˧'), ('開', 'hɔːi̯˥'), ('會', 'wuːi̯˧˥'), ('，', None), ('剩', 't͡seŋ˨'), ('低', 'tɐi̯˥'), ('嘅', 'kɛː˧'), ('嘢', 'jɛː˩˧'), ('我', 'ŋɔː˩˧'), ('會', 'wuːi̯˩˧'), ('搞', 'kaːu̯˧˥'), ('掂', 'tiːm˨'), ('㗎', 'kaː˧'), ('喇', 'laː˧'), ('。', None)]
        self.assertEqual(result, expected)

    def test_get_ipa(self):
        result = ToJyutping.get_ipa(self.test_string)
        expected = "咁[kɐm˧]啱[ŋaːm˥]老[lou̯˩˧]世[sɐi̯˧]要[jiːu̯˥]求[kʰɐu̯˨˩]佢[kʰɵy̑˩˧]等[tɐŋ˧˥]陣[t͡sɐn˨]要[jiːu̯˧]開[hɔːi̯˥]會[wuːi̯˧˥]，剩[t͡seŋ˨]低[tɐi̯˥]嘅[kɛː˧]嘢[jɛː˩˧]我[ŋɔː˩˧]會[wuːi̯˩˧]搞[kaːu̯˧˥]掂[tiːm˨]㗎[kaː˧]喇[laː˧]。"
        self.assertEqual(result, expected)

    def test_get_ipa_text(self):
        result = ToJyutping.get_ipa_text(self.test_string)
        expected = 'kɐm˧.ŋaːm˥.lou̯˩˧.sɐi̯˧.jiːu̯˥.kʰɐu̯˨˩.kʰɵy̑˩˧.tɐŋ˧˥.t͡sɐn˨.jiːu̯˧.hɔːi̯˥.wuːi̯˧˥ | t͡seŋ˨.tɐi̯˥.kɛː˧.jɛː˩˧.ŋɔː˩˧.wuːi̯˩˧.kaːu̯˧˥.tiːm˨.kaː˧.laː˧'
        self.assertEqual(result, expected)

    def test_get_ipa_candidates(self):
        result = ToJyutping.get_ipa_candidates(self.test_string)
        expected = [('咁', ['kɐm˧', 'kɐm˧˥', 'kɐm˥', 'kɐm˨˩']), ('啱', ['ŋaːm˥', 'aːm˥', 'ɐm˥', 'ŋɐm˥']), ('老', ['lou̯˩˧', 'lou̯˧˥']), ('世', ['sɐi̯˧', 'sɐi̯˧˥']), ('要', ['jiːu̯˥', 'jiːu̯˧', 'jiːu̯˧˥']), ('求', ['kʰɐu̯˨˩']), ('佢', ['kʰɵy̑˩˧', 'hɵy̑˩˧']), ('等', ['tɐŋ˧˥']), ('陣', ['t͡sɐn˨', 't͡sɐn˧˥']), ('要', ['jiːu̯˧', 'jiːu̯˧˥', 'jiːu̯˥']), ('開', ['hɔːi̯˥']), ('會', ['wuːi̯˧˥', 'wuːi̯˩˧', 'wuːi̯˨', 'wuːi̯˧', 'kʰuːi̯˧˥', 'kʰuːi̯˧', 'kʷʰuːi̯˧˥']), ('，', []), ('剩', ['t͡seŋ˨', 'seŋ˨']), ('低', ['tɐi̯˥']), ('嘅', ['kɛː˧', 'kɛː˧˥', 'kʰɔːi̯˧˥', 'kʰɔːi̯˧']), ('嘢', ['jɛː˩˧', 'ɛː˩˧']), ('我', ['ŋɔː˩˧', 'ɔː˩˧']), ('會', ['wuːi̯˩˧', 'wuːi̯˨', 'wuːi̯˧˥', 'wuːi̯˧', 'kʰuːi̯˧˥', 'kʰuːi̯˧', 'kʷʰuːi̯˧˥']), ('搞', ['kaːu̯˧˥']), ('掂', ['tiːm˨', 'tiːm˧', 'tiːm˥']), ('㗎', ['kaː˧', 'kɐ˧', 'kaː˧˥', 'kaː˥', 'kaː˨˩']), ('喇', ['laː˧', 'laː˥', 'laːk̚˧', 'laː˩˧', 'laːt̚˧']), ('。', [])]
        self.assertEqual(result, expected)

    def test_customize(self):
        converter_lesson = ToJyutping.customize({'上堂': None, '分數': 'fan6 sou3'})
        result = converter_lesson.get_jyutping_text('上堂終於講到分數')
        expected = 'soeng6 tong4 zung1 jyu1 gong2 dou3 fan6 sou3'
        self.assertEqual(result, expected)

        converter_studious = ToJyutping.customize({'好學生': None})
        result = converter_studious.get_jyutping_text('好學生')
        expected = 'hou3 hok6 saang1'
        self.assertEqual(result, expected)

        converter_good_student = converter_studious.customize({'好學': None})
        result = converter_good_student.get_jyutping_text('好學生')
        expected = 'hou2 hok6 saang1'
        self.assertEqual(result, expected)

        converter_dou2 = converter_lesson.customize({'到': 'dou2'})
        converter_None = converter_lesson.customize({'到': None})

        result = converter_dou2.get_jyutping_text('上堂終於講到分數')
        expected = 'soeng6 tong4 zung1 jyu1 gong2 dou2 fan6 sou3'
        self.assertEqual(result, expected)

        result = converter_None.get_jyutping_text('上堂終於講到分數')
        expected = 'soeng6 tong4 zung1 jyu1 gong2 […] fan6 sou3'
        self.assertEqual(result, expected)

        result_dou2 = converter_dou2.get_jyutping_text('笑到轆地')
        result_None = converter_None.get_jyutping_text('笑到轆地')
        expected = 'siu3 dou3 luk1 dei2'
        self.assertEqual(result_dou2, expected)
        self.assertEqual(result_None, expected)

        converter_another_lesson = ToJyutping.customize({'上': None, '分': 'fan6'})
        result = converter_another_lesson.get_jyutping_text('上堂終於講到分數')
        expected = 'soeng5 tong4 zung1 jyu1 gong2 dou3 fan6 sou3'
        self.assertEqual(result, expected)

        converter_dou2_dou3 = converter_lesson.customize({'到': ['dou2', 'dou3', 'dou2']})
        result = converter_dou2_dou3.get_jyutping_candidates('到')
        expected = [('到', ['dou2', 'dou3'])]
        self.assertEqual(result, expected)

        with self.assertRaises(ValueError):
            ToJyutping.customize({'': None})

        with self.assertRaises(ValueError):
            ToJyutping.customize({'foo': ''})

        with self.assertRaises(ValueError):
            ToJyutping.customize({'foo': ['']})

        with self.assertRaises(ValueError):
            ToJyutping.customize({'foo': 'foo'})

        with self.assertRaises(ValueError):
            ToJyutping.customize({'foo': 'foo1'})

        with self.assertRaises(ValueError):
            ToJyutping.customize({'foo': 'foo1 bar2 baz3'})

    def test_g2p(self):
        # This test is designed to check if:
        # - Conversions of characters with multiple pronunciations are correct
        # - Consecutive punctuations of the same type are collapsed
        # - Consecutive unknown character filler are not collapsed
        # - Separators between digits and negative sign before digits are treated as part of the number and therefore as unknown characters
        # - The `offset` and `puncts_offset` arguments shift the IDs correctly
        # - The tones are not shifted if `tone_same_seq` is `False` and `offset` is not provided
        # - /\p{Symbol}/u is not forbidden in `extra_puncts` and `puncts_map`
        # - The `offset` argument defaults to the one plus the maximum of `unknown_id` and all the values in `puncts_map` if `puncts_map` is provided, otherwise one plus the number of the maximum of default symbols and all the values in `extra_puncts` if `extra_puncts` is provided, otherwise one plus the number of default symbols
        # - The `puncts_offset` argument defaults to zero if `puncts_map` is provided, otherwise one
        # - `offset` and `puncts_offset` do not affect each other
        # - An error is raised if one of `puncts_map` and `unknown_id` is provided but the other isn’t
        # - An error is raised if `extra_puncts` and `puncts_map` are both provided

        g2p_test_string = '咩話……你話上個月上堂學法文文法用咗 $50,000！？'
        extra_puncts = {'$': 8, '！': 9}
        puncts_map = {'…': 1, '$': 2, '！': 3, '？': 4}
        expected_lengths = [2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        result = ToJyutping.g2p(g2p_test_string)
        expected_phonemes = [(11, 46, 1), (22, 28, 2), (2,), (15, 47, 5), (22, 28, 6), (26, 84, 6), (17, 64, 3), (27, 92, 6), (26, 84, 5), (14, 69, 4), (23, 72, 6), (12, 35, 3), (11, 41, 2), (11, 41, 4), (12, 35, 3), (27, 78, 6), (24, 64, 2), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (4,), (5,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [11, 46, 22, 28, 2, 15, 47, 22, 28, 26, 84, 17, 64, 27, 92, 26, 84, 14, 69, 23, 72, 12, 35, 11, 41, 11, 41, 12, 35, 27, 78, 24, 64, 1, 1, 1, 1, 1, 1, 1, 4, 5]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [1, 1, 2, 2, 0, 5, 5, 6, 6, 6, 6, 3, 3, 6, 6, 5, 5, 4, 4, 6, 6, 3, 3, 2, 2, 4, 4, 3, 3, 6, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, offset=0)
        expected_phonemes = [(3, 38, 1), (14, 20, 2), (2,), (7, 39, 5), (14, 20, 6), (18, 76, 6), (9, 56, 3), (19, 84, 6), (18, 76, 5), (6, 61, 4), (15, 64, 6), (4, 27, 3), (3, 33, 2), (3, 33, 4), (4, 27, 3), (19, 70, 6), (16, 56, 2), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (4,), (5,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [3, 38, 14, 20, 2, 7, 39, 14, 20, 18, 76, 9, 56, 19, 84, 18, 76, 6, 61, 15, 64, 4, 27, 3, 33, 3, 33, 4, 27, 19, 70, 16, 56, 1, 1, 1, 1, 1, 1, 1, 4, 5]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [1, 1, 2, 2, 0, 5, 5, 6, 6, 6, 6, 3, 3, 6, 6, 5, 5, 4, 4, 6, 6, 3, 3, 2, 2, 4, 4, 3, 3, 6, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, offset=(100, 200, 300), puncts_offset=400)
        expected_phonemes = [(103, 238, 301), (114, 220, 302), (401,), (107, 239, 305), (114, 220, 306), (118, 276, 306), (109, 256, 303), (119, 284, 306), (118, 276, 305), (106, 261, 304), (115, 264, 306), (104, 227, 303), (103, 233, 302), (103, 233, 304), (104, 227, 303), (119, 270, 306), (116, 256, 302), (400,), (400,), (400,), (400,), (400,), (400,), (400,), (403,), (404,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [103, 238, 114, 220, 401, 107, 239, 114, 220, 118, 276, 109, 256, 119, 284, 118, 276, 106, 261, 115, 264, 104, 227, 103, 233, 103, 233, 104, 227, 119, 270, 116, 256, 400, 400, 400, 400, 400, 400, 400, 403, 404]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [301, 301, 302, 302, 0, 305, 305, 306, 306, 306, 306, 303, 303, 306, 306, 305, 305, 304, 304, 306, 306, 303, 303, 302, 302, 304, 304, 303, 303, 306, 306, 302, 302, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, tone_same_seq=True)
        expected_phonemes = [(11, 46, 95), (22, 28, 96), (2,), (15, 47, 99), (22, 28, 100), (26, 84, 100), (17, 64, 97), (27, 92, 100), (26, 84, 99), (14, 69, 98), (23, 72, 100), (12, 35, 97), (11, 41, 96), (11, 41, 98), (12, 35, 97), (27, 78, 100), (24, 64, 96), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (4,), (5,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [11, 46, 22, 28, 2, 15, 47, 22, 28, 26, 84, 17, 64, 27, 92, 26, 84, 14, 69, 23, 72, 12, 35, 11, 41, 11, 41, 12, 35, 27, 78, 24, 64, 1, 1, 1, 1, 1, 1, 1, 4, 5]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [95, 95, 96, 96, 0, 99, 99, 100, 100, 100, 100, 97, 97, 100, 100, 99, 99, 98, 98, 100, 100, 97, 97, 96, 96, 98, 98, 97, 97, 100, 100, 96, 96, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, tone_same_seq=True, offset=0)
        expected_phonemes = [(3, 38, 87), (14, 20, 88), (2,), (7, 39, 91), (14, 20, 92), (18, 76, 92), (9, 56, 89), (19, 84, 92), (18, 76, 91), (6, 61, 90), (15, 64, 92), (4, 27, 89), (3, 33, 88), (3, 33, 90), (4, 27, 89), (19, 70, 92), (16, 56, 88), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (4,), (5,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [3, 38, 14, 20, 2, 7, 39, 14, 20, 18, 76, 9, 56, 19, 84, 18, 76, 6, 61, 15, 64, 4, 27, 3, 33, 3, 33, 4, 27, 19, 70, 16, 56, 1, 1, 1, 1, 1, 1, 1, 4, 5]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [87, 87, 88, 88, 0, 91, 91, 92, 92, 92, 92, 89, 89, 92, 92, 91, 91, 90, 90, 92, 92, 89, 89, 88, 88, 90, 90, 89, 89, 92, 92, 88, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, tone_same_seq=True, offset=(100, 200, 300), puncts_offset=400)
        expected_phonemes = [(103, 238, 387), (114, 220, 388), (401,), (107, 239, 391), (114, 220, 392), (118, 276, 392), (109, 256, 389), (119, 284, 392), (118, 276, 391), (106, 261, 390), (115, 264, 392), (104, 227, 389), (103, 233, 388), (103, 233, 390), (104, 227, 389), (119, 270, 392), (116, 256, 388), (400,), (400,), (400,), (400,), (400,), (400,), (400,), (403,), (404,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [103, 238, 114, 220, 401, 107, 239, 114, 220, 118, 276, 109, 256, 119, 284, 118, 276, 106, 261, 115, 264, 104, 227, 103, 233, 103, 233, 104, 227, 119, 270, 116, 256, 400, 400, 400, 400, 400, 400, 400, 403, 404]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [387, 387, 388, 388, 0, 391, 391, 392, 392, 392, 392, 389, 389, 392, 392, 391, 391, 390, 390, 392, 392, 389, 389, 388, 388, 390, 390, 389, 389, 392, 392, 388, 388, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, extra_puncts=extra_puncts)
        expected_phonemes = [(13, 48, 1), (24, 30, 2), (2,), (17, 49, 5), (24, 30, 6), (28, 86, 6), (19, 66, 3), (29, 94, 6), (28, 86, 5), (16, 71, 4), (25, 74, 6), (14, 37, 3), (13, 43, 2), (13, 43, 4), (14, 37, 3), (29, 80, 6), (26, 66, 2), (8,), (1,), (1,), (1,), (1,), (1,), (1,), (9,), (5,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [13, 48, 24, 30, 2, 17, 49, 24, 30, 28, 86, 19, 66, 29, 94, 28, 86, 16, 71, 25, 74, 14, 37, 13, 43, 13, 43, 14, 37, 29, 80, 26, 66, 8, 1, 1, 1, 1, 1, 1, 9, 5]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [1, 1, 2, 2, 0, 5, 5, 6, 6, 6, 6, 3, 3, 6, 6, 5, 5, 4, 4, 6, 6, 3, 3, 2, 2, 4, 4, 3, 3, 6, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, extra_puncts=extra_puncts, offset=0)
        expected_phonemes = [(3, 38, 1), (14, 20, 2), (2,), (7, 39, 5), (14, 20, 6), (18, 76, 6), (9, 56, 3), (19, 84, 6), (18, 76, 5), (6, 61, 4), (15, 64, 6), (4, 27, 3), (3, 33, 2), (3, 33, 4), (4, 27, 3), (19, 70, 6), (16, 56, 2), (8,), (1,), (1,), (1,), (1,), (1,), (1,), (9,), (5,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [3, 38, 14, 20, 2, 7, 39, 14, 20, 18, 76, 9, 56, 19, 84, 18, 76, 6, 61, 15, 64, 4, 27, 3, 33, 3, 33, 4, 27, 19, 70, 16, 56, 8, 1, 1, 1, 1, 1, 1, 9, 5]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [1, 1, 2, 2, 0, 5, 5, 6, 6, 6, 6, 3, 3, 6, 6, 5, 5, 4, 4, 6, 6, 3, 3, 2, 2, 4, 4, 3, 3, 6, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, extra_puncts=extra_puncts, offset=(100, 200, 300), puncts_offset=400)
        expected_phonemes = [(103, 238, 301), (114, 220, 302), (401,), (107, 239, 305), (114, 220, 306), (118, 276, 306), (109, 256, 303), (119, 284, 306), (118, 276, 305), (106, 261, 304), (115, 264, 306), (104, 227, 303), (103, 233, 302), (103, 233, 304), (104, 227, 303), (119, 270, 306), (116, 256, 302), (407,), (400,), (400,), (400,), (400,), (400,), (400,), (408,), (404,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [103, 238, 114, 220, 401, 107, 239, 114, 220, 118, 276, 109, 256, 119, 284, 118, 276, 106, 261, 115, 264, 104, 227, 103, 233, 103, 233, 104, 227, 119, 270, 116, 256, 407, 400, 400, 400, 400, 400, 400, 408, 404]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [301, 301, 302, 302, 0, 305, 305, 306, 306, 306, 306, 303, 303, 306, 306, 305, 305, 304, 304, 306, 306, 303, 303, 302, 302, 304, 304, 303, 303, 306, 306, 302, 302, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, tone_same_seq=True, extra_puncts=extra_puncts)
        expected_phonemes = [(13, 48, 97), (24, 30, 98), (2,), (17, 49, 101), (24, 30, 102), (28, 86, 102), (19, 66, 99), (29, 94, 102), (28, 86, 101), (16, 71, 100), (25, 74, 102), (14, 37, 99), (13, 43, 98), (13, 43, 100), (14, 37, 99), (29, 80, 102), (26, 66, 98), (8,), (1,), (1,), (1,), (1,), (1,), (1,), (9,), (5,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [13, 48, 24, 30, 2, 17, 49, 24, 30, 28, 86, 19, 66, 29, 94, 28, 86, 16, 71, 25, 74, 14, 37, 13, 43, 13, 43, 14, 37, 29, 80, 26, 66, 8, 1, 1, 1, 1, 1, 1, 9, 5]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [97, 97, 98, 98, 0, 101, 101, 102, 102, 102, 102, 99, 99, 102, 102, 101, 101, 100, 100, 102, 102, 99, 99, 98, 98, 100, 100, 99, 99, 102, 102, 98, 98, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, tone_same_seq=True, extra_puncts=extra_puncts, offset=0)
        expected_phonemes = [(3, 38, 87), (14, 20, 88), (2,), (7, 39, 91), (14, 20, 92), (18, 76, 92), (9, 56, 89), (19, 84, 92), (18, 76, 91), (6, 61, 90), (15, 64, 92), (4, 27, 89), (3, 33, 88), (3, 33, 90), (4, 27, 89), (19, 70, 92), (16, 56, 88), (8,), (1,), (1,), (1,), (1,), (1,), (1,), (9,), (5,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [3, 38, 14, 20, 2, 7, 39, 14, 20, 18, 76, 9, 56, 19, 84, 18, 76, 6, 61, 15, 64, 4, 27, 3, 33, 3, 33, 4, 27, 19, 70, 16, 56, 8, 1, 1, 1, 1, 1, 1, 9, 5]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [87, 87, 88, 88, 0, 91, 91, 92, 92, 92, 92, 89, 89, 92, 92, 91, 91, 90, 90, 92, 92, 89, 89, 88, 88, 90, 90, 89, 89, 92, 92, 88, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, tone_same_seq=True, extra_puncts=extra_puncts, offset=(100, 200, 300), puncts_offset=400)
        expected_phonemes = [(103, 238, 387), (114, 220, 388), (401,), (107, 239, 391), (114, 220, 392), (118, 276, 392), (109, 256, 389), (119, 284, 392), (118, 276, 391), (106, 261, 390), (115, 264, 392), (104, 227, 389), (103, 233, 388), (103, 233, 390), (104, 227, 389), (119, 270, 392), (116, 256, 388), (407,), (400,), (400,), (400,), (400,), (400,), (400,), (408,), (404,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [103, 238, 114, 220, 401, 107, 239, 114, 220, 118, 276, 109, 256, 119, 284, 118, 276, 106, 261, 115, 264, 104, 227, 103, 233, 103, 233, 104, 227, 119, 270, 116, 256, 407, 400, 400, 400, 400, 400, 400, 408, 404]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [387, 387, 388, 388, 0, 391, 391, 392, 392, 392, 392, 389, 389, 392, 392, 391, 391, 390, 390, 392, 392, 389, 389, 388, 388, 390, 390, 389, 389, 392, 392, 388, 388, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, puncts_map=puncts_map, unknown_id=0)
        expected_phonemes = [(8, 43, 1), (19, 25, 2), (1,), (12, 44, 5), (19, 25, 6), (23, 81, 6), (14, 61, 3), (24, 89, 6), (23, 81, 5), (11, 66, 4), (20, 69, 6), (9, 32, 3), (8, 38, 2), (8, 38, 4), (9, 32, 3), (24, 75, 6), (21, 61, 2), (2,), (0,), (0,), (0,), (0,), (0,), (0,), (3,), (4,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [8, 43, 19, 25, 1, 12, 44, 19, 25, 23, 81, 14, 61, 24, 89, 23, 81, 11, 66, 20, 69, 9, 32, 8, 38, 8, 38, 9, 32, 24, 75, 21, 61, 2, 0, 0, 0, 0, 0, 0, 3, 4]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [1, 1, 2, 2, 0, 5, 5, 6, 6, 6, 6, 3, 3, 6, 6, 5, 5, 4, 4, 6, 6, 3, 3, 2, 2, 4, 4, 3, 3, 6, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, puncts_map=puncts_map, unknown_id=0, offset=0)
        expected_phonemes = [(3, 38, 1), (14, 20, 2), (1,), (7, 39, 5), (14, 20, 6), (18, 76, 6), (9, 56, 3), (19, 84, 6), (18, 76, 5), (6, 61, 4), (15, 64, 6), (4, 27, 3), (3, 33, 2), (3, 33, 4), (4, 27, 3), (19, 70, 6), (16, 56, 2), (2,), (0,), (0,), (0,), (0,), (0,), (0,), (3,), (4,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [3, 38, 14, 20, 1, 7, 39, 14, 20, 18, 76, 9, 56, 19, 84, 18, 76, 6, 61, 15, 64, 4, 27, 3, 33, 3, 33, 4, 27, 19, 70, 16, 56, 2, 0, 0, 0, 0, 0, 0, 3, 4]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [1, 1, 2, 2, 0, 5, 5, 6, 6, 6, 6, 3, 3, 6, 6, 5, 5, 4, 4, 6, 6, 3, 3, 2, 2, 4, 4, 3, 3, 6, 6, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, puncts_map=puncts_map, unknown_id=0, offset=(100, 200, 300), puncts_offset=400)
        expected_phonemes = [(103, 238, 301), (114, 220, 302), (401,), (107, 239, 305), (114, 220, 306), (118, 276, 306), (109, 256, 303), (119, 284, 306), (118, 276, 305), (106, 261, 304), (115, 264, 306), (104, 227, 303), (103, 233, 302), (103, 233, 304), (104, 227, 303), (119, 270, 306), (116, 256, 302), (402,), (400,), (400,), (400,), (400,), (400,), (400,), (403,), (404,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [103, 238, 114, 220, 401, 107, 239, 114, 220, 118, 276, 109, 256, 119, 284, 118, 276, 106, 261, 115, 264, 104, 227, 103, 233, 103, 233, 104, 227, 119, 270, 116, 256, 402, 400, 400, 400, 400, 400, 400, 403, 404]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [301, 301, 302, 302, 0, 305, 305, 306, 306, 306, 306, 303, 303, 306, 306, 305, 305, 304, 304, 306, 306, 303, 303, 302, 302, 304, 304, 303, 303, 306, 306, 302, 302, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, tone_same_seq=True, puncts_map=puncts_map, unknown_id=0)
        expected_phonemes = [(8, 43, 92), (19, 25, 93), (1,), (12, 44, 96), (19, 25, 97), (23, 81, 97), (14, 61, 94), (24, 89, 97), (23, 81, 96), (11, 66, 95), (20, 69, 97), (9, 32, 94), (8, 38, 93), (8, 38, 95), (9, 32, 94), (24, 75, 97), (21, 61, 93), (2,), (0,), (0,), (0,), (0,), (0,), (0,), (3,), (4,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [8, 43, 19, 25, 1, 12, 44, 19, 25, 23, 81, 14, 61, 24, 89, 23, 81, 11, 66, 20, 69, 9, 32, 8, 38, 8, 38, 9, 32, 24, 75, 21, 61, 2, 0, 0, 0, 0, 0, 0, 3, 4]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [92, 92, 93, 93, 0, 96, 96, 97, 97, 97, 97, 94, 94, 97, 97, 96, 96, 95, 95, 97, 97, 94, 94, 93, 93, 95, 95, 94, 94, 97, 97, 93, 93, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, tone_same_seq=True, puncts_map=puncts_map, unknown_id=0, offset=0)
        expected_phonemes = [(3, 38, 87), (14, 20, 88), (1,), (7, 39, 91), (14, 20, 92), (18, 76, 92), (9, 56, 89), (19, 84, 92), (18, 76, 91), (6, 61, 90), (15, 64, 92), (4, 27, 89), (3, 33, 88), (3, 33, 90), (4, 27, 89), (19, 70, 92), (16, 56, 88), (2,), (0,), (0,), (0,), (0,), (0,), (0,), (3,), (4,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [3, 38, 14, 20, 1, 7, 39, 14, 20, 18, 76, 9, 56, 19, 84, 18, 76, 6, 61, 15, 64, 4, 27, 3, 33, 3, 33, 4, 27, 19, 70, 16, 56, 2, 0, 0, 0, 0, 0, 0, 3, 4]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [87, 87, 88, 88, 0, 91, 91, 92, 92, 92, 92, 89, 89, 92, 92, 91, 91, 90, 90, 92, 92, 89, 89, 88, 88, 90, 90, 89, 89, 92, 92, 88, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        result = ToJyutping.g2p(g2p_test_string, tone_same_seq=True, puncts_map=puncts_map, unknown_id=0, offset=(100, 200, 300), puncts_offset=400)
        expected_phonemes = [(103, 238, 387), (114, 220, 388), (401,), (107, 239, 391), (114, 220, 392), (118, 276, 392), (109, 256, 389), (119, 284, 392), (118, 276, 391), (106, 261, 390), (115, 264, 392), (104, 227, 389), (103, 233, 388), (103, 233, 390), (104, 227, 389), (119, 270, 392), (116, 256, 388), (402,), (400,), (400,), (400,), (400,), (400,), (400,), (403,), (404,)]
        self.assertEqual(list(result), expected_phonemes)
        expected_segmentals = [103, 238, 114, 220, 401, 107, 239, 114, 220, 118, 276, 109, 256, 119, 284, 118, 276, 106, 261, 115, 264, 104, 227, 103, 233, 103, 233, 104, 227, 119, 270, 116, 256, 402, 400, 400, 400, 400, 400, 400, 403, 404]
        self.assertEqual(result.segmentals, expected_segmentals)
        expected_tones = [387, 387, 388, 388, 0, 391, 391, 392, 392, 392, 392, 389, 389, 392, 392, 391, 391, 390, 390, 392, 392, 389, 389, 388, 388, 390, 390, 389, 389, 392, 392, 388, 388, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result.tones, expected_tones)
        self.assertEqual(result.lengths, expected_lengths)

        with self.assertRaises(ValueError):
            ToJyutping.g2p(g2p_test_string, puncts_map=puncts_map)

        with self.assertRaises(ValueError):
            ToJyutping.g2p(g2p_test_string, unknown_id=0)

        with self.assertRaises(ValueError):
            ToJyutping.g2p(g2p_test_string, extra_puncts=extra_puncts, puncts_map=puncts_map)

        with self.assertRaises(ValueError):
            ToJyutping.g2p(g2p_test_string, extra_puncts=extra_puncts, unknown_id=0)

    def test_jyutping2ipa(self):
        result = ToJyutping.jyutping2ipa("cin1 ngaa5")
        expected = "t͡sʰiːn˥.ŋaː˩˧"
        self.assertEqual(result, expected)

class TestToJyutpingPerformance(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.test_string = "咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。" * 100  # Repeat the string to make it longer

    def performance_test(self, stmt, repeat=1000, expected_time=10):
        # Measure the execution timings
        exec_timings = [t * 1000 for t in timeit.repeat(stmt, repeat=repeat, number=1)]

        # Calculate statistics
        mean = statistics.fmean(exec_timings)
        stdev = statistics.stdev(exec_timings)
        n = 40
        quantiles = statistics.quantiles(exec_timings, n=n, method="inclusive")
        if len(quantiles) == n - 1:
            # There is an implementation mistake in CPython,
            # method="inclusive" supposedly should return a list with n + 1 data points
            quantiles = [min(exec_timings), *quantiles, max(exec_timings)]

        # Print statistics
        print("Benchmark:")
        print(f"Time (mean ± ּσ):   {mean:8.3f} ms ± {stdev:8.3f} ms")
        print(f"Range (min … ּmax): {quantiles[0]:8.3f} ms … {quantiles[-1]:8.3f} ms")
        print(f"p75, p95, p975:    {quantiles[30]:8.3f} ms,  {quantiles[38]:8.3f} ms,  {quantiles[39]:8.3f} ms")

        # Check if the performance is below the threshold
        self.assertLess(mean, expected_time, "Performance is below expectation")

    def test_to_jyutping_init_performance(self):
        self.performance_test(lambda: importlib.reload(Trie), repeat=100, expected_time=1000)

    def test_get_jyutping_list_performance(self):
        self.performance_test(lambda: ToJyutping.get_jyutping_list(self.test_string))

    def test_get_jyutping_performance(self):
        self.performance_test(lambda: ToJyutping.get_jyutping(self.test_string))

    def test_get_jyutping_text_performance(self):
        self.performance_test(lambda: ToJyutping.get_jyutping_text(self.test_string))

    def test_get_jyutping_candidates_performance(self):
        self.performance_test(lambda: ToJyutping.get_jyutping_candidates(self.test_string))

    def test_get_ipa_list_performance(self):
        self.performance_test(lambda: ToJyutping.get_ipa_list(self.test_string))

    def test_get_ipa_performance(self):
        self.performance_test(lambda: ToJyutping.get_ipa(self.test_string))

    def test_get_ipa_text_performance(self):
        self.performance_test(lambda: ToJyutping.get_ipa_text(self.test_string))

    def test_get_ipa_candidates_performance(self):
        self.performance_test(lambda: ToJyutping.get_ipa_candidates(self.test_string))

if __name__ == '__main__':
    unittest.main(verbosity=2)
