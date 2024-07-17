import unittest
import sys
import os
import timeit

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ToJyutping import ToJyutping

class TestToJyutping(unittest.TestCase):

    def test_get_jyutping_performance(self):
        test_string = "咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。" * 100  # Repeat the string to make it longer
        
        # Number of iterations for timing
        number = 100
        
        # Measure the execution time
        execution_time = timeit.timeit(lambda: ToJyutping.get_jyutping(test_string), number=number)
        
        # Calculate average time per call
        avg_time = execution_time / number
        
        print(f"\nPerformance test for get_jyutping():")
        print(f"Average execution time: {avg_time:.6f} seconds")
        
        # You can set a threshold for acceptable performance
        self.assertLess(avg_time, 0.01, "Performance of get_jyutping() is below expectations")

    def test_get_jyutping_list(self):
        result = ToJyutping.get_jyutping_list("咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。")
        expected = [('咁', 'gam3'), ('啱', 'ngaam1'), ('老', 'lou5'), ('世', 'sai3'), ('要', 'jiu1'), ('求', 'kau4'), ('佢', 'keoi5'), ('等', 'dang2'), ('陣', 'zan6'), ('要', 'jiu3'), ('開', 'hoi1'), ('會', 'wui2'), ('，', None), ('剩', 'zing6'), ('低', 'dai1'), ('嘅', 'ge3'), ('嘢', 'je5'), ('我', 'ngo5'), ('會', 'wui5'), ('搞', 'gaau2'), ('掂', 'dim6'), ('㗎', 'gaa3'), ('喇', 'laa3'), ('。', None)]
        self.assertEqual(result, expected)

    def test_get_jyutping(self):
        result = ToJyutping.get_jyutping("咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。")
        expected = "咁(gam3)啱(ngaam1)老(lou5)世(sai3)要(jiu1)求(kau4)佢(keoi5)等(dang2)陣(zan6)要(jiu3)開(hoi1)會(wui2)，剩(zing6)低(dai1)嘅(ge3)嘢(je5)我(ngo5)會(wui5)搞(gaau2)掂(dim6)㗎(gaa3)喇(laa3)。"
        self.assertEqual(result, expected)

    def test_get_jyutping_text(self):
        result = ToJyutping.get_jyutping_text("咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。")
        expected = "gam3 ngaam1 lou5 sai3 jiu1 kau4 keoi5 dang2 zan6 jiu3 hoi1 wui2, zing6 dai1 ge3 je5 ngo5 wui5 gaau2 dim6 gaa3 laa3."
        self.assertEqual(result, expected)

    def test_get_jyutping_candidates(self):
        result = ToJyutping.get_jyutping_candidates("咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。")
        expected = [('咁', ['gam3', 'gam2', 'gam1', 'gam4']), ('啱', ['ngaam1', 'aam1', 'am1', 'ngam1']), ('老', ['lou5', 'lou2']), ('世', ['sai3', 'sai2']), ('要', ['jiu1', 'jiu3', 'jiu2']), ('求', ['kau4']), ('佢', ['keoi5', 'heoi5']), ('等', ['dang2']), ('陣', ['zan6', 'zan2']), ('要', ['jiu3', 'jiu2', 'jiu1']), ('開', ['hoi1']), ('會', ['wui2', 'wui5', 'wui6', 'wui3', 'kui2', 'kui3', 'kwui2']), ('，', []), ('剩', ['zing6', 'sing6']), ('低', ['dai1']), ('嘅', ['ge3', 'ge2', 'koi2', 'koi3']), ('嘢', ['je5', 'e5']), ('我', ['ngo5', 'o5']), ('會', ['wui5', 'wui6', 'wui2', 'wui3', 'kui2', 'kui3', 'kwui2']), ('搞', ['gaau2']), ('掂', ['dim6', 'dim3', 'dim1']), ('㗎', ['gaa3', 'ga3', 'gaa2', 'gaa1', 'gaa4']), ('喇', ['laa3', 'laa1', 'laak3', 'laa5', 'laat3']), ('。', [])]
        self.assertEqual(result, expected)

    def test_get_ipa_list(self):
        result = ToJyutping.get_ipa_list("咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。")
        expected = [('咁', 'kɐm˧'), ('啱', 'ŋaːm˥'), ('老', 'lou̯˩˧'), ('世', 'sɐi̯˧'), ('要', 'jiːu̯˥'), ('求', 'kʰɐu̯˨˩'), ('佢', 'kʰɵy̑˩˧'), ('等', 'tɐŋ˧˥'), ('陣', 't͡sɐn˨'), ('要', 'jiːu̯˧'), ('開', 'hɔːi̯˥'), ('會', 'wuːi̯˧˥'), ('，', None), ('剩', 't͡seŋ˨'), ('低', 'tɐi̯˥'), ('嘅', 'kɛː˧'), ('嘢', 'jɛː˩˧'), ('我', 'ŋɔː˩˧'), ('會', 'wuːi̯˩˧'), ('搞', 'kaːu̯˧˥'), ('掂', 'tiːm˨'), ('㗎', 'kaː˧'), ('喇', 'laː˧'), ('。', None)]
        self.assertEqual(result, expected)

    def test_get_ipa(self):
        result = ToJyutping.get_ipa("咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。")
        expected = "咁[kɐm˧]啱[ŋaːm˥]老[lou̯˩˧]世[sɐi̯˧]要[jiːu̯˥]求[kʰɐu̯˨˩]佢[kʰɵy̑˩˧]等[tɐŋ˧˥]陣[t͡sɐn˨]要[jiːu̯˧]開[hɔːi̯˥]會[wuːi̯˧˥]，剩[t͡seŋ˨]低[tɐi̯˥]嘅[kɛː˧]嘢[jɛː˩˧]我[ŋɔː˩˧]會[wuːi̯˩˧]搞[kaːu̯˧˥]掂[tiːm˨]㗎[kaː˧]喇[laː˧]。"
        self.assertEqual(result, expected)

    def test_get_ipa_text(self):
        result = ToJyutping.get_ipa_text("咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。")
        expected = 'kɐm˧.ŋaːm˥.lou̯˩˧.sɐi̯˧.jiːu̯˥.kʰɐu̯˨˩.kʰɵy̑˩˧.tɐŋ˧˥.t͡sɐn˨.jiːu̯˧.hɔːi̯˥.wuːi̯˧˥ | t͡seŋ˨.tɐi̯˥.kɛː˧.jɛː˩˧.ŋɔː˩˧.wuːi̯˩˧.kaːu̯˧˥.tiːm˨.kaː˧.laː˧'
        self.assertEqual(result, expected)

    def test_get_ipa_candidates(self):
        result = ToJyutping.get_ipa_candidates("咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。")
        expected = [('咁', ['kɐm˧', 'kɐm˧˥', 'kɐm˥', 'kɐm˨˩']), ('啱', ['ŋaːm˥', 'aːm˥', 'ɐm˥', 'ŋɐm˥']), ('老', ['lou̯˩˧', 'lou̯˧˥']), ('世', ['sɐi̯˧', 'sɐi̯˧˥']), ('要', ['jiːu̯˥', 'jiːu̯˧', 'jiːu̯˧˥']), ('求', ['kʰɐu̯˨˩']), ('佢', ['kʰɵy̑˩˧', 'hɵy̑˩˧']), ('等', ['tɐŋ˧˥']), ('陣', ['t͡sɐn˨', 't͡sɐn˧˥']), ('要', ['jiːu̯˧', 'jiːu̯˧˥', 'jiːu̯˥']), ('開', ['hɔːi̯˥']), ('會', ['wuːi̯˧˥', 'wuːi̯˩˧', 'wuːi̯˨', 'wuːi̯˧', 'kʰuːi̯˧˥', 'kʰuːi̯˧', 'kʷʰuːi̯˧˥']), ('，', []), ('剩', ['t͡seŋ˨', 'seŋ˨']), ('低', ['tɐi̯˥']), ('嘅', ['kɛː˧', 'kɛː˧˥', 'kʰɔːi̯˧˥', 'kʰɔːi̯˧']), ('嘢', ['jɛː˩˧', 'ɛː˩˧']), ('我', ['ŋɔː˩˧', 'ɔː˩˧']), ('會', ['wuːi̯˩˧', 'wuːi̯˨', 'wuːi̯˧˥', 'wuːi̯˧', 'kʰuːi̯˧˥', 'kʰuːi̯˧', 'kʷʰuːi̯˧˥']), ('搞', ['kaːu̯˧˥']), ('掂', ['tiːm˨', 'tiːm˧', 'tiːm˥']), ('㗎', ['kaː˧', 'kɐ˧', 'kaː˧˥', 'kaː˥', 'kaː˨˩']), ('喇', ['laː˧', 'laː˥', 'laːk̚˧', 'laː˩˧', 'laːt̚˧']), ('。', [])]
        self.assertEqual(result, expected)

    def test_g2p(self):
        result = ToJyutping.g2p("咁啱老世要求佢等陣要開會，剩低嘅嘢我會搞掂㗎喇。")
        expected = [(9, 32, 89), (11, 23, 87), (8, 58, 91), (18, 30, 89), (19, 49, 87), (10, 31, 90), (10, 79, 91), (5, 34, 88), (16, 33, 92), (19, 49, 89), (15, 57, 87), (14, 66, 88), (16, 52, 92), (5, 30, 87), (9, 38, 89), (19, 38, 91), (11, 56, 91), (14, 66, 91), (9, 22, 88), (5, 50, 92), (9, 20, 89), (8, 20, 89)]
        self.assertEqual(result, expected)

    def test_jyutping2ipa(self):
        result = ToJyutping.jyutping2ipa("cin1 ngaa5")
        expected = "t͡sʰiːn˥.ŋaː˩˧"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
