import random
import wikipedia


wiki_pages = ["Linus Torvalds"]



class SentenceGenerator(object):
    def __init__(self):
        self.words = {}

    def parse(self, words):
        word_list = words.split(" ")
        for i, word in enumerate(word_list):
            if word not in self.words:
                self.words[word] = {}
            if i < (len(word_list) - 1):
                if word_list[i+1] not in self.words[word]:
                    self.words[word][word_list[i+1]] = 0
                self.words[word][word_list[i+1]] += 1

    def make_sentence(self, start_word=""):
        if not start_word:
            start_word = random.choice(list(self.words))
        if start_word not in self.words:
            return ("Initial word not in list of words")
        sentence = [start_word]
        cur_word = start_word

        while(not "." in cur_word):
            choices = []
            for choice in self.words[cur_word]:
                for i in range(self.words[cur_word][choice]):
                        choices.append(choice)
            cur_word = random.choice(choices)
            sentence.append(cur_word)

        return " ".join(sentence)

    def parse_file(self, filename):
        with open(filename) as f:
            s = f.read().replace("\n", "")
            self.parse(s)

    def parse_wiki_page(self, page=""):
        if not page:
            page = random.choice(wiki_pages)
        p = wikipedia.page(page)
        self.parse(p.content.replace("\n", "").replace("==",""))

    def reset(self):
        del(self.words)


