"""

"""

import json
from difflib import get_close_matches
from difflib import SequenceMatcher


class Dictionary:
    """
    Dictionary is a class
    """
    def __init__(self):
        self.data = json.load(open("./data/wordsDefinitions.json"))

    def loaddata(self):
        self.data = json.load(open("data.json"))

    def nearestWordFound(self, word):
        '''This funcion looks on the dictionary the most similar word.

        Params:
            self -
            word - contains a word not in dictionaty to look for similarities

        Returns:
            Words with similarity selected on cutoff
        '''
        return get_close_matches(word, self.data.keys(), cutoff=0.7)

    def wordOptions(self, SimilarWords):
        ''' This function is called after "get_close_matches" to deal with
        the different options given a group of words similar to the word written
             This funcition handles the presentation of options so that the user
        can choose what to do.

        Params:
            SimilarWords - a group of words similar to a user written word that
                is not in the Dictionary


        Returns:
            Definitions for a word or an 'Error'
        '''

        msg = "The word you are looking for does not exist. \nI have found"
        msg= msg+" these words with a familiarity > 70%: "
        print(msg)

        for num, word in enumerate(SimilarWords):
            print("  {0}".format(SimilarWords[num]))
        inputWord = input("Type word you are looking for: ")
        if (inputWord in self.data.keys()):
            return self.data[inputWord]
        else:
            return "Error"

    def searchDefinition(self, word):
        '''Given a word it looks for it definition or for similar words.

        Params:
            self -
            word - It is a word written by the user to look for its definition

        Returns:
            True, results:
                If the word was found
                Results: returns the definitions (1-99) for a word
            False,  msgError:
                If the word was not found
                msgError: the reason for an error
        '''
        msgError = "Sorry, that word is not in the dictionary. Try again"
        #myword = word.lower()
        if word in self.data.keys():
            #Word in the dict. One to many definitions possible.
            return  True,self.data[word]
        elif len(get_close_matches(word, self.data.keys(), cutoff=0.7))>0:
            #Word not in the dict. Look for similar words
            closestWords = get_close_matches(word,
                                             self.data.keys(),
                                             cutoff=0.7)
            results = self.wordOptions(closestWords)
            if results =="Error":
                return False, msgError
            return True, results
        else:
            # Word not in dict and there are no similar words.
            return False ,msgError

    def getUserWishToContinue(self):
        """Gathers the wish of a user to continue or finish the program.
        This function doesn't end until the user message has been understood.

        Returns:
            True: if user want to finish
            False: If user wish to continue
        """
        yes = {'yes','y', 'ye', ''}
        no = {'no','n'}
        while True:
            choice = str(input("\nDo you want to look for another word? (y/n): "))
            if choice in yes:
               return True
            elif choice in no:
               return False
            else:
               print("Please respond with 'yes' or 'no'")
