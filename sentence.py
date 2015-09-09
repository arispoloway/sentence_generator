import random
import wikipedia
import time

class SentenceGenerator(object):
    def __init__(self):
        self.words = {}
        self.entry_points = []

    def parse(self, words):
        word_list = words.split(" ")
        for i, word in enumerate(word_list):
            if word not in self.words:
                self.words[word] = {}
            if i < (len(word_list) - 1):
                if word_list[i+1] not in self.words[word]:
                    self.words[word][word_list[i+1]] = 0
                self.words[word][word_list[i+1]] += 1
            if i > 0:
                if word_list[i - 1].endswith("."):
                    if word not in self.entry_points:
                        self.entry_points.append(word)
        self.recompute_probabilities()

    def recompute_probabilities(self):
        self.probabilities = {}
        for word in self.words:
            word_prob = []
            total = 0
            for w in self.words[word]:
                total += self.words[word][w]
            prob = 0.0
            for w in self.words[word]:
                prob += float(self.words[word][w])/float(total)
                word_prob.append( (w, prob) )
            self.probabilities[word] = word_prob

    def make_sentence(self, start_word=""):
        if not start_word:
            start_word = random.choice(self.entry_points if len(self.entry_points) > 0 else self.words)
        if start_word not in self.words:
            return ("Initial word not in list of words")
        sentence = [start_word]
        cur_word = start_word
        while not cur_word.endswith("."):
            rand = random.random()

            for choice in self.probabilities[cur_word]:
                if rand < choice[1]:
                    break
            cur_word = choice[0]
            sentence.append(cur_word)

        return " ".join(sentence).encode('ascii', 'ignore')

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


    @staticmethod
    def create_wiki_generators(wiki_list, debug=False):
        sentence_generators = []
        for page in wiki_list:
            sentence_generators.append( (page, SentenceGenerator()) )
            try:
                time_start = time.time()
                sentence_generators[-1][1].parse_wiki_page(page)

                if debug:
                    print("Took {1} Seconds to load Wikipedia Page \"{0}\" ".format(page, str(time.time()-time_start)[:5]))
            except:
                del(sentence_generators[-1])
                if debug:
                    print("Failed to load Wikipedia Page \"{0}\" ".format(page.replace("\n", "")))

        return sentence_generators



