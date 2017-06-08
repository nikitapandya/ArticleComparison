#Final Project !!
#name: Nikita Pandya
#email: npandy18@bu.edu
#
#
#HELPER FUNCTON clean_text

from math import *

def clean_text(txt):
    '''This function takes a string of text txt as a
       parameter and returns a list containing the words
       in txt after it has been “cleaned”.'''
    s = txt.lower()

    for char in s:
        
        if char == '.':
            s = s.replace('.', '')
        elif char == ',':
            s = s.replace(',', '')
        elif char == '?':
            s = s.replace('?', '')
        elif char == '!':
            s = s.replace('!', '')
        elif char == ':':
            s = s.replace(':', '')
        elif char == '-':
            s = s.replace('-', '')
        elif char == '"':
            s = s.replace('"', '')
        elif char == "'":
            s = s.replace("'", '')
        elif char == "(":
            s = s.replace("(", '')
        elif char == ")":
            s = s.replace(")", '')
    return s
#
#
#HELPER FUNCTON stem
def stem(word):
    '''This function accepts a string 's' as a parameter
       and then returns the stem of 's'.'''
    word = word.lower()
    
    #'UN' case
    if word[:2] == 'un':
        word = word[2:]
        return stem(word)

    #'RE' case
    elif word[:2] == 're' and len(word) > 4:
        word = word[2:]
        return stem(word)
    
    #"PRE" case 
    elif word[:3] == 'pre':
        word = word[3:]
        return stem(word)

    #'ING' case
    elif word[-3:] == 'ing' and len(word) > 5:
            word = word[:-3]
            return stem(word)
        
    #'IER' case
    elif word[-3:] == 'ier':
        word = word[:-3] + "y"
        return stem(word)
    
    #'IERS' case
    elif word[-4:] == 'iers':
        word = word[:-4] + 'y'
        return stem(word)

    #ERS case
    elif word[-3:] == 'ers' and len(word) > 5:
            word = word[:-3]
            return stem(word)
    
    #'ER' case
    elif word[-2:] == 'er' and len(word) > 5:
            word = word[:-2]
            return stem(word)
            
    #'IES' case
    elif word[-3:] == 'ies':
            word = word[:-3] + 'y'
            return stem(word)
 

    #Double letter condition/"SS" case
    elif len(word) > 2 and word[-1] == word[-2]:
        if word[-2:] == "ss":
            word = word
        else:
            word = word[:-1]
            return stem(word)
    
    #'ED' case
    elif word[-2:] == 'ed':
        word = word[:-2]
        return stem(word)

    return word
#
#
#
class TextModel:

    def __init__(self, model_name):
        '''This method constructs a new TextModel object by accepting
           a string model_name as a parameter and initializing the five
           following attributes.'''
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
#
#
#
    def __str__(self):
        '''This method returns a string that includes
           the name of the model as well as the sizes
           of the dictionaries for each feature of the text.'''

        s = "text model name: " + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        return s
#
#
#
    def __repr__(self):
        '''This method takes the TextModel self as input
           and returns a textual representation of the object.'''
        return self.__str__()
#
#
#
    def add_string(self, s):
        '''Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.'''
        
        #Updating sentence_lengths dictionary
        text = s.split(" ")
        count = 0
        for i in text:
            count += 1
            if "." in i or "?" in i or "!" in i:
                if count not in self.sentence_lengths:
                    self.sentence_lengths[count] = 1
                    count = 0
                else:
                    self.sentence_lengths[count] += 1
                    count = 0
        
        #The other three dictionaries are updated after the text is cleaned.
        words = clean_text(s)
        words = words.split(" ")

        #Updating words dictionary
        for w in words:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1

        #Updating word_lengths dictionary
        for w in words:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
                
        #Updating for stems
        for w in words:
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
            else:
                self.stems[stem(w)] += 1
            
#
#
#
    def add_file(self, filename):
        '''This method adds all of the text in the file
           identified by filename to the model.'''
        file = open(filename, 'r')
        text = file.read()
        self.add_string(str(text))
#
#
#
    def save_model(self):
        '''Saves the TextModel object self by writing its
           various feature dictionaries to files.'''
        #For Words
        filename1 = self.name + '_' + 'words'
        d1 = self.words
        f = open(filename1, 'w')
        f.write(str(d1))
        f.close()

        #For word lengths
        filename2 = self.name + '_' + 'word_lengths'
        d2 = self.word_lengths
        f = open(filename2, 'w')
        f.write(str(d2))
        f.close()
        
        #For sentence lengths
        filename3 = self.name + '_' + 'sentence_lengths'
        d3 = self.sentence_lengths
        f = open(filename3, 'w')
        f.write(str(d3))
        f.close()
        
        #For stems
        filename4 = self.name + '_' + 'stems'
        d4 = self.stems
        f = open(filename4, 'w')
        f.write(str(d4))
        f.close()
