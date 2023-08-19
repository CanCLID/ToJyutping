import jiwer
import ToJyutping
import re

sentences = []

with open("jyutping_sentences_filtered.txt", "r") as f:
    lines = [line for line in f.readlines() if len(line.strip()) > 0]
    for i in range(0, len(lines), 2):
        yue = lines[i].strip()
        jyutping = lines[i + 1].strip()
        sentences.append((yue, jyutping))

def diff_by_tone_only(reference: str, hypothesis: str) -> bool:
    return (len(reference) == len(hypothesis) and \
            all(((r.isdigit() and h.isdigit()) if r != h else True for r, h in zip(reference, hypothesis))))

assert(diff_by_tone_only("gwong5 dung1 waa2", "gwong5 dung1 waa6"))
assert(not diff_by_tone_only("gwong5 dung1 wa2", "gwong5 dung1 waa6"))

assert(not diff_by_tone_only("waa2 si6", "waa6 sa6"))

def diff_by_a(str1: str, str2: str) -> bool:
    if abs(len(str1) - len(str2)) != 1:
        return False
    
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    
    mismatch_found = False
    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if mismatch_found or str1[i] != 'a':
                return False
            mismatch_found = True
            i += 1
        else:
            i += 1
            j += 1

    return mismatch_found or (i < len(str1) and str1[i] == 'a')

assert(diff_by_a("jau1 hak1", "jau1 haak1"))
assert(diff_by_a("jau1 haak1", "jau1 hak1"))
assert(not diff_by_a("jau2 hak1", "jau1 hak1"))

def normalize_nei_to_ni(s: str) -> str:
    return s.replace("nei1", "ni1")

assert(normalize_nei_to_ni("nei1") == "ni1")
assert(normalize_nei_to_ni("ni1") == "ni1")
assert(normalize_nei_to_ni("nei2") == "nei2")
assert(normalize_nei_to_ni("ni2") == "ni2")
assert(normalize_nei_to_ni("nin1") == "nin1")

def remove_ng_onset(s: str) -> str:
    return re.compile(r"\bng([^1-6])").sub(r"\1", s)

assert(remove_ng_onset("ngo5") == "o5")
assert(remove_ng_onset("ngong6") == "ong6")
assert(remove_ng_onset("ong4") == "ong4")
assert(remove_ng_onset("ng4") == "ng4")

def run_benchmark():
    wrong_sentences = []
    correct_sentences = []
    total_wer = 0

    print("Total sentences: " + str(len(sentences)))

    for (yue, reference) in sentences:
        hypothesis = ToJyutping.get_jyutping_text(yue)
        sentence_wer = jiwer.wer(reference, hypothesis)
        if sentence_wer > 0:
            total_wer += sentence_wer
            wrong_sentences.append((yue, reference, hypothesis))
        else:
            correct_sentences.append((yue, reference))
    micro_wer = total_wer / len(sentences)
    print("{:.2f}%".format(micro_wer * 100))
    with open("tojyutping_wrong_sentences.txt", "w+") as f:
        for (yue, reference, hypothesis) in wrong_sentences:
            reference = remove_ng_onset(normalize_nei_to_ni(reference))
            hypothesis = remove_ng_onset(normalize_nei_to_ni(hypothesis))
            if reference == hypothesis or \
                diff_by_tone_only(reference, hypothesis) or \
                diff_by_a(reference, hypothesis):
                    continue
            f.write("yue: " + yue + "\n")
            f.write("ref: " + reference + "\n")
            f.write("hyp: " + hypothesis + "\n")
            f.write("\n")
    with open("tojyutping_correct_sentences.txt", "w+") as f:
        for (yue, reference) in correct_sentences:
            f.write("yue: " + yue + "\n")
            f.write("ref: " + reference + "\n")
            f.write("\n")

if __name__ == "__main__":
    run_benchmark()
