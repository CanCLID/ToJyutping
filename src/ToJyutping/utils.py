import re

punct_dict = dict(
	zip(
		'''!"'(),-./:;?[]{}~·‐‑‒–—―‘’“”…⋮⋯⸱⸳⸺⸻、。〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟・︐︑︒︓︔︕︖︗︘︙︱︲︵︶︷︸︹︺︻︼︽︾︿﹀﹁﹂﹃﹄﹇﹈﹐﹑﹒﹔﹕﹖﹗﹘﹙﹚﹛﹜﹝﹞﹣！＂＇（），－．／：；？［］｛｝～｟｠｡｢｣､･''',
		'''!"'(),-./:;?[]{}~·------‘’“”………··--,.‘’“”“”‘’[][][][][]~“””·,,.:;!?[]…--(){}[][]“”‘’“”‘’[],,.;:?!-(){}[]-!"'(),-./:;?[]{}~().“”,·'''
	)
)

left_bracket = '([{‘“'
right_bracket = ')]}’”'
left_bracket_to_right = dict(zip(left_bracket, right_bracket))
left_punct = left_bracket
right_punct = f'!,.:;?…{right_bracket}'
other_punct = '''"'·-~'''
decimal_separators = '''',.·⸱⸳﹒＇．'''
digits = '0０𝟎𝟘𝟢𝟬𝟶🯰1１𝟏𝟙𝟣𝟭𝟷🯱2２𝟐𝟚𝟤𝟮𝟸🯲3３𝟑𝟛𝟥𝟯𝟹🯳4４𝟒𝟜𝟦𝟰𝟺🯴5５𝟓𝟝𝟧𝟱𝟻🯵6６𝟔𝟞𝟨𝟲𝟼🯶7７𝟕𝟟𝟩𝟳𝟽🯷8８𝟖𝟠𝟪𝟴𝟾🯸9９𝟗𝟡𝟫𝟵𝟿🯹'

def format_romanization_text(s, conv):
  def inner(m):
    t = [None]
    d = [False]
    for k, v in conv(m[0]):
      if v:
        t += [v]
        d += [False]
      elif not k.isspace():
        t += [punct_dict.get(k, '')]
        d += [None if k in decimal_separators else k in digits]
    t += [None]
    d += [False]
    l = ''
    b = ''
    for i, (p, c, n) in enumerate(zip(t, t[1:], t[2:]), 1):
      def between():
        nonlocal t, i
        j = i - 1
        while j and t[j] and t[j] in right_bracket:
          j -= 1
        f = j and t[j] and len(t[j]) > 1
        j = i + 1
        while j < len(t) - 1 and t[j] and t[j] in left_bracket:
          j += 1
        g = j and t[j] and len(t[j]) > 1
        return f and g

      def lspace():
        nonlocal l
        if l and l[-1] not in f' {left_punct}{other_punct}':
          l += ' '

      def rspace():
        nonlocal n, l
        if not n or n not in f'{right_punct}{other_punct}':
          l += ' '

      if len(c) > 1:
        lspace()
        l += c
        rspace()
      elif not c:
        if not l.endswith('[…]'):
          l += '[…]'
      elif d[i] is None and d[i - 1] and d[i + 1]:
        continue
      elif c in left_punct:
        lspace()
        l += c
        b += left_bracket_to_right[c]
      elif c in right_punct:
        l += c
        rspace()
        try:
          b = b[:b.rindex(c)]
        except ValueError:
          pass
      elif c == '-':
        if p == '-':
          continue
        if n == '-' or between():
          l += ' – '
        else:
          l += c
      elif c == '~':
        if p == '~' and n != '~' or between():
          l += '~ '
        else:
          l += c
      elif c == '·':
        l += c
      else:
        j = len(b) - 1
        y = False
        while j >= 0 and b[j] not in right_bracket:
          if b[j] == c:
            y = True
            break
          j -= 1
        if y:
          b = b[:j]
          l += c
          rspace()
        else:
          lspace()
          l += c
          b += c
    return ' '.join(l.split())

  return re.sub(r'[^\0-\x1f\x80-\x9f]+', inner, s)

major_break = '.!?…'
minor_break = ',:;-~()[]{}'

def format_ipa_text(s, conv):
  def inner(m):
    t = []
    d = []
    for k, v in conv(m[0]):
      if v:
        t += [v]
        d += [False]
      elif not k.isspace():
        t += [punct_dict.get(k, '')]
        d += [None if k in decimal_separators else k in digits]
    l = []
    for i, c in enumerate(t):
      if len(c) > 1:
        l += [c]
      elif not c:
        if not l or l[-1] != '⸨…⸩':
          l += ['⸨…⸩']
      elif l:
        if d[i] is None and i and d[i - 1] and i < len(d) - 1 and d[i + 1]:
          continue
        if c in major_break:
          if len(l[-1]) > 1:
            l += ['‖']
          else:
            l[-1] = '‖'
        elif c in minor_break and len(l[-1]) > 1:
            l += ['|']
    if len(l[-1]) == 1:
      l.pop()
    s = ''
    for i, c in enumerate(l):
      s += c
      if i < len(l) - 1:
        n = l[i + 1]
        if c != '⸨…⸩' and len(c) > 1 and n != '⸨…⸩' and len(n) > 1:
          s += '.'
        else:
          s += ' '
    return s

  return re.sub(r'[^\0-\x1f\x80-\x9f]+', inner, s)
