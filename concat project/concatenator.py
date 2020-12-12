import itertools

with open('translation.txt', encoding='utf-8') as inp, open('translationFixed.txt', 'w', encoding='utf-8') as out:
	for line in inp:
		if not line.strip(): continue
		out.write(line)  

with open('spanish.txt', encoding='utf-8') as inp, open('spanishFixed.txt', 'w', encoding='utf-8') as out:
	for line in inp:
		if not line.strip(): continue
		out.write(line)  

with open ('spanishFixed.txt', 'r', encoding='utf-8') as f1, open ('translationFixed.txt', 'r', encoding='utf-8') as f2, open ('final.txt', 'w', encoding='utf-8') as of:
	for line_from_first, line_from_second in itertools.zip_longest(f1, f2):
		if line_from_first is not None:
			of.write(line_from_first)
		if line_from_second is not None:
			of.write(line_from_second)