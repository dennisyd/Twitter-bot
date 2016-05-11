import nltk
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn
import random
from time import time


class RndSentence:

    def __init__(self):
        t0 = time()
        print 'initalizing random word generator'

        self.s_articles = ['A', 'The']
        self.o_articles = ['a','the']
        self.prepositions = ['of','in','to','for','with','on','at','from','by',
        'about','as','into','like','through','after','over','out','around']

        self.nouns = list(wn.all_synsets(wn.NOUN))
        self.verbs = list(wn.all_synsets(wn.VERB))
        self.adjectives = list(wn.all_synsets(wn.ADJ))
        self.adverbs = list(wn.all_synsets(wn.ADV))
        t1 = time()
        runTime = t1-t0
        print 'word list initalized in ' + str(runTime) + ' seconds'

    def getVerb(self):
        word = self.verbs[self.rndNum(self.verbs)]
        verb = self.fetchWord(word)
        #print 'verb: ' + verb
        return str(verb)

    def getAdjective(self):
        word = self.adjectives[self.rndNum(self.adjectives)]
        adjective = self.fetchWord(word)
        #print 'adjective: ' + adjective
        return str(adjective)

    def getNoun(self):
        word = self.nouns[self.rndNum(self.nouns)]
        noun = self.fetchWord(word)
        #print 'noun: ' + noun
        return str(noun)

    def getAdverb(self):
        word = self.adverbs[self.rndNum(self.adverbs)]
        adverb = self.fetchWord(word)
        #print 'adverb: ' + adverb
        return str(adverb)

    def getPreposition(self):
        rnd = self.rndNum(self.prepositions)
        preposition = self.prepositions[rnd]
        return str(preposition)

    def getStartArticle(self):
        rnd = self.rndNum(self.s_articles)
        s_article = self.s_articles[rnd]
        return str(s_article)

    def getOtherArticle(self):
        rnd = self.rndNum(self.o_articles)
        o_article = self.o_articles[rnd]
        return str(o_article)


    def fetchWord(self, word):
        word = word.name().partition('.')[0]
        word = word.replace('_','')
        #print 'word in fetchWord: ' + str(word)
        return word

    def rndNum(self,listToParse):
        rnd = random.randint(0,len(listToParse)-1)
        #print 'random number generated: ' + str(rnd)
        return rnd

    #Generates a sentence of the form:
    #Article Noun Verb Preposition Article Noun
    def sentence_N_V_P_N(self):
        Tweet = self.getStartArticle() + ' ' + self.getNoun() + ' ' + self.getVerb() + 'ed ' + self.getPreposition() + ' ' + self.getOtherArticle() + ' ' + self.getNoun() + '.'
        while (len(Tweet) > 35):
            Tweet = self.getStartArticle() + ' ' + self.getNoun() + ' ' + self.getVerb() + 'ed ' + self.getPreposition() + ' ' + self.getOtherArticle() + ' ' + self.getNoun() + '.'

        #print Tweet
        return str(Tweet)
        #print 'len: ' + str(len(Tweet))

    def rndCriticReview(self):
        Tweet = str(self.sentence_N_V_P_N())
        Critic = 'One critic said \"' + Tweet +'\"'
        print Critic
        return str(Critic)


if __name__ == '__main__':
    sentence = RndSentence()
    i = 10
    for x in range(0,i):
        sentence.rndCriticReview()
