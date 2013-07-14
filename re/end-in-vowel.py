import re

words = '''Born in New York City in 1918, Richard Feynman earned a
bachelor's degree at MIT in 1939, and a doctorate from Princeton in
1942. After working on the Manhattan Project in Los Alamos during
World War II, he became a professor at CalTech in 1951.  Feynman won
the 1965 Nobel Prize in Physics for his work on quantum
electrodynamics, and served on the commission investigating the
Challenger disaster in 1986.'''.split()

end_in_vowel = set()
for w in words:
    if re.search(r'[aeiou]\b', w):
        end_in_vowel.add(w)
for w in end_in_vowel:
    print w
