import sentence

wiki_pages = []

with open("wikipedia_pages.txt") as pages:
    for line in pages:
        wiki_pages.append(line)

sentence_generators = []

for page in wiki_pages:
    sentence_generators.append(sentence.SentenceGenerator())
    try:
        sentence_generators[-1].parse_wiki_page(page)
    except:
        del(sentence_generators[-1])


for gen in sentence_generators:
    print(gen.make_sentence())
