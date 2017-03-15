import sys
import os

def parseCommandLine(argv):
        input_string = ""
        if len(argv) > 1:
            if os.path.isfile(argv[1]):
                with open(argv[1],'r') as input_file:
                    input_string = input_file.read()
            else:
                input_string = argv[1]

        return input_string

def printSentence(sentence,argv):
    if len(argv) > 2:
        with open(argv[2],'w') as output_file:
            output_file.write(sentence)
    else:
        print(sentence)

def isVowel(ch):
   if "aeiou".count(ch) >= 1:
      return True
   else:
      return False

def translateToPig(sentenceInEnglish):
    #Recieve a sentence, return the piglatin translation.
    sentenceInPig = ""

    #Split into seperate lines
    linesInEnglish = sentenceInEnglish.splitlines()
    for linenumber, line in enumerate(linesInEnglish):

      # Add newline
      if linenumber > 0:
        sentenceInPig=sentenceInPig+"\n"

      #Split on whitespace
      wordsInEnglish = line.split()
      for wordnumber, word in enumerate(wordsInEnglish):

        #Add whitespace
        if wordnumber > 0:
          sentenceInPig=sentenceInPig+" "

        sentenceInPig=sentenceInPig+translateWordToPig(word)

    return sentenceInPig

def translateWordToPig(wordInEnglish):
    #Receive a single word, return the piglatin translation.
    cap=wordInEnglish.istitle()
    wordInEnglish = wordInEnglish.lower()      
    #cap=wordInEnglish.istitle()       
    #wordInEnglish=wordInEnglish
    if not isVowel(wordInEnglish[0]):
       #word starts with a consonant, find index for first vowel
       i=[isVowel(ch) for ch in wordInEnglish].index(True)

       #move consonants in front of vowel to end and add "ay" at the end
       wordInPig=wordInEnglish[i:]+wordInEnglish[0:i]+'ay'

       if cap:
          wordInPig=wordInPig.capitalize()

       return wordInPig
    #word starts with a vowel
    elif isVowel(wordInEnglish[0]):
       wordInPig = wordInEnglish+'way'

       if cap:
          wordInPig=wordInPig.capitalize()
       return wordInPig
    else:
       return ""

if __name__ == "__main__":
    sentence = parseCommandLine(sys.argv)
    printSentence(translateToPig(sentence),sys.argv)
