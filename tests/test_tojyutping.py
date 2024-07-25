import unittest
import sys
import os
import timeit
import importlib
import statistics

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ToJyutping import ToJyutping

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

    def test_g2p(self):
        result = ToJyutping.g2p(self.test_string)
        expected = [(9, 32, 3), (11, 23, 1), (8, 58, 5), (18, 30, 3), (19, 49, 1), (10, 31, 4), (10, 79, 5), (5, 34, 2), (16, 33, 6), (19, 49, 3), (15, 57, 1), (14, 66, 2), (16, 52, 6), (5, 30, 1), (9, 38, 3), (19, 38, 5), (11, 56, 5), (14, 66, 5), (9, 22, 2), (5, 50, 6), (9, 20, 3), (8, 20, 3)]
        self.assertEqual(result, expected)

        result = ToJyutping.g2p(self.test_string, offset=100)
        expected = [(109, 132, 103), (111, 123, 101), (108, 158, 105), (118, 130, 103), (119, 149, 101), (110, 131, 104), (110, 179, 105), (105, 134, 102), (116, 133, 106), (119, 149, 103), (115, 157, 101), (114, 166, 102), (116, 152, 106), (105, 130, 101), (109, 138, 103), (119, 138, 105), (111, 156, 105), (114, 166, 105), (109, 122, 102), (105, 150, 106), (109, 120, 103), (108, 120, 103)]
        self.assertEqual(result, expected)

        result = ToJyutping.g2p(self.test_string, offset=(100, 200, 300))
        expected = [(109, 232, 303), (111, 223, 301), (108, 258, 305), (118, 230, 303), (119, 249, 301), (110, 231, 304), (110, 279, 305), (105, 234, 302), (116, 233, 306), (119, 249, 303), (115, 257, 301), (114, 266, 302), (116, 252, 306), (105, 230, 301), (109, 238, 303), (119, 238, 305), (111, 256, 305), (114, 266, 305), (109, 222, 302), (105, 250, 306), (109, 220, 303), (108, 220, 303)]
        self.assertEqual(result, expected)

        result = ToJyutping.g2p(self.test_string, tone_same_seq=True)
        expected = [(9, 32, 89), (11, 23, 87), (8, 58, 91), (18, 30, 89), (19, 49, 87), (10, 31, 90), (10, 79, 91), (5, 34, 88), (16, 33, 92), (19, 49, 89), (15, 57, 87), (14, 66, 88), (16, 52, 92), (5, 30, 87), (9, 38, 89), (19, 38, 91), (11, 56, 91), (14, 66, 91), (9, 22, 88), (5, 50, 92), (9, 20, 89), (8, 20, 89)]
        self.assertEqual(result, expected)

        result = ToJyutping.g2p(self.test_string, tone_same_seq=True, offset=100)
        expected = [(109, 132, 189), (111, 123, 187), (108, 158, 191), (118, 130, 189), (119, 149, 187), (110, 131, 190), (110, 179, 191), (105, 134, 188), (116, 133, 192), (119, 149, 189), (115, 157, 187), (114, 166, 188), (116, 152, 192), (105, 130, 187), (109, 138, 189), (119, 138, 191), (111, 156, 191), (114, 166, 191), (109, 122, 188), (105, 150, 192), (109, 120, 189), (108, 120, 189)]
        self.assertEqual(result, expected)

        result = ToJyutping.g2p(self.test_string, tone_same_seq=True, offset=(100, 200, 300))
        expected = [(109, 232, 389), (111, 223, 387), (108, 258, 391), (118, 230, 389), (119, 249, 387), (110, 231, 390), (110, 279, 391), (105, 234, 388), (116, 233, 392), (119, 249, 389), (115, 257, 387), (114, 266, 388), (116, 252, 392), (105, 230, 387), (109, 238, 389), (119, 238, 391), (111, 256, 391), (114, 266, 391), (109, 222, 388), (105, 250, 392), (109, 220, 389), (108, 220, 389)]
        self.assertEqual(result, expected)

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
        self.performance_test(lambda: importlib.reload(ToJyutping), repeat=100, expected_time=1000)

    def test_get_jyutping_list_performance(self):
        self.performance_test(lambda: ToJyutping.get_jyutping_list(self.test_string))

    def test_get_jyutping_performance(self):
        self.performance_test(lambda: ToJyutping.get_jyutping(self.test_string))

    def test_get_jyutping_text_performance(self):
        self.performance_test(lambda: ToJyutping.get_jyutping_text(self.test_string))

    def test_get_jyutping_candidates_performance(self):
        self.performance_test(lambda: ToJyutping.get_jyutping_candidates(self.test_string), expected_time=30)

    def test_get_ipa_list_performance(self):
        self.performance_test(lambda: ToJyutping.get_ipa_list(self.test_string))

    def test_get_ipa_performance(self):
        self.performance_test(lambda: ToJyutping.get_ipa(self.test_string))

    def test_get_ipa_text_performance(self):
        self.performance_test(lambda: ToJyutping.get_ipa_text(self.test_string))

    def test_get_ipa_candidates_performance(self):
        self.performance_test(lambda: ToJyutping.get_ipa_candidates(self.test_string), expected_time=30)

if __name__ == '__main__':
    unittest.main(verbosity=2)
