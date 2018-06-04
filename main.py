
from Dictionary import Dictionary

if __name__=="__main__":
    myEnglishDictionary = Dictionary()
    userChoice = True
    while userChoice:
        word = str(input('\nEnter the word you are looking for: '))
        found,wordDefs = myEnglishDictionary.searchDefinition(word)
        #found may be True or False. It depends on whether the word exist
        #wordDefs contains the definition/s of a word
        if found:
          print("Definitions:")
          for definition in wordDefs:
                print("->", definition)
        else:
            print(wordDefs)
        userChoice = myEnglishDictionary.getUserWishToContinue()
