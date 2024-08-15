if __package__:
    from .ToJyutping import ToJyutping, jyutping2ipa
    from .version import __version__
else:
    from ToJyutping import ToJyutping, jyutping2ipa
    from version import __version__

get_jyutping_list = ToJyutping.get_jyutping_list
get_jyutping = ToJyutping.get_jyutping
get_jyutping_text = ToJyutping.get_jyutping_text
get_jyutping_candidates = ToJyutping.get_jyutping_candidates
get_ipa_list = ToJyutping.get_ipa_list
get_ipa = ToJyutping.get_ipa
get_ipa_text = ToJyutping.get_ipa_text
get_ipa_candidates = ToJyutping.get_ipa_candidates
customize = ToJyutping.customize
g2p = ToJyutping.g2p