#
#
#
    def read_model(self):
        '''Reads the stored dictionaries for the called TextModel
           object from their files and assigns them to the attributes
           of the called TextModel.'''
        #For words
        filename1 = self.name + '_' + 'words'
        f = open(filename1, 'r')
        dict_str1 = f.read()
        f.close()
        self.words = eval(dict_str1)
        print('Inside the newly-read dictionary we have: ')
        print(dict_str1)

        #For word lengths
        filename2 = self.name + '_' + 'word_lengths'
        f = open(filename2, 'r')
        dict_str2 = f.read()
        f.close()
        self.word_lengths = eval(dict_str2)
        print('Inside the newly-read dictionary we have:')
        print(dict_str2)

        #For sentence lengths
        filename3 = self.name + '_' + 'sentence_lengths'
        f = open(filename3, 'r')
        dict_str3 = f.read()
        f.close()
        self.sentence_lengths = eval(dict_str3)
        print('Inside the newly-read dictionary we have: ')
        print(dict_str3)
        
        #For stems
        filename4 = self.name + '_' + 'stems'
        f = open(filename4, 'r')
        dict_str4 = f.read()
        f.close()
        self.stems = eval(dict_str4)
        print('Inside the newly-read dictionary we have: ')
        print(dict_str4)
#
#
#
    def similarity_score(self, other):
        '''Accepts a second TextModel object named other as a
           parameter and returns the log probability that the text
           from which the other model was derived is related to the
           text from which self‘s model was derived.'''
        scores = 0

        score_words = 0
        score_wordlen = 0
        score_senlen = 0
        score_stems = 0

        #For Words
        total_words = 0

        for i in self.words:
            total_words += self.words[i]

        for i in other.words:
            if i in self.words:
                a = self.words[i]/total_words
                b = other.words[i]*log(a)
                score_words += b
            else:
                score_words += other.words[i]*log(1/total_words)

        #For words lengths
        total_wordlen = 0

        for i in self.word_lengths:
            total_wordlen += self.word_lengths[i]

        for i in other.word_lengths:
            if i in self.word_lengths:
                a = self.word_lengths[i]/total_wordlen
                b = other.word_lengths[i]*log(a)
                score_wordlen += b
            else:
                score_wordlen += other.word_lengths[i]*log(1/total_wordlen)

        #For sentence lengths
        total_senlen = 0

        for i in self.sentence_lengths:
            total_senlen += self.sentence_lengths[i]

        for i in other.sentence_lengths:
            if i in self.sentence_lengths:
                a = self.sentence_lengths[i]/total_senlen
                b = other.sentence_lengths[i]*log(a)
                score_senlen += b
            else:
                score_senlen += other.sentence_lengths[i]*log(1/total_senlen)

        #For stems
        total_stems = 0

        for i in self.stems:
            total_stems += self.stems[i]

        for i in other.stems:
            if i in self.stems:
                a = self.stems[i]/total_stems
                b = other.stems[i]*log(a)
                score_stems += b
            else:
                score_stems += other.stems[i]*log(1/total_stems)

        scores = (0.35)*(score_words) + (0.35)*(score_wordlen) \
                 + (0.15)*(score_senlen) + (0.15)*(score_stems)
        
        return scores 
#We decided that words and word lengths should be weighted more than
#sentence length and stems. We believe that word and words lengths better
#characterize an author's writing style. Therefore, the scores of words and
#word lengths are each multiplied by 35%, while scores of sentence lengths
#and stems are each weighted 15%.  
#
def compare_texts():
    """A function to create text models and
       calculate similarity scores for bodies of text.
    """
    orig1 = TextModel('LOTR_Base')
    orig1.add_file('LOTR - Fellowship of the Rings (Base file).txt')

    orig2 = TextModel('GOT_Base')
    orig2.add_file('GOT - Pilot Episode (Base file).txt')

    new1 = TextModel('LOTR_Test')
    new1.add_file('LOTR - Return of the King.txt')
    score1 = orig1.similarity_score(new1)
    print("The similarity between LOTR-Fellowship of the Rings and",
          "LOTR-Return of the King is", score1)
    print()
    score2 = orig2.similarity_score(new1)
    print("The similarity between GOT-Pilot and",
          "LOTR-Return of the King 100 is", score2)
    print()
    print()

    new2 = TextModel('GOT_Test')
    new2.add_file('GOT - S4E2.txt')
    score3 = orig1.similarity_score(new2)
    print("The similarity between LOTR-Fellowship of the Rings and",
          "GOT-S4E2 is", score3)
    print()
    score4 = orig2.similarity_score(new2)
    print("The similarity between GOT-Pilot and GOT - S4E2 is", score4)
    print()
    print()

    new3 = TextModel('Star_Wars')
    new3.add_file('Star Wars - Revenge of the Sith.txt')
    score5 = orig1.similarity_score(new3)
    print("The similarity between LOTR-Fellowship of the Rings and",
          "Star_Wars is", score5)
    print()
    score6 = orig2.similarity_score(new3)
    print("The similarity between GOT-Pilot and Star_Wars is", score6)
    print()
    print()

    new4 = TextModel('Modern_Family')
    new4.add_file('Modern Family - S3E7 .txt')
    score7 = orig1.similarity_score(new4)
    print("The similarity between LOTR-Fellowship of the Rings and Modern_Family is", score7)
    print()
    score8 = orig2.similarity_score(new4)
    print("The similarity between GOT-Pilot and Modern_Family is", score8)
    print()
#
#
#
