import sentence
import time

print("Starting Wiki Game\n")

wiki_pages = []

with open("wikipedia_pages.txt") as pages:
    for line in pages:
        wiki_pages.append(line.replace("\n", ""))

sentence_generators = sentence.SentenceGenerator.create_wiki_generators(wiki_pages, True)


for gen in sentence_generators:
    print(gen[0])
    print(gen[1].make_sentence())
    print
