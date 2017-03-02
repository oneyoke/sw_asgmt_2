import sys

def parseCommandLine(argv):
       return argv[1] if len(argv) > 1 else ""

def isVowel(ch):
   if "aeiou".count(ch) >= 1:
      return True
   else:
      return False


def translateToPig(wordInEnglish):
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
    print(translateToPig(sentence))
